from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_base.model_validators import date_not_future, datetime_not_future
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import date_not_before_study_start

from ..choices import POS_NEG_IND


class RapidHIVTesting(NonUniqueSubjectIdentifierFieldMixin,
                      SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text='Date and time of report.')

    rapid_test_done = models.CharField(
        verbose_name='Was a rapid test processed?',
        choices=YES_NO,
        max_length=3)

    result_date = models.DateField(
        validators=[
            date_not_before_study_start,
            date_not_future, ],
        verbose_name='Date of rapid test',
        blank=True,
        null=True)

    result = models.CharField(
        verbose_name='What is the rapid test result?',
        choices=POS_NEG_IND,
        max_length=15,
        blank=True,
        null=True)

    comments = models.CharField(
        verbose_name='Comment',
        max_length=250,
        blank=True,
        null=True)

    class Meta:
        app_label = 'esr21_subject'
        verbose_name = 'Rapid HIV Testing'
        verbose_name_plural = 'Rapid HIV Testing'
