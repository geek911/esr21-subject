from django.db import models

from edc_constants.choices import YES_NO

from .list_models import Symptoms, Diseases
from ..choices import SMOKED_STATUS_CHOICES, ALCOHOL_STATUS_CHOICES, MODE_OF_TRANSPORT_CHOICE

from .model_mixins import CrfModelMixin


class MedicalHistory(CrfModelMixin):
    relevant_history = models.CharField(
        verbose_name='Does the subject have any relevant Medical History?',
        max_length=10,
        choices=YES_NO, )

    was_subject_infected_before = models.CharField(
        verbose_name='Has the participant had a prior infection of SARS-CoV-2/COVID 19?',
        max_length=10,
        choices=YES_NO, )

    # TODO: Needed if {was_subject_infected_before} is 'yes'
    symptoms = models.ManyToManyField(
        Symptoms,
        verbose_name='If yes, did the participant experience any symptoms? ')

    # TODO: Needed if {symptoms} is 'other'
    is_other = models.TextField(
        verbose_name='If other specify', )

    smoking_status = models.CharField(
        choices=SMOKED_STATUS_CHOICES,
        verbose_name='Smoking status/history',
        max_length=20, )

    alcohol_status = models.CharField(
        choices=ALCOHOL_STATUS_CHOICES,
        verbose_name='Alcohol Use',
        max_length=20,
    )

    diabetes = models.CharField(
        verbose_name="Is the participant diabetes mellitus?",
        choices=YES_NO
    )

    comorbidities = models.ManyToManyField(Diseases, verbose_name='Comorbidities')

    # TODO: If {comorbidities} is 'other'
    other_specify = models.CharField(
        verbose_name='Other specify',
        max_length=50, )

    no_of_mass_gathering = models.PositiveIntegerField(
        default=0,
        verbose_name='How many mass gatherings has the participant attended in the preceding 12 weeks?'
    )

    no_internal_trips = models.PositiveIntegerField(
        default=0,
        verbose_name='How many COVID-19 inter-zonal trips has the participant made in Botswana in the past 12 weeks?'
    )

    mode_of_transport = models.CharField(
        choices=MODE_OF_TRANSPORT_CHOICE,
        verbose_name='Mode of Transport'
    )

    using_shared_kitchen = models.CharField(
        choices=YES_NO,
        verbose_name='Is the participant using a shared kitchen/dinning at work?'
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Medical History'
        verbose_name_plural = 'Medical History'


class MedicalDiagnosis(CrfModelMixin):
    medical_history_diagnosis = models.CharField(
        verbose_name='Medical History Diagnosis',
        max_length=29)
    start_date = models.DateField(
        verbose_name='Start Date (DD/MMM/YYYY)', )

    end_date = models.DateField(
        verbose_name='End Date (DD/MMM/YYYY)', )

    ongoing = models.CharField(
        verbose_name='Ongoing',
        choices=YES_NO,
        max_length=5)

    subject_taking_medicine = models.CharField(
        verbose_name='Is the subject taking medication related to this condition?',
        choices=YES_NO,
        max_length=5)

    cm_log_line = models.CharField(
        max_length=200,
        verbose_name='CM log line')

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Medical Diagnosis'
        verbose_name_plural = 'Medical Diagnosis'
