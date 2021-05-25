from django import forms
from ..models import InformedConsent


class InformedConsentForm(forms.ModelForm):

    class Meta:
        model = InformedConsent
        fields = '__all__'
