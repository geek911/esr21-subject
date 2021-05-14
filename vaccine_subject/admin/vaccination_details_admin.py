from django.contrib import admin

from edc_model_admin import ModelAdminBasicMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..forms import VaccinationDetailsForm
from ..models import VaccinationDetails


@admin.register(VaccinationDetails)
class VaccinationDetailsAdmin(ModelAdminBasicMixin,
                                SimpleHistoryAdmin,
                                admin.ModelAdmin):
    form = VaccinationDetailsForm
    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'date_of_vaccination',
                'vaccination_place',
                'vaccine_name',
                'dosage_administered',
                'batch_number',
                'expiry_date',
                'provider_name',
                'next_vaccination',)}),
        audit_fieldset_tuple)