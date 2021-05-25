from django import forms
from ..models import DemographicsData


class DemographicsDataForm(forms.ModelForm):

    class Meta:
        model = DemographicsData
        fields = '__all__'