from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import Covid19PreventativeBehaviours


class Covid19PreventativeBehavioursForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = Covid19PreventativeBehaviours
        fields = '__all__'
