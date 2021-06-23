from esr21_subject_validation.form_validators import DemographicsDataFormValidator
from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import DemographicsData


class DemographicsDataForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = DemographicsDataFormValidator

    class Meta:
        model = DemographicsData
        fields = '__all__'
