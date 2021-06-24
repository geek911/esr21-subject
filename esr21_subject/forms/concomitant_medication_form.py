from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import ConcomitantMedication


class ConcomitantMedicationForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = ConcomitantMedication
        fields = '__all__'
