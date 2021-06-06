from esr21_subject_validation.form_validators import HospitalizationFormValidator
from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Hospitalization


class HospitalizationForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = HospitalizationFormValidator
    class Meta:
        model = Hospitalization
        fields = '__all__'
