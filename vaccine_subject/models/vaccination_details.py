from django.db import models
from django_crypto_fields.fields import EncryptedCharField

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_base.model_validators import date_not_future, date_is_future
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow


class VaccinationDetails(NonUniqueSubjectIdentifierFieldMixin,
                         SiteModelMixin, BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    date_of_vaccination = models.DateField(
        verbose_name="When did the participant receive their vaccination dose?",
        validators=[date_not_future, ])

    vaccination_place = models.CharField(
        verbose_name="Where was the vaccination administered?",
        max_length=35,
        blank=True,
        null=True, )

    vaccine_name = models.CharField(
        verbose_name="Name of the vaccination",
        max_length=35,
        blank=True,
        null=True, )

    dosage_administered = models.IntegerField(
        verbose_name="Dosage administered",
        blank=True,
        null=True, )

    batch_number = models.CharField(
        verbose_name="Vaccination batch number",
        max_length=35,
        blank=True,
        null=True, )

    expiry_date = models.DateField(
        verbose_name="Vaccination expiry date",
        validators=[date_is_future, ])

    provider_name = EncryptedCharField(
        verbose_name="Name of the provider",
        max_length=35,
        blank=True,
        null=True, )

    next_vaccination = models.DateField(
        verbose_name="When is the participant scheduled for "
                     "their next vaccination dose?",
        validators=[date_is_future, ])

    class Meta:
        verbose_name = "Vaccine Details"
        verbose_name_plural = "Vaccine Details"
