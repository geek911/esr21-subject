from django import forms

from ..models import RapidHIVTesting


class RapidHIVTestingForm(forms.ModelForm):

    class Meta:
        model = RapidHIVTesting
        fields = '__all__'
