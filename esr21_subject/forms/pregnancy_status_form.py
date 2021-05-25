from django import forms
from ..models import PregnancyStatus


class PregnancyStatusForm(forms.ModelForm):

    class Meta:
        model = PregnancyStatus
        fields = '__all__'
