from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import PhysicalExam


class PhysicalExamForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = PhysicalExam
        fields = '__all__'
