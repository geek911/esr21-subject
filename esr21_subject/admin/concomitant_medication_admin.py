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
                'prohibited',
                'reason_prohibited')}),
        audit_fieldset_tuple)

    radio_fields = {'ongoing': admin.VERTICAL,
                    'prohibited': admin.VERTICAL, }


    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)