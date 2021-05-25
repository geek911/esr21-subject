from django.contrib import admin

from edc_model_admin import ModelAdminBasicMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..forms import SubjectLocatorForm
from ..models import SubjectLocator
from ..admin_site import esr21_subject_admin


@admin.register(SubjectLocator, site=esr21_subject_admin)
class SubjectLocatorAdmin(ModelAdminBasicMixin,
                          SimpleHistoryAdmin,
                          admin.ModelAdmin):
    form = SubjectLocatorForm
    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'date_signed',
                'permission',
                'physical_address',
                'call_permission',
                'participant_cell',
                'alt_participant_cell',
                'participant_tel',
                'alt_participant_tel',
                'may_call_work',
                'work_place',
                'work_location',
                'call_any',
                'full_name',
                'relation_to_participant',
                'address',
                'cell',
                'tel',)}),
        audit_fieldset_tuple)

    radio_fields = {'permission': admin.VERTICAL,
                    'call_permission': admin.VERTICAL,
                    'may_call_work': admin.VERTICAL,
                    'call_any': admin.VERTICAL,
                    }
