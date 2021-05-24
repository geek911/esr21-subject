from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_base.model_fields import OtherCharField
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO, YES_NO_NA
from .list_models import ChronicConditions, ParticipantMedications, WcsDxAdult
from ..maternal_choices import KNOW_HIV_STATUS, IS_DATE_ESTIMATED


class PregnancyStatus(NonUniqueSubjectIdentifierFieldMixin,
                      SiteModelMixin, BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    """"Maternal Medical History"""""

    chronic_condition = models.CharField(
        verbose_name='Does the participant have any significant chronic'
                     ' condition(s) that were diagnosed prior to the current'
                     ' pregnancy and that remain ongoing?',
        choices=YES_NO,
        max_length=10,)

    who_diagnosed = models.CharField(
        verbose_name='Prior to the current pregnancy, was the participant'
                     'Yes ever diagnosed with a WHO Stage III or IV illness?',
        choices=YES_NO_NA,
        max_length=10,)

    who = models.ManyToManyField(
        WcsDxAdult,
        verbose_name='List any new WHO Stage III/IV diagnoses that are '
                     'not reported'
    )
    participant_chronic = models.ManyToManyField(
        ChronicConditions,
        max_length=10,
        related_name='caregiver',
        verbose_name=('Does the caregiver have any of the above. Tick all '
                      'that apply'),
    )

    participant_chronic_other = OtherCharField(
        max_length=35,
        verbose_name='If other, specify.',
        blank=True,
        null=True)

    participant_medications = models.ManyToManyField(
        ParticipantMedications,
        max_length=10,
        verbose_name='Does the participant currently take any of the '
                     'following medications.(tick all that apply)',
        blank=True
    )

    participant_medications_other = OtherCharField(
        max_length=35,
        verbose_name='If other, specify.',
        blank=True,
        null=True)

    sero_positive = models.CharField(
        verbose_name='Is the participant HIV sero-positive?',
        max_length=10,
        choices=YES_NO,)

    if_sero_positive = models.DateField(
        verbose_name='If HIV sero-positive, what is the approximate '
                     'date of diagnosis?',
        default=get_utcnow,)

    hiv_infected = models.CharField(
        verbose_name='Was the mother perinatally infected with HIV?',
        max_length=10,
        choices=YES_NO_NA,)

    know_hiv_status = models.CharField(
        verbose_name='Was the mother perinatally infected with HIV?',
        max_length=30,
        choices=KNOW_HIV_STATUS, )

    cd4_known = models.CharField(
        verbose_name='Is the participants lowest CD4 known?',
        max_length=10,
        choices=YES_NO_NA, )

    lowest_known_cd4 = models.IntegerField(
        verbose_name='What was the participants lowest known (nadir) CD4 '
                     'cell count (cells/mm3) at any time in the past?')
    date_cd4_test = models.DateField(
        verbose_name='Year/Month of CD4 test',
        default=get_utcnow, )

    is_estimated = models.CharField(
        verbose_name='Is the subject date of CD4 test estimated?',
        max_length=40,
        choices=IS_DATE_ESTIMATED)

    """""Maternal Obstetric History"""""

    prev_pregnancies = models.IntegerField(
        verbose_name=('Including this pregnancy, how many previous '
                      'pregnancies for this participant?'),
        validators=[MinValueValidator(1), MaxValueValidator(20), ],)

    pregs_24wks_or_more = models.IntegerField(
        verbose_name='Number of pregnancies at least 24 weeks?',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    lost_before_24wks = models.IntegerField(
        verbose_name='Number of pregnancies lost before 24 weeks gestation',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    lost_after_24wks = models.IntegerField(
        verbose_name='Number of pregnancies lost at or after 24 weeks'
                     ' gestation ',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    live_children = models.IntegerField(
        verbose_name='How many other living children does the '
                     'participant currently have (excluding baby to be '
                     'enrolled in the study)',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    children_died_b4_5yrs = models.IntegerField(
        verbose_name='How many of the participant\'s children died after '
                     'birth before 5 years of age? ',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    children_deliv_before_37wks = models.IntegerField(
        verbose_name='Number of previous pregnancies delivered at < 37'
                     ' weeks GA?',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )

    children_deliv_aftr_37wks = models.IntegerField(
        verbose_name='Number of previous pregnancies delivered at >= 37'
                     ' weeks GA?',
        validators=[MinValueValidator(0), MaxValueValidator(20), ],
    )
    comments = models.TextField(
        verbose_name='Comments',
    )

    class Meta:
        verbose_name = "Pregnancy Status"
        verbose_name_plural = "Pregnancy Status"
