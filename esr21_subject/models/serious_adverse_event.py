from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.sites import SiteModelMixin
from edc_constants.choices import SEVERITY_LEVEL, YES_NO

from .list_models import SAECriteria
from .model_mixins import CrfModelMixin


class SeriousAdverseEventRecordManager(models.Manager):

    def get_by_natural_key(self, sae_name, start_date, serious_adverse_event):
        return self.get(serious_adverse_event=serious_adverse_event,
                        sae_name=sae_name,
                        start_date=start_date)


class SeriousAdverseEvent(CrfModelMixin):

    """""Serious Adverse Events (SAE)"""""

    class Meta:
        app_label = 'esr21_subject'
        verbose_name = 'Serious Adverse Event'


class SeriousAdverseEventRecord(SiteModelMixin, BaseUuidModel):

    serious_adverse_event = models.ForeignKey(
        SeriousAdverseEvent,
        on_delete=models.PROTECT)

    sae_details = models.TextField(
        verbose_name='Details of the SAE',)

    sae_name = models.CharField(
        verbose_name='Name of the SAE',
        max_length=100)

    meddra_pname = models.CharField(
        verbose_name='MedDRA Preferred Name of the SAE',
        max_length=100,
        blank=True,
        null=True)

    meddra_pcode = models.CharField(
        verbose_name='MedDRA Preferred Code OF the SAE',
        max_length=50,
        blank=True,
        null=True)

    meddra_version = models.PositiveIntegerField(
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
        help_text='(check all that apply)',)

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
    
    ae_number = models.TextField(
        verbose_name='AE Number',
        blank=True,
        null=True)

    ae_term = models.CharField(
        verbose_name='Adverse Event Reported Term',
        max_length=200
    )

    aes_dat = models.CharField(
        verbose_name='Date AE Met Criteria for Serious AE',
        max_length=10
    )

    ae_siadat = models.CharField(
        verbose_name='Date Investigator Aware of Serious AE',
        max_length=10
    )

    ae_sdth = models.CharField(
        verbose_name='Results in Death',
        max_length=3,
        choices=YES_NO
    )

    ae_shosp = models.CharField(
        verbose_name='Requires or Prolongs Hospitalization',
        max_length=3,
        choices=YES_NO
    )

    ae_scong = models.CharField(
        verbose_name='Congenital Anomaly or Birth Defect',
        max_length=6,
        choices=YES_NO
    )

    ae_slife = models.CharField(
        verbose_name='Is Life Threatening',
        max_length=6,
        choices=YES_NO
    )

    ae_sdisab = models.CharField(
        verbose_name='Persist. or Sign. Disability/Incapacity',
        max_length=6,
        choices=YES_NO
    )

    ae_smie = models.CharField(
        verbose_name='Other Medically Important Serious Event',
        max_length=6,
        choices=YES_NO
    )

    ae_shodat = models.CharField(
        verbose_name='Date of Hospitalization',
        max_length=10,
        choices=YES_NO
    )

    ae_sdidat = models.CharField(
        verbose_name='Date of Discharge',
        max_length=10,
    )

    dthcaus_1 = models.CharField(
        verbose_name='Primary Cause of Death',
        max_length=200,
    )

    dthcaus_2 = models.CharField(
        verbose_name='Secondary Cause of Death',
        max_length=200,
    )

    ae_sautop = models.CharField(
        verbose_name='Autopsy Performed',
        max_length=10,
        choices=YES_NO
    )

    ad = models.CharField(
        verbose_name='Additional Drug',
        max_length=10,
    )

    ae_caad = models.CharField(
        verbose_name='AE Caused by Additional Drug',
        max_length=10,
    )

    ae_smedca = models.CharField(
        verbose_name='SAE Caused by Other Medication',
        max_length=10,
    )
    
    ae_smed = models.CharField(
        verbose_name='Other Medication',
        max_length=200,
    )
    
    ae_caussp = models.CharField(
        verbose_name='Other Medication',
        max_length=200,
    )

    ae_sp = models.CharField(
        verbose_name='Study Procedure(s)',
        max_length=200,
    )
    
    

    history = HistoricalRecords()

    objects = SeriousAdverseEventRecordManager()

    def natural_key(self):
        return (self.sae_name, self.start_date,) + self.serious_adverse_event.natural_key()

    natural_key.dependencies = ['esr21_subject.seriousadverseevent']

    class Meta:
        app_label = 'esr21_subject'
        unique_together = ('serious_adverse_event', 'start_date', 'date_aware_of')
        verbose_name = 'Serious Adverse Event Record'
