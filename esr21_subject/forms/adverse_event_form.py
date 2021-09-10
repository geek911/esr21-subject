from django import forms
from edc_constants.constants import YES, NO
from esr21_subject_validation.form_validators import AdverseEventRecordFormValidator
from django.core.exceptions import ValidationError
from .form_mixins import SubjectModelFormMixin
from ..models import AdverseEvent, AdverseEventRecord


class AdverseEventForm(SubjectModelFormMixin, forms.ModelForm):
    class Meta:
        model = AdverseEvent
        fields = '__all__'


class AdverseEventRecordForm(SubjectModelFormMixin, forms.ModelForm):
    form_validator_cls = AdverseEventRecordFormValidator

    def clean(self):
        cleaned_data = super(AdverseEventRecordForm, self).clean()
        serious_event = cleaned_data.get('serious_event')
        serious_ae = self.data.get('seriousadverseevent_set-TOTAL_FORMS')

        if serious_event and serious_ae:
            """
            Null exception fix
            """
            if serious_event == YES and int(serious_ae) == 0:
                msg = {'serious_event':
                           'Please complete the serious adverse event table.'}
                raise forms.ValidationError(msg)
        elif serious_event == NO and int(serious_ae) != 0:
            msg = {'serious_event':
                       'This is not a serious AE, please *DO NOT* complete the '
                       'serious adverse event table.'}
            raise forms.ValidationError(msg)

        special_interest_ae = cleaned_data.get('special_interest_ae')
        aesi = self.data.get('specialinterestadverseevent_set-TOTAL_FORMS')

        if special_interest_ae and aesi:
            """
            Null exception fix
            """
            if special_interest_ae == YES and aesi and int(aesi) == 0:
                msg = {'special_interest_ae':
                           'Please complete the AEs of special interest table.'}
                raise forms.ValidationError(msg)
            elif special_interest_ae == NO and int(aesi) != 0:
                msg = {'special_interest_ae':
                           'This is not an AE of special interest, please *DO NOT* '
                           'complete the AEs of special interest table.'}
                raise forms.ValidationError(msg)


class Meta:
    model = AdverseEventRecord
    fields = '__all__'
