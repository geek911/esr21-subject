from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO

from ..choices import (HOSPITALIZATION_STATUS,
                       HOSPITALIZATION_REASON, HOSPITALIZATION_OUTCOME)
from .model_mixins import CrfModelMixin
from .list_models import COVIDSymptoms


class Hospitalization(CrfModelMixin):

    status = models.CharField(
        verbose_name='Hospitalization Status',
        max_length=50,
        choices=HOSPITALIZATION_STATUS)

    start_date = models.DateField(
        verbose_name='Start date of hospitalization')

    stop_date = models.DateField(
        verbose_name='Stop date of hospitalization',
        null=True,
        blank=True)

    ongoing = models.CharField(
        max_length=3,
        choices=YES_NO)

    reason = models.CharField(
        verbose_name='Primary reason for hospital/ inpatient/ ER visit',
        max_length=50,
        choices=HOSPITALIZATION_REASON,)

    reason_other = OtherCharField(
        verbose_name='If Other, specify',
        max_length=100,
        null=True,
        blank=True,
    )

    covid_symptoms = models.ManyToManyField(
        COVIDSymptoms,
        verbose_name=('If COVID-19 related symptoms, please check all that '
                      'apply'),
        blank=True)

    hospitalization_outcome = models.CharField(
        verbose_name='Hospitalization Outcome',
        max_length=90,
        choices=HOSPITALIZATION_OUTCOME,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Hospitalization'
        verbose_name_plural = 'Hospitalization'
