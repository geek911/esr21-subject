from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Azd1222Vaccination


class Azd1222VaccinationForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = Azd1222Vaccination
        fields = '__all__'