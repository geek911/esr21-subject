from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from edc_protocol.validators import date_not_before_study_start

from .model_mixins import CrfModelMixin
from ..choices import ACTION_TAKEN, STATUS, AE_GRADE, TREATMENT_RELATIONSHIP
from ..choices import OUTCOME


class AdverseEvent(CrfModelMixin):
    """"Adverse Event"""""

    experienced_ae = models.CharField(
        verbose_name='Did the participant experience any Adverse Event?',
        choices=YES_NO,
        max_length=3)

    ae_name = models.CharField(
        verbose_name='Name of the Adverse Event',
        max_length=100,
        blank=True,
        null=True)

    event_details = models.TextField(
        verbose_name='Details of the Adverse Event',
        blank=True,
        null=True)

    meddra_pname = models.CharField(
        verbose_name='MedDRA Preferred Name of the Adverse Event',
        max_length=100,
        blank=True,
        null=True)

    meddra_pcode = models.CharField(
        verbose_name='MedDRA Preferred Code of the Adverse Event',
        max_length=50,
        blank=True,
        null=True)

    meddra_version = models.PositiveIntegerField(
        verbose_name='MedDRA version',
        blank=True,
        null=True)

    start_date = models.DateField(
        verbose_name='Adverse Event start date',
        validators=[
            date_not_before_study_start,
            date_not_future, ],
        blank=True,
        null=True)

    stop_date = models.DateField(
        verbose_name='Adverse Event stop date',
        validators=[date_not_future, ],
        null=True,
        blank=True)

    status = models.CharField(
        verbose_name='Status of the Adverse Event',
        max_length=10,
        choices=STATUS,
        blank=True,
        null=True)

    ae_grade = models.CharField(
        verbose_name='FDA Severity Grading',
        max_length=30,
        choices=AE_GRADE,
        blank=True,
        null=True)

    study_treatmnt_rel = models.CharField(
        verbose_name='Relationship to study treatment',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP,
        blank=True,
        null=True)

    nonstudy_treatmnt_rel = models.CharField(
        verbose_name='Relationship to non-study treatment',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP,
        blank=True,
        null=True)

    studyproc_treatmnt_rel = models.CharField(
        verbose_name='Relationship to study procedure',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP,
        blank=True,
        null=True)

    action_taken = models.CharField(
        verbose_name='Action taken with study treatment',
        max_length=50,
        choices=ACTION_TAKEN,
        blank=True,
        null=True)

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
        choices=YES_NO,
        blank=True,
        null=True)

    special_interest_ae = models.CharField(
        verbose_name='Was the event an AE of Special Interest?',
        max_length=3,
        choices=YES_NO,
        help_text=('(If Yes, check all serious criteria that apply on the '
                   'corresponding SAE form.)'),
        blank=True,
        null=True)

    medically_attended_ae = models.CharField(
        verbose_name='Was the event a Medically attended AE?',
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    maae_specify = OtherCharField(
        verbose_name='If MAAE, specify',
        max_length=100, )

    treatment_given = models.CharField(
        verbose_name='Was treatment given?',
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    treatmnt_given_specify = OtherCharField(
        verbose_name='If yes, specify details')

    ae_study_discontinued = models.CharField(
        verbose_name='Did the AE cause the subject to discontinue from the study?',
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    discontn_dt = models.DateField(
        verbose_name='Date of discontinuation',
        blank=True,
        null=True)

    covid_related_ae = models.CharField(
        verbose_name='Is this a COVID-19 related AE?',
        max_length=3,
        choices=YES_NO,
        blank=True,
        null=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Adverse Event'
        verbose_name_plural = 'Adverse Events'
