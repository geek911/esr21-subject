from django.contrib import admin

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import Covid19PreventativeBehavioursForm
from ..models import Covid19PreventativeBehaviours
from ..admin_site import esr21_subject_admin


@admin.register(Covid19PreventativeBehaviours, site=esr21_subject_admin)
class Covid19PreventativeBehavioursAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = Covid19PreventativeBehavioursForm
    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'people_sneezing',
                'avoid_touching',
                'dislike_face_mask',
                'temperature',
                'crowded_places',
                'self_isolate',
                'use_hand_sanitizer',
                'avoid_public_places',)}),
        audit_fieldset_tuple)

    radio_fields = {'people_sneezing': admin.VERTICAL,
                    'avoid_touching': admin.VERTICAL,
                    'dislike_face_mask': admin.VERTICAL,
                    'temperature': admin.VERTICAL,
                    'crowded_places': admin.VERTICAL,
                    'self_isolate': admin.VERTICAL,
                    'use_hand_sanitizer': admin.VERTICAL,
                    'avoid_public_places': admin.VERTICAL,
                    }


    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
