from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from esr21_subject_validation.form_validators import PersonalContactInformationFormValidator
from ..models import PersonalContactInfo


class PersonalContactInfoForm(SiteModelFormMixin, FormValidatorMixin,
                              forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    form_validator_cls = PersonalContactInformationFormValidator

    class Meta:
        model = PersonalContactInfo
        fields = '__all__'
