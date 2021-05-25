from django import forms
from ..models import EligibilityConfirmation


class EligibilityConfirmationForm(forms.ModelForm):

    screening_identifier = forms.CharField(
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = EligibilityConfirmation
        fields = '__all__'
