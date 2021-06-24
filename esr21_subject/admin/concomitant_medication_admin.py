from django.contrib import admin

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import ConcomitantMedicationForm
from ..models import ConcomitantMedication
from ..admin_site import esr21_subject_admin


@admin.register(ConcomitantMedication, site=esr21_subject_admin)
class ConcomitantMedicationAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = ConcomitantMedicationForm
    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'administered_date',
                'medication_name',
                'medDra_name',
                'medDra_code',
                'atc_code',
                'dose',
                'unit',
                'unit_other',
                'frequency',
                'frequency_other',
                'route',
                'route_other',
                'reason_of_use',
                'ongoing',
                'stop_date',
                'prohibited',)}),
        audit_fieldset_tuple)

    radio_fields = {'ongoing': admin.VERTICAL,
                    'prohibited': admin.VERTICAL, }