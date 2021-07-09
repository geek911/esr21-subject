from django import forms
from esr21_subject_validation.form_validators import PregnancyStatusFormValidator
from .form_mixins import SubjectModelFormMixin
from ..models import PregnancyStatus


class PregnancyStatusForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = PregnancyStatusFormValidator

    class Meta:
        model = PregnancyStatus
        fields = '__all__'
