from django.contrib import admin

from edc_model_admin import ModelAdminBasicMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..forms import EligibilityConfirmationForm
from ..models import EligibilityConfirmation
from ..admin_site import esr21_subject_admin


@admin.register(EligibilityConfirmation, site=esr21_subject_admin)
class EligibilityConfirmationAdmin(ModelAdminBasicMixin,
                                   SimpleHistoryAdmin,
                                   admin.ModelAdmin):

    form = EligibilityConfirmationForm
    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'report_datetime',
                'age_in_years',)}),
        audit_fieldset_tuple)

    search_fields = ['screening_identifier']

    readonly_fields = ('screening_identifier',)
