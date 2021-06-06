from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import SeriousAdverseEvent


class SeriousAdverseEventForm(SubjectModelFormMixin, forms.ModelForm):

    def has_changed(self):
        return True

    class Meta:
        model = SeriousAdverseEvent
        fields = '__all__'
