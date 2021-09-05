from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from esr21_subject_validation.form_validators import EligibilityConfirmationFormValidator
from ..models import EligibilityConfirmation


class EligibilityConfirmationForm(SiteModelFormMixin, FormValidatorMixin,
                                  forms.ModelForm):

    form_validator_cls = EligibilityConfirmationFormValidator

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = EligibilityConfirmation
        fields = '__all__'
