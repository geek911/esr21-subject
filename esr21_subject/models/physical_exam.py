from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from ..choices import REASON


class PhysicalExam(NonUniqueSubjectIdentifierFieldMixin,
                   SiteModelMixin, BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    physical_exam = models.CharField(
        verbose_name='Was the physical examination performed?',
        max_length=10,
        choices=YES_NO)

    reason_not_done = models.CharField(
        verbose_name='If No, Reason Not Done',
        max_length=30,
        choices=REASON)

    exam_date = models.DateField(
        verbose_name='Date of examination (DD MMM YYYY)',
        blank=True,
        null=True,)

    abnormalities = models.CharField(
        verbose_name='Were any abnormalities found?',
        max_length=10,
        choices=YES_NO)

    clinically_significant = models.CharField(
        verbose_name='If Yes, were any abnormalities clinically significant?',
        max_length=10,
        choices=YES_NO)

    comment = models.TextField(
        verbose_name='Comment',
        blank=True,
        null=True,)

    class Meta:
        app_label = 'esr21_subject'
        verbose_name = 'Physical Examination'
        verbose_name_plural = 'Physical Examination'
