from django.db import models

from edc_constants.choices import YES_NO
from .model_mixins import CrfModelMixin
from ..choices import LEFT_RIGHT


class Azd1222Vaccination(CrfModelMixin):

    vaccine_status = models.CharField(
        verbose_name='Vaccine status:',
        max_length=20,
        choices=YES_NO,)

    received_first_dose = models.CharField(
        verbose_name='Has the participant received a first dose of AZD1222?',
        max_length=20,
        choices=YES_NO)

    vaccination_date = models.DateField(
        verbose_name='Vaccination date',
        blank=True,
        null=True)

    lot_number = models.CharField(
        verbose_name='Vaccine batch/lot number',
        max_length=20,
        blank=True,
        null=True)

    vaccination_site = models.CharField(
        verbose_name='Vaccination site',
        max_length=20,
        choices=LEFT_RIGHT,)

    receive_second_dose = models.CharField(
        verbose_name='Is the participant scheduled to receive a second '
                     'dose of AZD1222?',
        max_length=20,
        choices=YES_NO,)

    scheduled_vaccination = models.DateField(
        verbose_name='Date of scheduled vaccination',)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'AZD1222 Vaccination'
        verbose_name_plural = 'AZD1222 Vaccination'
