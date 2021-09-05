from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import PregnancyTest
from esr21_subject_validation.form_validators import PregnancyTestFormValidator


class PregnancyTestForm(SubjectModelFormMixin, forms.ModelForm):
    form_validator_cls = PregnancyTestFormValidator

    class Meta:
        model = PregnancyTest
        fields = '__all__'
