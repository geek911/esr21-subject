from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow


class EligibilityConfirmation(NonUniqueSubjectIdentifierFieldMixin,
                              SiteModelMixin, BaseUuidModel):

    screening_identifier = models.CharField(
        verbose_name='Screening Identifier',
        max_length=36,
        unique=True,)

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    age_in_years = models.IntegerField(
        verbose_name='What is the participants age?',
        help_text='(Years)', )

    class Meta:
        app_label = 'esr21_subject'
        verbose_name = 'Eligibility Confirmation'
        verbose_name_plural = 'Eligibility Confirmation'
