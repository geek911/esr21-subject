from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import esr21_subject_admin
from ..forms import SubjectVisitForm
from ..models import SubjectVisit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectVisit, site=esr21_subject_admin)
class SubjectVisitAdmin(
    ModelAdminMixin, VisitModelAdminMixin, admin.ModelAdmin):
    form = SubjectVisitForm

    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'reason',
                'reason_missed',
                'reason_unscheduled',
                'info_source',
                'info_source_other',
                'comments'
            ]}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple
    )

    radio_fields = {
        'reason': admin.VERTICAL,
        'info_source': admin.VERTICAL}

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['timepoint'] = self.get_timepoint(request)

        return super().add_view(
            request, form_url=form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['timepoint'] = self.get_timepoint(request)

        return super().change_view(
            request, object_id, form_url=form_url, extra_context=extra_context)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
