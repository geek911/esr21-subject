from django import forms
from esr21_subject_validation.form_validators import ConcomitantMedicationFormValidator
from .form_mixins import SubjectModelFormMixin
from ..models import ConcomitantMedication


class ConcomitantMedicationForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = ConcomitantMedicationFormValidator

    class Meta:
        model = ConcomitantMedication
        fields = '__all__'
