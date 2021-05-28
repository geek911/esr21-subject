from django import forms
from ..models import Hospitalization


class HospitalizationForm(forms.ModelForm):
    class Meta:
        model = Hospitalization
        fields = '__all__'
