from django import forms
from . import models

class CarsForm(forms.ModelForm):
    class Meta:
        model = models.Cars
        fields = "__all__"