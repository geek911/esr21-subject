from django import forms
from ..models import VaccinationDetails


class VaccinationDetailsForm(forms.ModelForm):

    class Meta:
        model = VaccinationDetails
        fields = '__all__'