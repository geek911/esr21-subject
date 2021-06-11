from django.apps import apps as django_apps
from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.constants import NOT_APPLICABLE
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_lab.models import RequisitionIdentifierMixin
from edc_lab.models import RequisitionModelMixin, RequisitionStatusMixin
from edc_metadata.model_mixins.updates import UpdatesRequisitionMetadataModelMixin
from edc_reference.model_mixins import RequisitionReferenceModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_visit_tracking.managers import CrfModelManager as VisitTrackingCrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin as VisitTrackingCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from ..choices import REASON_NOT_DRAWN
from .subject_visit import SubjectVisit
# from .search_slug_model_mixin import SearchSlugModelMixin


class Manager(VisitTrackingCrfModelManager, SearchSlugManager):
    pass


class SubjectRequisition(
        NonUniqueSubjectIdentifierFieldMixin,
        RequisitionModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin,
        VisitTrackingCrfModelMixin, SubjectScheduleCrfModelMixin,
        RequiresConsentFieldsModelMixin, PreviousVisitModelMixin,
        RequisitionReferenceModelMixin, UpdatesRequisitionMetadataModelMixin,
        # SearchSlugModelMixin,
        BaseUuidModel):

    lab_profile_name = 'esr21_subject'

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    is_drawn = models.CharField(
        verbose_name='Was a sample collected?',
        max_length=3,
        choices=YES_NO)

    reason_not_drawn = models.CharField(
        verbose_name='If no, reason not done',
        max_length=25,
        default=NOT_APPLICABLE,
        choices=REASON_NOT_DRAWN)

    drawn_date = models.DateField(
        verbose_name='Collection date',
        validators=[datetime_not_future, ],
        null=True,
        blank=True,)

    drawn_time = models.TimeField(
        verbose_name='Collection time',
        null=True,
        blank=True)

    objects = Manager()

    history = HistoricalRecords()

    def __str__(self):
        return (
            f'{self.requisition_identifier} '
            f'{self.panel_object.verbose_name}')

    def save(self, *args, **kwargs):
        if not self.id:
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.protocol_number = edc_protocol_app_config.protocol_number
        self.report_datetime = self.requisition_datetime
        self.subject_identifier = self.subject_visit.subject_identifier
        super().save(*args, **kwargs)

    # def get_search_slug_fields(self):
        # fields = super().get_search_slug_fields()
        # fields.extend([
            # 'requisition_identifier',
            # 'human_readable_identifier', 'identifier_prefix'])
        # return fields

    class Meta:
        unique_together = ('panel', 'subject_visit')
