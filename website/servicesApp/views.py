from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, UserRentService, ReturnRequest
from .forms import RentServiceForm, SaleServiceForm, RentForm
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import date

from .forms import ServiceSearchForm

def services_list(request):
    form = ServiceSearchForm(request.GET)
    services = Service.objects.all()

    if form.is_valid():
        if form.cleaned_data['search_category']:
            services = services.filter(category=form.cleaned_data['search_category'])

    return render(request, 'servicesApp/services_list.html', {'services': services, 'form': form})


def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    template_name = 'servicesApp/rent_detail.html' if service.type == Service.RENT else 'servicesApp/sale_detail.html'
    return render(request, template_name, {'service': service})


def create_rent_service(request):
    form = RentServiceForm(request.POST or None)
    if form.is_valid():
        service = form.save(commit=False)
        service.type = Service.RENT
        service.save()
        return redirect('servicesApp:service_detail', pk=service.pk)
    return render(request, 'servicesApp/create_service.html', {'form': form})

def create_sale_service(request):
    form = SaleServiceForm(request.POST or None)
    if form.is_valid():
        service = form.save(commit=False)
        service.type = Service.SALE
        service.save()
        return redirect('servicesApp:service_detail', pk=service.pk)
    return render(request, 'servicesApp/create_service.html', {'form': form})

@csrf_exempt
def rent_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    user = request.user

    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            user_rent_service = form.save(commit=False)
            user_rent_service.service = service
            user_rent_service.user = user.username
            days = (user_rent_service.end_date - user_rent_service.start_date).days
            user_rent_service.total_price = days * service.price
            user_rent_service.save()
            service.stock -= 1
            service.save()
            return redirect('servicesApp:service_detail', pk=service.pk)
    else:
        start_date = datetime.date.today()
        end_date = start_date + timedelta(days=7)
        form = RentForm(initial={'start_date': start_date, 'end_date': end_date})

    return render(request, 'servicesApp/rent_form.html', {'service': service, 'form': form})

def rented_services(request):
    today = date.today()
    rented_services = UserRentService.objects.filter(returned=False, end_date__gte=today)
    return render(request, 'servicesApp/rented_services.html', {'rented_services': rented_services})

def rented_service_detail(request, pk):
    rented_service = get_object_or_404(UserRentService, pk=pk)
    return render(request, 'servicesApp/rented_service_detail.html', {'rented_service': rented_service})


def return_service(request, pk):
    rented_service = get_object_or_404(UserRentService, pk=pk)
    ReturnRequest.objects.create(rented_service=rented_service)
    return redirect('servicesApp:rented_services')

def admin_return_requests(request):
    if not request.user.is_staff:
        return redirect('servicesApp:services_list')
    return_requests = ReturnRequest.objects.filter(approved=None)
    return render(request, 'servicesApp/admin_return_requests.html', {'return_requests': return_requests})

def approve_return_request(request, pk):
    if not request.user.is_staff:
        return redirect('servicesApp:services_list')
    return_request = get_object_or_404(ReturnRequest, pk=pk)
    rented_service = return_request.rented_service
    rented_service.returned = True
    rented_service.service.stock += 1
    rented_service.service.save()
    return_request.approved = True
    return_request.save()
    rented_service.delete() 
    return redirect('servicesApp:admin_return_requests')


def deny_return_request(request, pk):
    if not request.user.is_staff:
        return redirect('servicesApp:services_list')
    return_request = get_object_or_404(ReturnRequest, pk=pk)
    return_request.approved = False
    return_request.save()
    return redirect('servicesApp:admin_return_requests')

@csrf_exempt
def sale_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if service.stock > 0:
        service.stock -= 1
        service.save()
    return redirect('servicesApp:service_detail', pk=service.pk)

def rented_services_log(request):
    rented_services = UserRentService.objects.all()
    return render(request, 'servicesApp/rented_services_log.html', {'rented_services': rented_services})
