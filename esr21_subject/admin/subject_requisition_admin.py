from django.contrib import admin
from edc_lab.admin import RequisitionAdminMixin
from edc_lab.admin import requisition_identifier_fields
from edc_lab.admin import requisition_identifier_fieldset, requisition_verify_fields
from edc_lab.admin import requisition_verify_fieldset, requisition_status_fieldset
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import esr21_subject_admin
from ..forms import SubjectRequisitionForm
from ..models import SubjectRequisition


@admin.register(SubjectRequisition, site=esr21_subject_admin)
class SubjectRequisitionAdmin(
        RequisitionAdminMixin, admin.ModelAdmin):

    form = SubjectRequisitionForm
    actions = ["export_as_csv"]
    ordering = ('requisition_identifier',)

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'is_drawn',
                'reason_not_drawn',
                'drawn_date',
                'drawn_time',
                'study_site',
            )}),
        audit_fieldset_tuple)

    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj)
