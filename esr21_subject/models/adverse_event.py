from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.sites import SiteModelMixin
from edc_constants.choices import YES_NO
from edc_protocol.validators import date_not_before_study_start

from ..choices import ACTION_TAKEN, STATUS, AE_GRADE, TREATMENT_RELATIONSHIP, TREATMENT_RELATIONSHIP_WITH_NA
from ..choices import OUTCOME
from .model_mixins import CrfModelMixin


class AdverseEventRecordManager(models.Manager):

    def get_by_natural_key(self, ae_name, start_date, adverse_event):
        return self.get(adverse_event=adverse_event,
                        ae_name=ae_name,
                        start_date=start_date)


class AdverseEvent(CrfModelMixin):
    """"Adverse Event"""""

    experienced_ae = models.CharField(
        verbose_name='Did the participant experience any Adverse Event?',
        choices=YES_NO,
        max_length=3)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Adverse Event'


class AdverseEventRecord(SiteModelMixin, BaseUuidModel):

    adverse_event = models.ForeignKey(
        AdverseEvent,
        on_delete=models.PROTECT,
        max_length=25)

    ae_name = models.CharField(
        verbose_name='Name of the Adverse Event',
        max_length=100,)

    event_details = models.TextField(
        verbose_name='Details of the Adverse Event',
        blank=True,
        null=True)

    ae_number = models.TextField(
        verbose_name='AE Number',
        blank=True,
        null=True)

    ae_term = models.TextField(
        verbose_name='Adverse Event Reported Term',
        blank=True,
        null=True)

    start_date = models.DateField(
        verbose_name='Adverse Event start date',
        validators=[
            date_not_before_study_start,
            date_not_future, ])

    stop_date = models.DateField(
        verbose_name='Adverse Event stop date',
        validators=[date_not_future, ],
        null=True,
        blank=True)

    # TODO: Question 3
    substance_hypersensitivity = models.CharField(
        verbose_name=('Any hypersensitivity to the active substance or to any of the '
                    'excipients?'),
        choices=YES_NO,
        max_length=3,
    )

    status = models.CharField(
        verbose_name='Status of the Adverse Event',
        max_length=10,
        choices=STATUS,)

    ae_grade = models.CharField(
        verbose_name='Common Terminology Criteria for Adverse Events (CTCAE) grading',
        max_length=30,
        choices=AE_GRADE)

    study_treatmnt_rel = models.CharField(
        verbose_name='Relationship to study treatment',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP)

    nonstudy_treatmnt_rel = models.CharField(
        verbose_name='Relationship to non-study treatment',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP)

    studyproc_treatmnt_rel = models.CharField(
        verbose_name='Relationship to study procedure',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP_WITH_NA,
    )

    action_taken = models.CharField(
        verbose_name='Action taken with study treatment',
        max_length=25,
        choices=ACTION_TAKEN)

    outcome = models.CharField(
        verbose_name='Outcome',
        max_length=50,
        choices=OUTCOME,
        blank=True,
        null=True)

    sequelae_specify = OtherCharField(
        verbose_name='If Recovered / resolved with sequelae, please specify sequelae',
        max_length=100)

    serious_event = models.CharField(
        verbose_name='Was this considered to be a Serious Adverse Event?',
        max_length=3,
        choices=YES_NO)

    special_interest_ae = models.CharField(
        verbose_name='Was the event an AE of Special Interest?',
        max_length=3,
        choices=YES_NO,
        help_text=('(If Yes, check all serious criteria that apply on the '
                'corresponding SAE form.)'))

    medically_attended_ae = models.CharField(
        verbose_name='Was the event a Medically attended AE?',
        max_length=3,
        choices=YES_NO)

    maae_specify = OtherCharField(
        verbose_name='If MAAE, specify',
        max_length=100,)
    
    hospitalized = models.CharField(
        verbose_name='Was the participant hospitalized?',
        max_length=3,
        choices=YES_NO)

    treatment_given = models.CharField(
        verbose_name='Was treatment given?',
        max_length=3,
        choices=YES_NO)

    treatmnt_given_specify = OtherCharField(
        verbose_name='If yes, specify details')

    ae_study_discontinued = models.CharField(
        verbose_name='Did the AE cause the subject to discontinue from the study?',
        max_length=3,
        choices=YES_NO)

    discontn_dt = models.DateField(
        verbose_name='Date of discontinuation',
        blank=True,
        null=True)

    covid_related_ae = models.CharField(
        verbose_name='Is this a COVID-19 related AE?',
        max_length=3,
        choices=YES_NO)
    
    invest_product = models.CharField(
        verbose_name='Investigational Product',
        max_length=20)

    ae_rel = models.CharField(
        verbose_name=('Was AE caused by investigational product (IP)?'),
        choices=YES_NO,
        max_length=3,
    )

    aecontfr = models.CharField(
        verbose_name=('Continued from AE Section X*? '),
        choices=YES_NO,
        max_length=3,
    )

    llt_code = models.PositiveIntegerField(
        verbose_name=('MedDRA Lowest Level Term Code'),
    )

    llt_name = models.CharField(
        verbose_name=('MedDRA Lowest Level Term Name'),
        max_length=200,
    )

    pt_code = models.CharField(
        verbose_name='MedDRA Preferred Term Code',
        max_length=10,
    )

    pt_name = models.CharField(
        verbose_name='MedDRA Preferred Term Name',
        max_length=200,
    )

    hlt_code = models.PositiveIntegerField(
        verbose_name='MedDRA High Level Term Code',
    )

    hlt_name = models.CharField(
        verbose_name='MMedDRA High Level Term Name',
        max_length=6,
    )

    hlgt_code = hlt_name = models.PositiveIntegerField(
        verbose_name='MedDRA High Level Group Term Code',
    )

    hlgt_name = models.CharField(
        verbose_name='MedDRA High Level Group Term Name',
        max_length=200,
    )

    soc_code = models.PositiveIntegerField(
        verbose_name='MedDRA System Organ Class Code',
    )

    soc_name = models.CharField(
        verbose_name='MedDRA System Organ Class Name',
        max_length=200,
    )

    meddra_v = hlgt_name = models.CharField(
        verbose_name='MedDRA Version',
        max_length=5,
    )

    ctcae_v = models.CharField(
        verbose_name='CTCAE Version',
        max_length=5,
    )



    objects = AdverseEventRecordManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.ae_name, self.start_date,) + self.adverse_event.natural_key()

    natural_key.dependencies = ['esr21_subject.adverseevent']

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Adverse Event Record'
        app_label = 'esr21_subject'
