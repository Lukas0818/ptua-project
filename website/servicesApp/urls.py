from django.urls import path
from . import views

app_name = 'servicesApp'

urlpatterns = [
    path('services_list/', views.services_list, name='services_list'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
    path('rent/<int:pk>/', views.rent_service, name='rent_service'),
    path('sale/<int:pk>/', views.sale_service, name='sale_service'),
    path('rented_services/', views.rented_services, name='rented_services'),
    path('rented_service_detail/<int:pk>/', views.rented_service_detail, name='rented_service_detail'),
    path('return_service/<int:pk>/', views.return_service, name='return_service'),
]
