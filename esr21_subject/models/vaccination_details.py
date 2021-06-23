from django.db import models
from django_crypto_fields.fields import EncryptedCharField

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import datetime_not_future, date_is_future
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin
from ..choices import ROUTE, VACCINATION_LOCATION


class VaccinationDetails(CrfModelMixin):

    vaccination_place = models.CharField(
        verbose_name='Where was the vaccination administered?',
        max_length=35,
        blank=True,
        null=True, )

    vaccination_dt = models.DateTimeField(
        verbose_name='Date and time the vaccination was administered',
        validators=[datetime_not_future, ])

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

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Collection of vaccination details'
        verbose_name_plural = 'Collection of vaccination details'
