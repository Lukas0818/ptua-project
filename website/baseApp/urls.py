from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('contact_form_submit/', views.contact_form_submit, name='contact_form_submit'),
    path('about_us/', views.about_us, name="about_us"),
    path('profile/', views.profile, name="profile"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]