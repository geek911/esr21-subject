from django import forms
from edc_form_validators import FormValidatorMixin

from edc_lab.forms.modelform_mixins import RequisitionFormMixin

from ..models import SubjectRequisition


class SubjectRequisitionForm(RequisitionFormMixin,
                             FormValidatorMixin):

    requisition_identifier = forms.CharField(
        label='Requisition identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        super().clean()

    class Meta:
        model = SubjectRequisition
        fields = '__all__'
