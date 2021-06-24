from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import DemographicsDataForm
from ..models import DemographicsData
from ..admin_site import esr21_subject_admin


@admin.register(DemographicsData, site=esr21_subject_admin)
class DemographicDataAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = DemographicsDataForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_visit',
                'report_datetime',
                'age_at_entry',
                'country',
                'ethnicity',
                'ethnicity_other',
                'household_members',
                'highest_education',
                'employment_status',
                'employment_status_other',
                'settlement_type',
                'marital_status',
                'marital_status_other',
                'running_water',
               ]}
         ), audit_fieldset_tuple)

    radio_fields = {'ethnicity': admin.VERTICAL,
                    'highest_education': admin.VERTICAL,
                    'employment_status': admin.VERTICAL,
                    'settlement_type': admin.VERTICAL,
                    'marital_status': admin.VERTICAL,
                    'running_water': admin.VERTICAL, }
