from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_base.model_fields import OtherCharField
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_constants.choices import YES_NO
from ..choices import (HOSPITALIZATION_STATUS,
                       HOSPITALIZATION_REASON, HOSPITALIZATION_OUTCOME)
from .list_models import COVIDSymptoms


class Hospitalization(NonUniqueSubjectIdentifierFieldMixin,
                      SiteModelMixin, BaseUuidModel):
    status = models.CharField(
        verbose_name='Hospitalization Status',
        max_length=50,
        choices=HOSPITALIZATION_STATUS)
    start_date = models.DateField()
    stop_date = models.DateField(
        verbose_name='Stop date',
        null=True,
        blank=True)
    ongoing = models.CharField(
        max_length=3,
        choices=YES_NO)
    reason = models.CharField(
        verbose_name='Primary reason for hospital/ inpatient/ ER visit',
        max_length=50,
        choices=HOSPITALIZATION_REASON, )

    reason_other = OtherCharField(
        verbose_name='If Other, specify',
        max_length=100,
        null=True,
        blank=True,
    )

    seriousness_criteria = models.ManyToManyField(
        COVIDSymptoms,
        verbose_name='If COVID-19 related symptoms',
        help_text='(check all that apply)', )
    hospitalization_outcome = models.CharField(
        verbose_name='Hospitalization Outcome',
        max_length=90,
        choices=HOSPITALIZATION_OUTCOME,
    )

    class Meta:
        verbose_name = "Hospitalization"
        verbose_name_plural = "Hospitalization"
