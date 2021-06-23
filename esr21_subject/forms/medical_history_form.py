from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import MedicalHistory, MedicalDiagnosis


class MedicalHistoryForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = '__all__'


class MedicalDiagnosisForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = MedicalDiagnosis
        fields = '__all__'
