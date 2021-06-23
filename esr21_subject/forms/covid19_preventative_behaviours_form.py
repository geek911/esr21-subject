from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Covid19PreventativeBehaviors


class Covid19PreventativeBehaviorsForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = Covid19PreventativeBehaviors
        fields = '__all__'
