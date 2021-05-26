from django import forms
from ..models import PhysicalExam


class PhysicalExamForm(forms.ModelForm):
    class Meta:
        model = PhysicalExam
        fields = '__all__'
