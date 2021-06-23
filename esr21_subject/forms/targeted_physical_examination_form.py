from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import TargetedPhysicalExamination


class TargetedPhysicalExaminationForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = TargetedPhysicalExamination
        fields = '__all__'
