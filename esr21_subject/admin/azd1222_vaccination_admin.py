from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import esr21_subject_admin
from ..forms import Azd1222VaccinationForm
from ..models import Azd1222Vaccination
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(Azd1222Vaccination, site=esr21_subject_admin)
class Azd1222VaccinationAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = Azd1222VaccinationForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'vaccine_status',
                'received_first_dose',
                'vaccination_date',
                'lot_number',
                'vaccination_site',
                'receive_second_dose',
                'scheduled_vaccination',
            ),
        }),
        audit_fieldset_tuple
    )

    radio_fields = {
        'vaccine_status': admin.VERTICAL,
        'received_first_dose': admin.VERTICAL,
        'receive_second_dose': admin.VERTICAL,
        'vaccination_site': admin.VERTICAL,}
