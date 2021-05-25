from django import forms
from ..models import SeriousAdverseEvent


class SeriousAdverseEventForm(forms.ModelForm):

    class Meta:
        model = SeriousAdverseEvent
        fields = '__all__'
