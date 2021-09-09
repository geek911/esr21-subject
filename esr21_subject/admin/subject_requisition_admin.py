from django.contrib import admin
from edc_lab.admin import RequisitionAdminMixin
from edc_lab.admin import requisition_verify_fields
from edc_lab.admin import requisition_verify_fieldset, requisition_status_fieldset
from edc_model_admin import audit_fieldset_tuple
from edc_senaite_interface.admin import SenaiteRequisitionAdminMixin

from ..admin_site import esr21_subject_admin
from ..forms import SubjectRequisitionForm
from ..models import SubjectRequisition
from .modeladmin_mixins import CrfModelAdminMixin

requisition_identifier_fields = (
    'requisition_identifier',
    'identifier_prefix',
    'primary_aliquot_identifier'
)

requisition_identifier_fieldset = (
    'Identifiers', {
        'classes': ('collapse',),
        'fields': (requisition_identifier_fields)})


@admin.register(SubjectRequisition, site=esr21_subject_admin)
class SubjectRequisitionAdmin(CrfModelAdminMixin, RequisitionAdminMixin,
                              SenaiteRequisitionAdminMixin, admin.ModelAdmin):

    form = SubjectRequisitionForm
    ordering = ('requisition_identifier',)

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'requisition_datetime',
                'is_drawn',
                'reason_not_drawn',
                'reason_not_drawn_other',
                'drawn_datetime',
                'study_site',
                'panel',
                'item_type',
                'item_type_other',
                'item_count',
                'estimated_volume',
                'priority',
                'urgent_specify',
                'comments',
            )}),
        requisition_status_fieldset,
        requisition_identifier_fieldset,
        requisition_verify_fieldset,
        audit_fieldset_tuple)

    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
        'priority': admin.VERTICAL,
    }

    list_display = ('subject_visit', 'is_drawn', 'panel', 'estimated_volume',)

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj)
                +requisition_identifier_fields
                +requisition_verify_fields)
