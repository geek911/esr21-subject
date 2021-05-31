from django.db import models

from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin
from ..choices import ACTION_TAKEN, STATUS, AE_GRADE, TREATMENT_RELATIONSHIP
from ..choices import OUTCOME


class AdverseEvent(CrfModelMixin):
    """"Adverse Event"""""

    event_details = models.TextField(
        verbose_name='Details of the Adverse Event', )

    start_date = models.DateField(
        verbose_name='Adverse Event start date', )

    status = models.CharField(
        verbose_name='Status of the Adverse Event',
        max_length=10,
        choices=STATUS, )

    resolution_date = models.DateField(
        verbose_name='Adverse Event end date',
        null=True,
        blank=True)

    ae_grade = models.CharField(
        verbose_name='FDA Severity Grading',
        max_length=30,
        choices=AE_GRADE, )

    study_treatmnt_rel = models.CharField(
        verbose_name='Relationship to study treatment',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP, )

    nonstudy_treatmnt_rel = models.CharField(
        verbose_name='Relationship to non-study treatment',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP, )

    studyproc_treatmnt_rel = models.CharField(
        verbose_name='Relationship to study procedure',
        max_length=15,
        choices=TREATMENT_RELATIONSHIP, )

    action_taken = models.CharField(
        verbose_name='Action taken with study treatment',
        max_length=50,
        choices=ACTION_TAKEN, )

    outcome = models.CharField(
        verbose_name='Outcome',
        max_length=50,
        choices=OUTCOME, )

    sequelae_specify = OtherCharField(
        verbose_name='If Recovered / resolved with sequelae, please specify sequelae',
        max_length=100, )

    serious_event = models.CharField(
        verbose_name='Serious Event?',
        max_length=3,
        choices=YES_NO, )

    special_interest_ae = models.CharField(
        verbose_name='Was the event an AE of Special Interest?',
        max_length=3,
        choices=YES_NO,
        help_text=('(If Yes, check all serious criteria that apply on the '
                   'corresponding SAE form.)'), )

    medically_attended_ae = models.CharField(
        verbose_name='Was the event a Medically attended AE?',
        max_length=3,
        choices=YES_NO, )

    maae_specify = OtherCharField(
        verbose_name='If MAAE, specify',
        max_length=100, )

    treatment_given = models.CharField(
        verbose_name='Was treatment given?',
        max_length=3,
        choices=YES_NO, )

    ae_study_discontinued = models.CharField(
        verbose_name='Did the AE cause the subject to discontinue from the study?',
        max_length=3,
        choices=YES_NO, )

    covid_related_ae = models.CharField(
        verbose_name='Is this a COVID-19 related AE?',
        max_length=3,
        choices=YES_NO, )

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Adverse Event'
        verbose_name_plural = 'Adverse Events'
