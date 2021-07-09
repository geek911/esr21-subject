from django.db import models
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from .model_mixins import CrfModelMixin
from ..choices import UNIT_OPTIONS, FREQUENCY, CONCOMITANT_ROUTE


class ConcomitantMedication(CrfModelMixin):

    administered_date = models.DateField(
        verbose_name='Date Administered (DD MMM YYYY):',
        validators=[date_not_future])

    medication_name = models.CharField(
        verbose_name='Name of concomitant medication ',
        max_length=40,
    )

    who_name = models.CharField(
        verbose_name='WHODRUG preferred name',
        max_length=30)

    who_code = models.CharField(
        verbose_name='WHODRUG preferred code',
        max_length=30)

    atc_code = models.CharField(
        verbose_name='ATC code',
        max_length=30)

    dose = models.DecimalField(
        verbose_name='Dose',
        decimal_places=2,
        max_digits=4)

    unit = models.CharField(
        verbose_name='Unit',
        max_length=25,
        choices=UNIT_OPTIONS)

    unit_other = models.CharField(
        verbose_name='Other, specify',
        max_length=25,
        blank=True,
        null=True)

    frequency = models.CharField(
        verbose_name='Frequency',
        max_length=25,
        choices=FREQUENCY)

    frequency_other = models.CharField(
        verbose_name='Other, specify',
        max_length=25,
        blank=True,
        null=True)

    route = models.CharField(
        verbose_name='Route',
        max_length=25,
        choices=CONCOMITANT_ROUTE)

    route_other = models.CharField(
        verbose_name='Other, specify',
        max_length=25,
        blank=True,
        null=True)

    reason_of_use = models.TextField(
        verbose_name='Reason for use',)

    ongoing = models.CharField(
        verbose_name='Ongoing',
        max_length=25,
        choices=YES_NO)

    stop_date = models.DateField(
        verbose_name='Stop Date (DD MMM YYYY)',
        validators=[date_not_future, ])

    prohibited = models.CharField(
        verbose_name='Is concomitant medication prohibited?',
        max_length=25,
        choices=YES_NO)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Concomitant Medication'
        verbose_name_plural = 'Concomitant Medication'
