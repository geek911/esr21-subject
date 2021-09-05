from django import forms

from .form_mixins import SubjectModelFormMixin
from esr21_subject_validation.form_validators import \
    RapidHivTestingFormValidator
from ..models import RapidHIVTesting


class RapidHIVTestingForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = RapidHivTestingFormValidator

    class Meta:
        model = RapidHIVTesting
        fields = '__all__'
