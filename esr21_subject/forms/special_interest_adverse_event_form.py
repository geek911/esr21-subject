from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import SpecialInterestAdverseEvent


class SpecialInterestAdverseEventForm(SubjectModelFormMixin, forms.ModelForm):

    def has_changed(self):
        return True

    class Meta:
        model = SpecialInterestAdverseEvent
        fields = '__all__'
