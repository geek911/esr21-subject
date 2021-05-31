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
                'date_of_birth',
                'age',
                'gender',
                'childbearing_potential',
                'if_no_reason',
                'if_no_reason_other',
                'ethnicity',
                'ethnicity_other',
                'race_of_subject',
                'race',
               ]}
         ), audit_fieldset_tuple)

    radio_fields = {'gender': admin.VERTICAL,
                    'childbearing_potential': admin.VERTICAL,
                    'if_no_reason': admin.VERTICAL,
                    'ethnicity': admin.VERTICAL,
                    'race_of_subject': admin.VERTICAL, }

    filter_horizontal = ('race',)
