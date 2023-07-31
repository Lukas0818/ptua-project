from django import forms
from .models import Project, ProjectCategory

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status', 'category']

class SearchForm(forms.Form):
    search_name = forms.CharField(required=False, label="Pavadinimas")
    search_status = forms.ChoiceField(required=False, choices=[('','')] + list(Project.STATUS_CHOICES), label="Statusas")
    search_category = forms.ModelChoiceField(required=False, queryset=ProjectCategory.objects.all(), label="Kategorija")
