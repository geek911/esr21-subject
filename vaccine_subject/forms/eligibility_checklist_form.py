from django import forms
from ..models import EligibilityCheckList


class EligibilityCheckListForm(forms.ModelForm):

    class Meta:
        model = EligibilityCheckList
        fields = '__all__'
