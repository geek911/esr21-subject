from django.db import models

from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE

from .model_mixins import CrfModelMixin
from ..choices import REASON, TEMP_UNITS


class PhysicalExam(CrfModelMixin):
    """Physical Examination"""

    physical_exam = models.CharField(
        verbose_name='Was the physical examination performed?',
        max_length=10,
        choices=YES_NO)

    reason_not_done = models.CharField(
        verbose_name='If No, Reason Not Done',
        max_length=30,
        choices=REASON,
        default=NOT_APPLICABLE)

    exam_date = models.DateField(
        verbose_name='Date of examination (DD/MMM/YYYY)',
        blank=True,
        null=True,)

    abnormalities = models.CharField(
        verbose_name='Were any abnormalities found?',
        max_length=10,
        choices=YES_NO)

    abn_specify = OtherCharField(verbose_name='If yes, specify')

    clinically_significant = models.CharField(
        verbose_name='If yes, were any abnormalities clinically significant?',
        max_length=10,
        choices=YES_NO,
        blank=True,
        null=True)

    comment = models.TextField(
        verbose_name='Comment',
        blank=True,
        null=True,)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Physical examination and Vital signs'
        verbose_name_plural = 'Physical examination and Vital signs'
