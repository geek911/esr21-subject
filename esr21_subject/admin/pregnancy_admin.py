from django.contrib import admin

from edc_model_admin import ModelAdminBasicMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..forms import PregnancyForm
from ..models import Pregnancy
from ..admin_site import esr21_subject_admin


@admin.register(Pregnancy, site=esr21_subject_admin)
class PregnancyAdmin(ModelAdminBasicMixin,
                     SimpleHistoryAdmin,
                     admin.ModelAdmin):
    form = PregnancyForm
    fieldsets = (
        (None, {
            'fields': (
                'preg_performed',
                'preg_date',
                'result',)}),
        audit_fieldset_tuple)

    radio_fields = {'preg_performed': admin.VERTICAL,
                    'result': admin.VERTICAL,
                    }
