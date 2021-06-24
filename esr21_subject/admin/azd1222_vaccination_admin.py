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
                'report_datetime',  # )}),
        # ('First Dose', {
            # 'fields': (
                'received_first_dose',
                'first_vaccination_date',
                'first_lot_number',
                'first_dose_site',
                'first_dose_site_other',  # )})
        # ('Second Dose', {
            # 'fields': (
                'receive_second_dose',
                'second_scheduled_dose_date',
                'second_lot_number',
                'second_dose_site',
                'second_dose_site_other'
            ), }),
        audit_fieldset_tuple
    )

    radio_fields = {
        'received_first_dose': admin.VERTICAL,
        'receive_second_dose': admin.VERTICAL,
        'first_dose_site': admin.VERTICAL,
        'second_dose_site': admin.VERTICAL, }
