from django import forms

from .form_mixins import SubjectModelFormMixin
from esr21_subject_validation.form_validators import \
    TargetedPhysicalExamFormValidator
from ..models import TargetedPhysicalExamination


class TargetedPhysicalExaminationForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = TargetedPhysicalExamFormValidator

    class Meta:
        model = TargetedPhysicalExamination
        fields = '__all__'
