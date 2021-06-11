from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_validators.date import date_not_future
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin
from ..choices import CONTRACEPTIVES
from ..maternal_choices import OUTCOME


class PregnancyStatus(CrfModelMixin):

    start_date_menstrual_period = models.DateField(
        verbose_name='Start Date of Last Menstrual Period (DD/MMM/YYYY)',
        validators=[date_not_future, ],
        null=True,
        blank=True)

    expected_delivery = models.DateField(
        verbose_name='Date of Expected Delivery (DD/MMM/YYYY)',
        null=True,
        blank=True)

    contraceptive_usage = models.CharField(
        verbose_name='Using Contraception',
        choices=YES_NO,
        max_length=10,)

    contraceptive = models.CharField(
        verbose_name='If yes, specify contraception',
        choices=CONTRACEPTIVES,
        max_length=30,
        blank=True,
        null=True)

    contraceptive_othr = OtherCharField()

    pregnancy_outcome = models.CharField(
        verbose_name='Pregnancy Outcome',
        choices=OUTCOME,
        max_length=30,
        null=True,
        blank=True)

    birth_defects = models.CharField(
        verbose_name='Were there any birth defects/anomalies?',
        max_length=10,
        choices=YES_NO,)

    specify_defect = models.CharField(
        verbose_name='If yes, Specify:',
        max_length=50,
        null=True,
        blank=True)

    """""Pregnancy History"""""

    number_prev_pregnancies = models.IntegerField(
        verbose_name='Overall Number of Previous Pregnancies',
        null=True,
        blank=True)

    number_normal_pregnancies = models.IntegerField(
        verbose_name='Number of Normal Deliveries',
        null=True,
        blank=True)

    number_miscarriages = models.IntegerField(
        verbose_name='Number of Spontaneous Miscarriages',
        null=True,
        blank=True)

    risk_factor = models.CharField(
        verbose_name='Relevant Pregnancy Risk Factor',
        max_length=10,
        null=True,
        blank=True)

    family_history = models.CharField(
        verbose_name='Relevant Family History',
        max_length=10,
        null=True,
        blank=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Pregnancy Status'
        verbose_name_plural = 'Pregnancy Status'
