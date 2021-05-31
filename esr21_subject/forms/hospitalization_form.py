from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Hospitalization


class HospitalizationForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = Hospitalization
        fields = '__all__'
