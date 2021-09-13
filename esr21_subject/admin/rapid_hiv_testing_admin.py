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
                'prev_hiv_test',
                'evidence_hiv_status',
                'hiv_test_date',
                'hiv_result',
                'rapid_test_done',
                'rapid_test_date',
                'rapid_test_result',
                'comments']}
        ), audit_fieldset_tuple)

    list_display = ('rapid_test_done',
                    'rapid_test_result')

    list_filter = ('prev_hiv_test', 'hiv_result', 'rapid_test_done', 'rapid_test_date')

    search_fields = ('rapid_test_date',)

    radio_fields = {
        'rapid_test_done': admin.VERTICAL,
        'evidence_hiv_status': admin.VERTICAL,
        'prev_hiv_test': admin.VERTICAL,
        'hiv_result': admin.VERTICAL,
        'rapid_test_result': admin.VERTICAL, }


    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
