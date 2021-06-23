from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Covid19PreventiveBehaviors


class Covid19PreventiveBehaviorsForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = Covid19PreventiveBehaviors
        fields = '__all__'
