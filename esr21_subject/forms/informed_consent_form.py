from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import InformedConsent


class InformedConsentForm(SiteModelFormMixin, FormValidatorMixin,
                          ConsentModelFormMixin, forms.ModelForm):

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False)

    class Meta:
        model = InformedConsent
        fields = '__all__'
