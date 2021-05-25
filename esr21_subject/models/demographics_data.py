from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO, YES_NO_NA, NOT_APPLICABLE

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow
from ..maternal_choices import (MARITAL_STATUS, ETHNICITY, HIGHEST_EDUCATION,
                                CURRENT_OCCUPATION, MONEY_PROVIDER,
                                MONEY_EARNED, WATER_SOURCE, TOILET_FACILITY,
                                HOUSE_TYPE)


class DemographicsData(NonUniqueSubjectIdentifierFieldMixin,
                       SiteModelMixin, BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    marital_status = models.CharField(
        max_length=25,
        verbose_name="Current Marital status ",
        choices=MARITAL_STATUS)

    marital_status_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
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

    highest_education = models.CharField(
        max_length=25,
        verbose_name="Highest educational level completed ",
        choices=HIGHEST_EDUCATION)

    current_occupation = models.CharField(
        max_length=75,
        verbose_name="Current occupation",
        choices=CURRENT_OCCUPATION)

    current_occupation_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True, )

    provides_money = models.CharField(
        max_length=50,
        verbose_name="Who provides most of your money?",
        choices=MONEY_PROVIDER)

    provides_money_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True, )

    money_earned = models.CharField(
        max_length=50,
        verbose_name="How much money do you personally earn? ",
        choices=MONEY_EARNED)

    money_earned_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True, )

    own_phone = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="Do you have your own cell phone that you use regularly?",
        blank=True,
        null=True, )

    water_source = models.CharField(
        max_length=50,
        verbose_name="At your primary home  where do you "
                     "get most of your family's drinking water?",
        choices=WATER_SOURCE,
        blank=True,
        null=True, )

    house_electrified = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name="Is there electricity in this house / compound? ",
        blank=True,
        null=True, )

    toilet_facility = models.CharField(
        max_length=50,
        verbose_name=("Which of the following types of toilet facilities do "
                      "you most often use at this house / compound? "),
        choices=TOILET_FACILITY,
        blank=True,
        null=True, )

    toilet_facility_other = OtherCharField(
        max_length=35,
        verbose_name="if other specify...",
        blank=True,
        null=True, )

    house_people_number = models.IntegerField(
        verbose_name="How many people, including yourself, "
                     "stay in this home / compound most of the time?",
        blank=True,
        null=True)

    house_type = models.CharField(
        max_length=50,
        verbose_name="Housing type? ",
        choices=HOUSE_TYPE,
        blank=True,
        null=True,)

    class Meta:
        verbose_name = "DemographicsData"
        verbose_name_plural = "DemographicsData"
