from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Pregnancy


class PregnancyForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = Pregnancy
        fields = '__all__'
