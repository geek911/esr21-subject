from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import PregnancyStatus


class PregnancyStatusForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = PregnancyStatus
        fields = '__all__'
