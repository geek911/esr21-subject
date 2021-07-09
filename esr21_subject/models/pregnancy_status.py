from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_validators.date import date_not_future, date_is_future
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin
from ..choices import CONTRACEPTIVES


class PregnancyStatus(CrfModelMixin):

    start_date_menstrual_period = models.DateField(
        verbose_name='Start Date of Last Menstrual Period (DD/MMM/YYYY)',
        validators=[date_not_future, ],
        null=True,
        blank=True)

    expected_delivery = models.DateField(
        verbose_name='Date of Expected Delivery (DD/MMM/YYYY)',
        validators=[date_is_future, ],
        null=True,
        blank=True)

    contraceptive_usage = models.CharField(
        verbose_name='Using Contraception',
        choices=YES_NO,
        max_length=3,)

    contraceptive = models.CharField(
        verbose_name='If yes, specify contraception',
        choices=CONTRACEPTIVES,
        max_length=30,
        blank=True,
        null=True)

    contraceptive_other = OtherCharField()

    """""Pregnancy History"""""

    number_prev_pregnancies = models.PositiveIntegerField(
        verbose_name='Overall number of previous pregnancies',
        null=True,
        blank=True)

    number_normal_pregnancies = models.PositiveIntegerField(
        verbose_name='Number of normal deliveries',
        null=True,
        blank=True)

    number_miscarriages = models.PositiveIntegerField(
        verbose_name='Number of spontaneous miscarriages',
        null=True,
        blank=True)

    date_miscarriages = models.DateField(
        verbose_name='Date of last spontaneous miscarriage',
        validators=[date_not_future, ],
        null=True,
        blank=True)

    risk_factor = models.CharField(
        verbose_name='Relevant pregnancy risk factor',
        max_length=10,
        null=True,
        blank=True)

    maternal_history = models.TextField(
        verbose_name='Maternal medical and obstetric history',
        max_length=350,
        null=True,
        blank=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Pregnancy Status'
        verbose_name_plural = 'Pregnancy Status'
