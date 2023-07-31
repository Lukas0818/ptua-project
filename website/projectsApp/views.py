from django.shortcuts import render

def projects(request):
    return render(request, 'projectsApp/projects.html')
