from django.contrib import admin
from django.db import models
from django.forms import Textarea

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import VitalSignsForm
from ..models import VitalSigns
from ..admin_site import esr21_subject_admin


@admin.register(VitalSigns, site=esr21_subject_admin)
class VitalSignsAdmin(CrfModelAdminMixin, admin.ModelAdmin):
    form = VitalSignsForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }
    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'vital_signs_measured',
                'reason_vitals_nd',
                'assessment_dt',
                'systolic_bp',
                'diastolic_bp',
                'heart_rate',
                'body_temp',
                'body_temp_unit',
                'oxygen_saturated',
                'comment',
            ),
        }),
        audit_fieldset_tuple)

    radio_fields = {'vital_signs_measured': admin.VERTICAL,
                    'reason_vitals_nd': admin.VERTICAL,
                    'body_temp_unit': admin.VERTICAL,
                    }

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
