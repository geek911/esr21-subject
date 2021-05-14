from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_metadata import NextFormGetter
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin, ModelAdminBasicMixin)
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fields, audit_fieldset_tuple)
from simple_history.admin import SimpleHistoryAdmin

from ..forms import EligibilityCheckListForm
from ..models import EligibilityCheckList

# class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
#                       ModelAdminFormInstructionsMixin,
#                       ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
#                       ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
#                       ModelAdminInstitutionMixin,
#                       ModelAdminRedirectOnDeleteMixin,
#                       ModelAdminSiteMixin):
#
#     list_per_page = 10
#     date_hierarchy = 'modified'
#     empty_value_display = '-'
#     next_form_getter_cls = NextFormGetter

@admin.register(EligibilityCheckList)
class EligibilityCheckListAdmin(ModelAdminBasicMixin,
                                SimpleHistoryAdmin,
                                admin.ModelAdmin):
    form = EligibilityCheckListForm
    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'report_datetime',
                'age_in_years',)}),
        audit_fieldset_tuple)
