from django import forms
from .models import Service, UserRentService, Category

class BaseServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'category']

class RentServiceForm(BaseServiceForm):
    class Meta(BaseServiceForm.Meta):
        fields = BaseServiceForm.Meta.fields + ['stock']

class SaleServiceForm(BaseServiceForm):
    pass

class RentForm(forms.ModelForm):
    class Meta:
        model = UserRentService
        fields = ['start_date', 'end_date']

class ServiceSearchForm(forms.Form):
    search_category = forms.ModelChoiceField(required=False, queryset=Category.objects.all(), label="Kategorija")
