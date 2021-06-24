from django.db import models

from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE

from .model_mixins import CrfModelMixin
from ..choices import REASON, GENERAL_APPEARANCE


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

    abnormalities_found = models.CharField(
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

    general_appearance = models.CharField(
        verbose_name='General Appearance',
        max_length=20,
        choices=GENERAL_APPEARANCE,
    )

    abnormality_description = models.TextField(
        verbose_name='Abnormal, description of abnormality',
        blank=True,
        null=True,)

    face_check = models.CharField(
        verbose_name='Head, eyes, ears, and nose',
        max_length=20,
        choices=GENERAL_APPEARANCE,
    )

    face_description = models.TextField(
        verbose_name='Abnormal, description of abnormality',
        blank=True,
        null=True, )

    neck_check = models.CharField(
        verbose_name='Neck',
        max_length=20,
        choices=GENERAL_APPEARANCE,
    )

    neck_description = models.TextField(
        verbose_name='Abnormal, description of abnormality',
        blank=True,
        null=True, )

    respiratory_check = models.CharField(
        verbose_name='Respiratory',
        max_length=20,
        choices=GENERAL_APPEARANCE,
    )

    respiratory_description = models.TextField(
        verbose_name='Abnormal, description of abnormality',
        blank=True,
        null=True, )

    cardiovascular_check = models.CharField(
        verbose_name='Cardiovascular',
        max_length=20,
        choices=GENERAL_APPEARANCE,
    )

    cardiovascular_description = models.TextField(
        verbose_name='Abnormal, description of abnormality',
        blank=True,
        null=True, )

    abdominal_check = models.CharField(
        verbose_name='Abdominal',
        max_length=20,
        choices=GENERAL_APPEARANCE,
    )

    abdominal_description = models.TextField(
        verbose_name='Abnormal, description of abnormality',
        blank=True,
        null=True, )

    dermatologic_check = models.CharField(
        verbose_name='Dermatologic',
        max_length=20,
        choices=GENERAL_APPEARANCE,
    )

    dermatologic_description = models.TextField(
        verbose_name='Abnormal, description of abnormality',
        blank=True,
        null=True, )

    neurological_check = models.CharField(
        verbose_name='Neurological',
        max_length=20,
        choices=GENERAL_APPEARANCE,
    )

    neurological_description = models.TextField(
        verbose_name='Abnormal, description of abnormality',
        blank=True,
        null=True, )

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Physical examination'
        verbose_name_plural = 'Physical examination'
