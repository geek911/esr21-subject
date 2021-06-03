from django.db import models

from edc_constants.choices import YES_NO
from .model_mixins import CrfModelMixin


class Azd1222Vaccination(CrfModelMixin):
    vaccine_status = models.CharField(
        verbose_name='Vaccine status:',
        max_length=20,
        choices=YES_NO, )

    received_first_dose = models.CharField(
        verbose_name='Has the participant received a first dose of AZD1222?',
        max_length=20,
        choices=YES_NO)

    vaccination_date = models.DateField(
        verbose_name='Vaccination date',
        blank=True,
        null=True)

    lot_number = models.CharField(
        verbose_name='Vaccine batch/lot number (C25)',
        max_length=20,
        blank=True,
        null=True)

    vaccination_site = models.CharField(
        verbose_name='Vaccination site (eg, left arm) (C200)',
        max_length=20, )

    receive_second_dose = models.CharField(
        verbose_name='Is the participant scheduled to receive a second '
                     'dose of AZD1222?',
        max_length=20,
        choices=YES_NO, )

    scheduled_vaccination = models.CharField(
        verbose_name='Date of scheduled vaccination – DD/MMM/YYYY',
        max_length=20, )

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'AZD122 Vaccination'
        verbose_name_plural = 'AZD1222 Vaccination'
