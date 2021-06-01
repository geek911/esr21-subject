from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..models import PersonalContactInfo


class PersonalContactInfoForm(SiteModelFormMixin, FormValidatorMixin,
                              forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = PersonalContactInfo
        fields = '__all__'
