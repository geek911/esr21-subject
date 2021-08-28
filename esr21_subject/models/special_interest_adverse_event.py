from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.sites import SiteModelMixin

from .adverse_event import AdverseEvent
from ..choices import AESI_CATEGORY


class SpecialInterestAdverseEventManager(models.Manager):

    def get_by_natural_key(self, meddra_pname, start_date, adverse_event):
        return self.get(adverse_event=adverse_event,
                        meddra_pname=meddra_pname,
                        start_date=start_date)


class SpecialInterestAdverseEvent(SiteModelMixin, BaseUuidModel):

    """""Adverse Event of Special Interest (AESI)"""""

    adverse_event = models.ForeignKey(
        AdverseEvent,
        on_delete=models.PROTECT)

    aesi_name = models.CharField(
        verbose_name='Name of the AESI',
        max_length=100)

    meddra_pname = models.CharField(
        verbose_name='MedDRA Preferred Name of the AESI',
        max_length=100)

    meddra_pcode = models.CharField(
        verbose_name='MedDRA Preferred Code of the AESI',
        max_length=50)

    meddra_version = models.IntegerField(
        verbose_name='MedDRA version')

    start_date = models.DateField(
        verbose_name='AESI start date',
        validators=[date_not_future, ])

    end_date = models.DateField(
        verbose_name='AESI end date',
        validators=[date_not_future, ],
        null=True,
        blank=True)

    date_aware_of = models.DateField(
        verbose_name="Date investigator became aware of AESI",
        validators=[date_not_future, ])

    aesi_category = models.CharField(
        verbose_name='AESI category',
        max_length=50,
        choices=AESI_CATEGORY,)

    rationale = models.CharField(
        verbose_name=('Investigator\'s rationale for Study Treatment being '
                      'related to the events'),
        max_length=100)

    describe_aesi_treatmnt = models.TextField(
        verbose_name='Describe treatment for event including medications',
        max_length=200)

    additional_info = models.TextField(
        verbose_name=('Additional information (Symptoms, course, results, '
                      'diagnostic and other comments)'),
        max_length=200)

    history = HistoricalRecords()

    objects = SpecialInterestAdverseEventManager()

    def natural_key(self):
        return (self.meddra_pname, self.start_date,) + self.adverse_event.natural_key()

    natural_key.dependencies = ['esr21_subject.adverseevent']

    class Meta:
        app_label = 'esr21_subject'
        unique_together = ('adverse_event', 'start_date', 'end_date',
                           'aesi_category')
        verbose_name = 'Adverse Event of Special Interest'
        verbose_name_plural = 'Adverse Events of Special Interest'
