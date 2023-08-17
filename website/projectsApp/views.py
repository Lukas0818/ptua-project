from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import SearchForm
from django.contrib.auth.decorators import login_required


@login_required
def projects(request):
    projects = Project.objects.all()
    form = SearchForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data["search_name"]:
            projects = projects.filter(name__icontains=form.cleaned_data["search_name"])
        if form.cleaned_data["search_status"]:
            projects = projects.filter(status=form.cleaned_data["search_status"])
        if form.cleaned_data["search_category"]:
            projects = projects.filter(category=form.cleaned_data["search_category"])
    return render(
        request, "projectsApp/projects.html", {"projects": projects, "form": form}
    )


@login_required
def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "projectsApp/project_details.html", {"project": project})
