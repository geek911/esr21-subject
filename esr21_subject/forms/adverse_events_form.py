from django import forms
from ..models import AdverseEvents


class AdverseEventsForm(forms.ModelForm):

    class Meta:
        model = AdverseEvents
        fields = '__all__'