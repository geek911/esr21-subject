from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO, YES_NO_NA, NOT_APPLICABLE

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import GENDER
from ..maternal_choices import (ETHNICITY, RACE, MONEY_PROVIDER,
                                MONEY_EARNED, WATER_SOURCE, TOILET_FACILITY,
                                HOUSE_TYPE, CHILDBEARING)
from .list_models import SubjectRace


class DemographicsData(NonUniqueSubjectIdentifierFieldMixin,
                       SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    date_of_birth = models.DateField(
        verbose_name='Date of Birth (YYYY)',
        help_text='(integrated, no entry required)', )

    age = models.CharField(
        max_length=25,
        verbose_name="Age",
        help_text='(integrated, no entry required)', )

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=1)

    childbearing_potential = models.CharField(
        max_length=25,
        verbose_name="Is the subject a woman of childbearing potential?",
        choices=YES_NO_NA)

    if_no_reason = models.CharField(
        max_length=25,
        verbose_name="If No, reason",
        choices=CHILDBEARING, )

    if_no_reason_other = models.CharField(
        max_length=50,
        verbose_name="Other, specify",
        blank=True,
        null=True, )

    ethnicity = models.CharField(
        max_length=25,
        verbose_name="Ethnicity ",
        choices=ETHNICITY)

    ethnicity_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True, )

    race_of_subject = models.CharField(
        max_length=75,
        verbose_name="Race of Subject",
        choices=RACE,)

    race = models.ManyToManyField(
        SubjectRace,
        max_length=35,
        verbose_name="if Reported, Check ALL that apply below:",
        blank=True, )

    class Meta:
        verbose_name = "Demographic Data"
        verbose_name_plural = "Demographic Data"
