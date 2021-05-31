from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import DemographicsData


class DemographicsDataForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = DemographicsData
        fields = '__all__'
