from django import forms
from esr21_subject_validation.form_validators import VitalSignsFormValidator
from .form_mixins import SubjectModelFormMixin
from ..models import VitalSigns


class VitalSignsForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = VitalSignsFormValidator

    class Meta:
        model = VitalSigns
        fields = '__all__'
