from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from esr21_subject_validation.form_validators import ScreeningEligibilityFormValidator
from ..models import ScreeningEligibility


class  ScreeningEligibilityForm(SiteModelFormMixin, FormValidatorMixin,
                                forms.ModelForm):

    form_validator_cls = ScreeningEligibilityFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = ScreeningEligibility
        fields = '__all__'
