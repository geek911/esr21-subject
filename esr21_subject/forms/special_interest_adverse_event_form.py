from django import forms
from esr21_subject_validation.form_validators import SpecialInterestAdverseEventFormValidator

from .form_mixins import SubjectModelFormMixin
from ..models import SpecialInterestAdverseEvent


class SpecialInterestAdverseEventForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = SpecialInterestAdverseEventFormValidator

    def has_changed(self):
        return True

    class Meta:
        model = SpecialInterestAdverseEvent
        fields = '__all__'
