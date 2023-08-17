from django.urls import path
from . import views

app_name = "projectsApp"

urlpatterns = [
    path("projects/", views.projects, name="projects"),
    path("project/<int:pk>/", views.project_details, name="project_details"),
]
