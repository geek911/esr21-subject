from django import forms
from esr21_subject_validation.form_validators import SeriousAdverseEventFormValidator

from .form_mixins import SubjectModelFormMixin
from ..models import SeriousAdverseEvent


class SeriousAdverseEventForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = SeriousAdverseEventFormValidator

    def has_changed(self):
        return True

    class Meta:
        model = SeriousAdverseEvent
        fields = '__all__'
