from typing import Type
from django import forms
from .import models
from .models import Play
from .models import Review
class CreatePlay(forms.ModelForm):
    class Meta:
        model = models.Play
        fields = ["title", "plot", "slug", "cast", "category", "image", "year"]

class CreateReview(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["text"]