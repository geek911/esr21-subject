from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO_NA, GENDER

from ..maternal_choices import ETHNICITY, RACE, CHILDBEARING
from .model_mixins import CrfModelMixin
from .list_models import SubjectRace


class DemographicsData(CrfModelMixin):

    date_of_birth = models.DateField(
        verbose_name='Date of Birth (YYYY)', )

    age = models.CharField(
        max_length=25,
        verbose_name='Age', )

    gender = models.CharField(
        verbose_name='Gender',
        choices=GENDER,
        max_length=1)

    childbearing_potential = models.CharField(
        max_length=25,
        verbose_name='Is the subject a woman of childbearing potential?',
        choices=YES_NO_NA)

    if_no_reason = models.CharField(
        max_length=25,
        verbose_name='If No, reason',
        choices=CHILDBEARING,
        null=True,
        blank=True)

    if_no_reason_other = OtherCharField(
        max_length=50,
        verbose_name='Other, specify',
        blank=True,
        null=True, )

    ethnicity = models.CharField(
        max_length=25,
        verbose_name='Ethnicity ',
        choices=ETHNICITY)

    ethnicity_other = OtherCharField(
        max_length=35,
        verbose_name='If other specify...',
        blank=True,
        null=True, )

    race_of_subject = models.CharField(
        max_length=75,
        verbose_name='Race of Subject',
        choices=RACE,)

    race = models.ManyToManyField(
        SubjectRace,
        max_length=35,
        verbose_name='If Reported, Check ALL that apply:',
        blank=True, )

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Demographic Data'
        verbose_name_plural = 'Demographic Data'
