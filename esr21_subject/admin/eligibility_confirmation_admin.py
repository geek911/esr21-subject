from django.contrib import admin

from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin
from ..forms import EligibilityConfirmationForm
from ..models import EligibilityConfirmation
from ..admin_site import esr21_subject_admin


@admin.register(EligibilityConfirmation, site=esr21_subject_admin)
class EligibilityConfirmationAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = EligibilityConfirmationForm
    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'report_datetime',
                'participating_in_other_studies',
                'age_in_years',
                'any_vaccine_receipt',
                'received_vaccines', )}),
        audit_fieldset_tuple)

    radio_fields = {
        'received_vaccines': admin.VERTICAL,
        'participating_in_other_studies': admin.VERTICAL,
    }

    search_fields = ['screening_identifier']

    readonly_fields = ('screening_identifier',)
