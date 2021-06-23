from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import PregnancyTest


class PregnancyTestForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = PregnancyTest
        fields = '__all__'
