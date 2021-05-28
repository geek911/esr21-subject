from django.db import models
from django_crypto_fields.fields import EncryptedCharField

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future, date_is_future
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin

from ..choices import ROUTE, VACCINATION_LOCATION


class VaccinationDetails(NonUniqueSubjectIdentifierFieldMixin,
                         SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text='Date and time of report.')

    vaccination_place = models.CharField(
        verbose_name='Where was the vaccination administered?',
        max_length=35,
        blank=True,
        null=True, )

    vaccination_dt = models.DateTimeField(
        verbose_name='Date and time the vaccination was administered',
        validators=[datetime_not_future, ])

    route = models.CharField(
        verbose_name='Route (defaulted, no entry required)',
        max_length=30,
        choices=ROUTE,
        blank=True,
        null=True)

    location = models.CharField(
        verbose_name='Location',
        max_length=30,
        choices=VACCINATION_LOCATION)

    location_other = OtherCharField()

    admin_per_protocol = models.CharField(
        verbose_name='Was the vaccine administered per protocol?',
        max_length=3,
        choices=YES_NO)

    reason_not_per_protocol = models.CharField(
        verbose_name='If No, please explain:',
        max_length=100,
        blank=True,
        null=True)

    dose_administered = models.DecimalField(
        verbose_name='Dosage administered',
        decimal_places=2,
        max_digits=3)

    batch_number = models.CharField(
        verbose_name='Vaccination batch number',
        max_length=35, )

    expiry_date = models.DateField(
        verbose_name='Vaccination expiry date',
        validators=[date_is_future, ])

    provider_name = EncryptedCharField(
        verbose_name='Name of the provider',
        max_length=35, )

    next_vaccination = models.DateField(
        verbose_name=('When is the participant scheduled for their next '
                      'vaccination dose?'),
        validators=[date_is_future, ])

    class Meta:
        app_label = 'esr21_subject'
        verbose_name = 'Collection of vaccination details'
        verbose_name_plural = 'Collection of vaccination details'
