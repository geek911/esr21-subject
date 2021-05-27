from django import forms
from ..models import Pregnancy


class PregnancyForm(forms.ModelForm):

    class Meta:
        model = Pregnancy
        fields = '__all__'
