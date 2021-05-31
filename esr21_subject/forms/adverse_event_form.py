from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import AdverseEvent


class AdverseEventForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = AdverseEvent
        fields = '__all__'
