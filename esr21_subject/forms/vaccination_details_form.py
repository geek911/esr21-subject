from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import VaccinationDetails


class VaccinationDetailsForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = VaccinationDetails
        fields = '__all__'
