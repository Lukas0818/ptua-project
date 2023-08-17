from django import forms
from .models import Review
from django.core.validators import MinValueValidator, MaxValueValidator


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta:
        model = Review
        fields = ["title", "content", "rating"]
