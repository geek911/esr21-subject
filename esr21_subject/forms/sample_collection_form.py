from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import SampleCollection


class SampleCollectionForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = SampleCollection
        fields = '__all__'