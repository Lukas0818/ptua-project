from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

def contact_form_submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print("Vardas:", name)
        print("El. Pastas:", email)
        print("Žinutė:", message)

        response_data = {
            'status': 'success',
            'message': 'Forma sėkmingai pateikta.',
            'data': {
                'name': name,
                'email': email,
                'message': message,
            }
        }
        return JsonResponse(response_data)
    else:
        response_data = {
            'status': 'error',
            'message': 'Netinkamas užklausos metodas.',
        }
        return JsonResponse(response_data, status=405)

@login_required    
def about_us(request):
    return render(request, 'about_us.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def reviews(request):
    reviews_list = Review.objects.all().order_by('-date_posted')
    paginator = Paginator(reviews_list, 10)  # Rodo 10 atsiliepimų per puslapį

    page = request.GET.get('page')
    reviews = paginator.get_page(page)

    return render(request, 'reviews.html', {'reviews': reviews})


@login_required
def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.user.is_superuser or review.user.id == request.user.id:
        review.delete()
        messages.success(request, "Atsiliepimas sėkmingai ištrintas!")
    else:
        messages.error(request, "Neturite teisių ištrinti šio atsiliepimo!")

    return redirect('reviews')

