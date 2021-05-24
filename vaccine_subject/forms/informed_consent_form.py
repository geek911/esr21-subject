from django import forms
from ..models import EligibilityCheckList


class InformedConsentForm(forms.ModelForm):

    class Meta:
        model = EligibilityCheckList
        fields = '__all__'
