from django import forms
from ..models import AdverseEvent


class AdverseEventForm(forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = AdverseEvent
        fields = '__all__'
