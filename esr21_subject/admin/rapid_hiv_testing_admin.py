from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import esr21_subject_admin
from ..forms import RapidHIVTestingForm
from ..models import RapidHIVTesting


@admin.register(RapidHIVTesting, site=esr21_subject_admin)
class RapidHIVTestingAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = RapidHIVTestingForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_visit',
                'report_datetime',
                'rapid_test_done',
                'result_date',
                'result',
                'comments']}
         ), audit_fieldset_tuple)

    list_display = ('rapid_test_done',
                    'result')
    list_filter = ('rapid_test_done', 'result')
    search_fields = ('result_date', )
    radio_fields = {'rapid_test_done': admin.VERTICAL,
                    'result': admin.VERTICAL, }
