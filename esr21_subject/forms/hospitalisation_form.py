from esr21_subject_validation.form_validators import HospitalisationFormValidator
from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Hospitalisation


class HospitalisationForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = HospitalisationFormValidator
    class Meta:
        model = Hospitalisation
        fields = '__all__'
