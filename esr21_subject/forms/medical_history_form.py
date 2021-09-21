from esr21_subject_validation.form_validators import MedicalHistoryFormValidator

from django import forms
from django.apps import apps as django_apps
from edc_constants.constants import YES

from ..models import MedicalHistory, MedicalDiagnosis
from .form_mixins import SubjectModelFormMixin


class MedicalHistoryForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = MedicalHistoryFormValidator

    medical_diagnosis = 'esr21_subject.medicaldiagnosis'

    @property
    def medical_diagnosis_cls(self):
        return django_apps.get_model(self.medical_diagnosis)

    def clean(self):
        total_medical_diagnosis = int(self.data.get('medicaldiagnosis_set-TOTAL_FORMS'))
        relevant_history = self.data.get('relevant_history')
        if relevant_history == YES and total_medical_diagnosis == 0:
                msg = 'Participant has relevant medical history, '\
                f'{self.medical_diagnosis_cls._meta.verbose_name} is required'
                raise forms.ValidationError(msg)

    class Meta:
        model = MedicalHistory
        fields = '__all__'


class MedicalDiagnosisForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = MedicalDiagnosis
        fields = '__all__'
