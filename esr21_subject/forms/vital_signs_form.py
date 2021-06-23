from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import VitalSigns


class VitalSignsForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = VitalSigns
        fields = '__all__'
