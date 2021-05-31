from django.contrib import admin

from ..forms import HospitalizationForm
from ..models import Hospitalization
from ..admin_site import esr21_subject_admin


@admin.register(Hospitalization, site=esr21_subject_admin)
class HospitalizationAdmin(admin.ModelAdmin):
    model = Hospitalization
    form = HospitalizationForm

    fieldsets = (
        (None, {
            'fields': [
                'status',
                'start_date',
                'stop_date',
                'ongoing',
                'reason',
                'reason_other',
                'seriousness_criteria',
                'hospitalization_outcome',
            ]}
         ),)

    radio_fields = {'status': admin.VERTICAL,
                    'ongoing': admin.VERTICAL,
                    'reason': admin.VERTICAL,
                    'hospitalization_outcome': admin.VERTICAL, }

    filter_horizontal = ('seriousness_criteria',)