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
            'fields': (
                'subject_visit',
                'report_datetime',
                'relevant_history',
                'diagnosis',
                'start_date',
                'end_date',
                'ongoing',
                'on_medication',
                'cm_log_line',
            ),
        }),
    )

    radio_fields = {'relevant_history': admin.VERTICAL,
                    'on_medication': admin.VERTICAL,
                    'ongoing': admin.VERTICAL, }
