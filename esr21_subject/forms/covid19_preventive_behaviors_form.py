from django import forms
from ..models import Covid19PreventiveBehaviors


class Covid19PreventiveBehaviorsForm(forms.ModelForm):

    class Meta:
        model = Covid19PreventiveBehaviors
        fields = '__all__'
