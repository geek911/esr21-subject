from django import forms
from esr21_subject_validation.form_validators import SeriousAdverseEventRecordFormValidator

from .form_mixins import SubjectModelFormMixin
from ..models import SeriousAdverseEvent, SeriousAdverseEventRecord


class SeriousAdverseEventForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = SeriousAdverseEvent
        fields = '__all__'


class SeriousAdverseEventRecordForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = SeriousAdverseEventRecordFormValidator

    def has_changed(self):
        return True

    class Meta:
        model = SeriousAdverseEventRecord
        fields = '__all__'
