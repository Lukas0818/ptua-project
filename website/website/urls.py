from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('baseApp.urls')),
    path('projectsApp/', include('projectsApp.urls')),
    path('servicesApp/', include('servicesApp.urls')),
]
