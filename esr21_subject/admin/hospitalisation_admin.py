from django.contrib import admin

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import HospitalisationForm
from ..models import Hospitalisation
from ..admin_site import esr21_subject_admin


@admin.register(Hospitalisation, site=esr21_subject_admin)
class HospitalisationAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    model = Hospitalisation
    form = HospitalisationForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_visit',
                'report_datetime',
                'status',
                'start_date',
                'stop_date',
                'ongoing',
                'reason',
                'reason_other',
                'covid_symptoms',
                'hospitalisation_outcome',
            ]}
         ),)

    radio_fields = {'status': admin.VERTICAL,
                    'ongoing': admin.VERTICAL,
                    'reason': admin.VERTICAL,
                    'hospitalisation_outcome': admin.VERTICAL, }

    filter_horizontal = ('covid_symptoms',)
