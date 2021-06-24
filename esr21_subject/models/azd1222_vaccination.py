from django.db import models

from edc_constants.choices import YES_NO
from .model_mixins import CrfModelMixin
from ..choices import LEFT_RIGHT
from edc_base.model_fields.custom_fields import OtherCharField


class Azd1222Vaccination(CrfModelMixin):

    received_first_dose = models.CharField(
        verbose_name='Has the participant received a first dose?',
        max_length=3,
        choices=YES_NO)

    first_vaccination_date = models.DateField(
        verbose_name='Vaccination date',
        blank=True,
        null=True)

    first_lot_number = models.CharField(
        verbose_name='Vaccine batch/lot number',
        max_length=20,
        blank=True,
        null=True,
        help_text='NB:First dose')

    first_dose_site = models.CharField(
        verbose_name='Vaccination site',
        max_length=20,
        choices=LEFT_RIGHT,
        help_text='NB:First dose')

    first_dose_site_other = OtherCharField()

    receive_second_dose = models.CharField(
        verbose_name='Has the participant received the second dose?',
        max_length=3,
        choices=YES_NO,)

    second_scheduled_dose_date = models.DateField(
        verbose_name='When is the scheduled date for the second dose?',)

    second_lot_number = models.CharField(
        verbose_name='Vaccine batch/lot number',
        max_length=20,
        blank=True,
        null=True,
        help_text='NB:Second dose')

    second_dose_site = models.CharField(
        verbose_name='Vaccination site',
        max_length=20,
        choices=LEFT_RIGHT,
        help_text='NB:Second dose')

    second_dose_site_other = OtherCharField()

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'AZD1222 Vaccination'
        verbose_name_plural = 'AZD1222 Vaccination'
