from django.urls import path
from . import views

app_name = 'projectsApp'

urlpatterns = [
    path('projects/', views.projects, name='projects'),
]
