from django.apps import apps as django_apps
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings
from django_crypto_fields.fields import (
    IdentityField, FirstnameField, LastnameField)
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future, date_not_future
from edc_base.sites.site_model_mixin import SiteModelMixin
# from edc_consent.field_mixins import IdentityFieldsMixin
from edc_constants.choices import GENDER, YES_NO
from edc_base.model_fields import IsDateEstimatedField
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import datetime_not_before_study_start
from ..choices import LANGUAGE, IDENTITY_TYPE
from edc_base.utils import get_utcnow


class InformedConsent(SiteModelMixin, BaseUuidModel):
    consent_datetime = models.DateTimeField(
        verbose_name='Consent datetime',
        default=get_utcnow,
        help_text='Date and time of consent.')

    first_name = FirstnameField(
        blank=False
    )

    last_name = LastnameField(
        blank=False
    )

    language = models.CharField(
        verbose_name='Language of consent',
        max_length=50,
        choices=settings.LANGUAGES,
        null=True,
        blank=True,
        help_text=(
            'The language used for the consent process will '
            'also be used during data collection.')
    )

    is_literate = models.CharField(
        verbose_name='Is the participant literate?',
        max_length=5,
        choices=YES_NO,
        help_text='If No provide witness name on this form and signature'
                  'on the paper document')

    witness_fname = FirstnameField(
        verbose_name='Witness first name',
        max_length=5, )

    witness_lname = LastnameField(
        verbose_name='Witness last name',
        max_length=5, )

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=1)

    date_of_birth = models.DateField(
        verbose_name="Date of birth",
        validators=[date_not_future, ])

    is_estimated = IsDateEstimatedField(
        verbose_name="Is date of birth estimated?",
        null=True,
        blank=False)
    national_identity = IdentityField(
        verbose_name='Patient ID number (Omang)',
        # validators=[identity_check, ],
        unique=True)

    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=25,
        choices=IDENTITY_TYPE)

    """"Review Questions"""

    reviewed_consent = models.CharField(
        verbose_name='I have reviewed the consent with the participant',
        max_length=3,
        choices=YES_NO,
        help_text='If no, participant is not eligible.')

    answered_all_questions = models.CharField(
        verbose_name='I have answered all questions the participant'
                     ' had about the study',
        max_length=3,
        choices=YES_NO,
        help_text='If no, participant is not eligible.')

    asked_questions = models.CharField(
        verbose_name='I have asked the participant questions about'
                     ' this study and the participant has demonstrated '
                     'understanding',
        max_length=3,
        choices=YES_NO,
        help_text='If no, participant is not eligible.')

    have_verified = models.CharField(
        verbose_name='I have verified that the participant has'
                     'signed the consent form',
        max_length=3,
        choices=YES_NO,
        help_text='If no, participant is not eligible.')

    copy_of_consent = models.CharField(
        verbose_name='I have provided the participant with a copy'
                     ' of their signed informed consent',
        max_length=3,
        choices=YES_NO,
        help_text='if declined, return copy with the consent')
