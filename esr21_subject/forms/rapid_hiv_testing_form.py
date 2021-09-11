from dateutil.relativedelta import relativedelta
from django import forms
from django.core.exceptions import ValidationError
from .form_mixins import SubjectModelFormMixin
from esr21_subject_validation.form_validators import \
    RapidHivTestingFormValidator
from ..models import RapidHIVTesting
from edc_constants.constants import NO


class RapidHIVTestingForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = RapidHivTestingFormValidator

    def clean(self):
        rapid_test_result = self.cleaned_data.get('rapid_test_result')
        rapid_test_date = self.cleaned_data.get('rapid_test_date')
        hiv_test_date = self.cleaned_data.get('hiv_test_date')

        if self.instance.rapid_test_result and rapid_test_result:
            if rapid_test_result != self.instance.rapid_test_result:
                raise ValidationError(
                    'The rapid test result cannot be changed')
        if self.instance.rapid_test_date and rapid_test_date:
            if rapid_test_date != self.instance.rapid_test_date:
                raise ValidationError(
                    'The rapid test result date cannot be changed')

        subject_visit = self.cleaned_data.get('subject_visit')

        # import pdb; pdb.set_trace()
        if hiv_test_date:

            rapid_test_done = self.cleaned_data.get('rapid_test_done')

            date_diff = relativedelta(subject_visit.report_datetime.date(), hiv_test_date)

            if (date_diff.years or date_diff.months >= 3) and rapid_test_done == NO:
                message = {'rapid_test_done': 'Rapid test must be performed if participant\'s '
                           'previous hiv results are more than 3 months old.'}
                raise ValidationError(message)

        if rapid_test_date:

            date_diff = relativedelta(subject_visit.report_datetime.date(), rapid_test_date)

            if date_diff.years or date_diff.months >= 3:
                message = {'rapid_test_date': 'The date provided is more than 3 months old.'}
                raise ValidationError(message)

        super().clean()

    class Meta:
        model = RapidHIVTesting
        fields = '__all__'
