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

    """Vital signs"""
    vital_signs_measured = models.CharField(
        verbose_name='Were the vital signs measurements performed?',
        max_length=3,
        choices=YES_NO)

    reason_vitals_nd = models.CharField(
        verbose_name='If No, Reason Not Done',
        max_length=30,
        choices=REASON,
        default=NOT_APPLICABLE)

    assessment_dt = models.DateTimeField(
        verbose_name='Date and Time of Assessment',
        blank=True,
        null=True)

    systolic_bp = models.IntegerField(
        verbose_name='Systolic Blood Pressure',
        help_text='Fixed Unit: mmHg',
        blank=True,
        null=True)

    diastolic_bp = models.IntegerField(
        verbose_name='Diastolic Blood Pressure',
        help_text='Fixed Unit: mmHg',
        blank=True,
        null=True)

    heart_rate = models.IntegerField(
        verbose_name='Heart Rate',
        help_text='beats/min',
        blank=True,
        null=True)

    body_temp = models.DecimalField(
        verbose_name='Body Temperature',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True)

    body_temp_unit = models.CharField(
        verbose_name='Unit of temperature',
        choices=TEMP_UNITS,
        max_length=10,
        blank=True,
        null=True)

    oxygen_saturated = models.DecimalField(
        verbose_name='Oxygen Saturation (via Pulse Oximetry)',
        max_digits=5,
        decimal_places=2,
        help_text='Fixed Unit: %',
        blank=True,
        null=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Physical examination and Vital signs'
        verbose_name_plural = 'Physical examination and Vital signs'
