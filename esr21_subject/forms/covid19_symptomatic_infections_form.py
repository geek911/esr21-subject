from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Covid19SymptomaticInfections


class Covid19SymptomaticInfectionsForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = Covid19SymptomaticInfections
        fields = '__all__'
