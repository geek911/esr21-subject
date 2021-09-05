from django import forms
from esr21_subject_validation.form_validators import MedicalHistoryFormValidator
from .form_mixins import SubjectModelFormMixin
from ..models import MedicalHistory, MedicalDiagnosis


class MedicalHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MedicalHistoryFormValidator

    class Meta:
        model = MedicalHistory
        fields = '__all__'


class MedicalDiagnosisForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MedicalDiagnosis
        fields = '__all__'
