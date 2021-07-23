from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.sites import SiteModelMixin
from edc_constants.choices import SEVERITY_LEVEL

from .adverse_event import AdverseEvent
from .list_models import SAECriteria
from edc_constants.choices import YES_NO


class SeriousAdverseEvent(SiteModelMixin, BaseUuidModel):

    """""Serious Adverse Event (SAE)"""""

    adverse_event = models.ForeignKey(
        AdverseEvent,
        on_delete=models.PROTECT)

    sae_details = models.TextField(
        verbose_name='Details of the SAE', )

    sae_name = models.CharField(
        verbose_name='Name of the SAE',
        max_length=100)

    meddra_pname = models.CharField(
        verbose_name='MedDRA Preferred Name of the SAE',
        max_length=100)

    meddra_pcode = models.CharField(
        verbose_name='MedDRA Preferred Code OF the SAE',
        max_length=50)

    meddra_version = models.IntegerField(
        verbose_name='MedDRA version')

    sae_intensity = models.CharField(
        verbose_name='Intensity of the SAE',
        choices=SEVERITY_LEVEL,
        max_length=10)

    start_date = models.DateField(
        verbose_name='SAE start date',
        validators=[date_not_future, ])

    resolution_date = models.DateField(
        verbose_name='SAE end date',
        validators=[date_not_future, ],
        null=True,
        blank=True)

    date_aware_of = models.DateField(
        verbose_name="Date investigator became aware of SAE",
        validators=[date_not_future, ])

    seriousness_criteria = models.ManyToManyField(
        SAECriteria,
        verbose_name='Select seriousness criteria',
        help_text='(check all that apply)', )

    admission_date = models.DateField(
        verbose_name='If hospitalized, Date of Admission',
        validators=[date_not_future, ],
        null=True,
        blank=True)

    discharge_date = models.DateField(
        verbose_name='If hospitalized, Date of Discharge',
        null=True,
        blank=True)

    incapacity_specify = OtherCharField(
        verbose_name='Specify persistent or significant disability/incapacity',
        max_length=100)

    medical_event_other = OtherCharField(
        verbose_name='If, Other important medical event, specify',
        max_length=100)

    rationale = models.CharField(
        verbose_name=('Investigator\'s rationale for Study Treatment being '
                      'Related to the events'),
        max_length=100)

    event_abate = models.CharField(
        verbose_name='Did the event abate after drug discontinuation?',
        choices=YES_NO,
        max_length=3)

    describe_sae_treatmnt = models.TextField(
        verbose_name='Describe treatment for event including medications',
        max_length=200)

    test_performed = models.TextField(
        verbose_name='List all diagnostic tests that were performed to confirm event',
        max_length=200)

    additional_info = models.TextField(
        verbose_name=('Additional information (for example: history of '
                      'presenting illness, course of illness, complications, '
                      'risk factors and/or other contributing factors)'),
        max_length=200)

    class Meta:
        app_label = 'esr21_subject'
        verbose_name = 'Serious Adverse Event'
        verbose_name_plural = 'Serious Adverse Events'
