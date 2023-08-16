from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


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
