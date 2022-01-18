from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django_crypto_fields.fields import EncryptedCharField

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import datetime_not_future, date_is_future
from edc_constants.choices import YES_NO, YES_NO_NA

from .model_mixins import CrfModelMixin
from ..choices import VACCINATION_LOCATION, VACCINATION_DOSE
from edc_constants.constants import NOT_APPLICABLE


class VaccinationDetails(CrfModelMixin):
    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        validators=[datetime_not_future, ])

    received_dose = models.CharField(
        verbose_name='Has the participant received a vaccination dose?',
        max_length=3,
        choices=YES_NO)

    received_dose_before = models.CharField(
        verbose_name='If yes, please indicate dose',
        max_length=12,
        choices=VACCINATION_DOSE,
        default=NOT_APPLICABLE)

    vaccination_site = models.CharField(
        verbose_name='Where was the vaccination administered?',
        max_length=30,
        blank=True,
        null=True,
        help_text="Geographical location")

    vaccination_date = models.DateTimeField(
        verbose_name='Date and time the vaccination was administered?',
        blank=True,
        null=True)

    location = models.CharField(
        verbose_name='Location administered',
        max_length=30,
        default=NOT_APPLICABLE,
        choices=VACCINATION_LOCATION)

    location_other = OtherCharField()

    admin_per_protocol = models.CharField(
        verbose_name='Was the vaccine administered per protocol?',
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    reason_not_per_protocol = models.CharField(
        verbose_name='If No, please explain:',
        max_length=100,
        blank=True,
        null=True)

    lot_number = models.CharField(
        verbose_name='Vaccine batch/lot number',
        max_length=20,
        blank=True,
        null=True, )

    expiry_date = models.DateField(
        verbose_name='Vaccination expiry date',
        validators=[date_is_future, ],
        blank=True,
        null=True)

    provider_name = EncryptedCharField(
        verbose_name='Name of the provider',
        max_length=35,
        blank=True,
        null=True)

    part_supervised = models.CharField(
        verbose_name='Was the participant supervised 15 minutes post-dosing?',
        max_length=3,
        choices=YES_NO_NA)

    adverse_event = models.CharField(
        verbose_name='Were any adverse events experienced?',
        max_length=3,
        choices=YES_NO_NA)

    next_vaccination_date = models.DateField(
        verbose_name=('When is the participant scheduled for their next '
                      'vaccination dose?'),
        validators=[date_is_future, ],
        blank=True,
        null=True)

    def validate_unique(self, exclude=None):
        """
        validated_unique had to be overridden because unique_together does not work
        with foreign keys or foreign keys yet each CRF for each participant can be uniquely
        be identified using the subject identifier obtained from the appointments
        """
        try:
            vaccination_details = VaccinationDetails.objects.get(
                subject_visit__appointment__subject_identifier=self.subject_identifier)
        except VaccinationDetails.DoesNotExist:
            pass
        else:
            if self.subject_visit.schedule_name != 'esr21_enrol_schedule' and \
                    vaccination_details.received_dose_before == self.received_dose_before:
                # cannot be first_dose == first_dose nor sec_dose == sec_dose
                # otherwise a constraint will be thrown
                error_message = '''\
                Indicated dose cannot be the same when the participant \
                when the participant was vaccinated before.
                '''
                raise IntegrityError(error_message)

        super(VaccinationDetails, self).validate_unique(exclude=exclude)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Collection of vaccination details'
        verbose_name_plural = 'Collection of vaccination details'
