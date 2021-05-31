from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import RapidHIVTesting


class RapidHIVTestingForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = RapidHIVTesting
        fields = '__all__'
