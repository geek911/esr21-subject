from django import forms
from django.core.exceptions import ValidationError
from .form_mixins import SubjectModelFormMixin
from esr21_subject_validation.form_validators import \
    RapidHivTestingFormValidator
from ..models import RapidHIVTesting


class RapidHIVTestingForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = RapidHivTestingFormValidator

    def clean(self):
        rapid_test_result = self.cleaned_data.get('rapid_test_result')
        rapid_test_date = self.cleaned_data.get('rapid_test_date')

        if self.instance.rapid_test_result and rapid_test_result:
            if rapid_test_result != self.instance.rapid_test_result:
                raise ValidationError(
                    'The rapid test result cannot be changed')
        if self.instance.rapid_test_date and rapid_test_date:
            if rapid_test_date != self.instance.rapid_test_date:
                raise ValidationError(
                    'The rapid test result date cannot be changed')

        super().clean()

    class Meta:
        model = RapidHIVTesting
        fields = '__all__'
