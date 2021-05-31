from django.contrib import admin

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import MedicalHistoryForm
from ..models import MedicalHistory
from ..admin_site import esr21_subject_admin


@admin.register(MedicalHistory, site=esr21_subject_admin)
class MedicalHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = MedicalHistoryForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_visit',
                'report_datetime',
                'medical_history',
                'medical_history_diagnosis',
                'start_date',
                'end_date',
                'ongoing',
                'subject_taking_medication',
                'cm_log_line',
            ]}
         ),)

    radio_fields = {'medical_history': admin.VERTICAL,
                    'subject_taking_medication': admin.VERTICAL, }
