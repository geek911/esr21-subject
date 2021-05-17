from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from ..choices import STATUS, AE_GRADE


class AdverseEvents(NonUniqueSubjectIdentifierFieldMixin,
                    SiteModelMixin, BaseUuidModel):
    report_date_time = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    """"Adverse Event"""""

    event_details = models.TextField(
        verbose_name='Details of the Adverse Even', )

    start_date = models.DateTimeField(
        verbose_name="Adverse Event start date (and time)",
        default=get_utcnow, )

    status = models.CharField(
        verbose_name="Status of the Adverse Event",
        max_length=10,
        choices=STATUS,
    )
    resolution_date = models.DateTimeField(
        verbose_name="AdverseEvent resolution date and time",
        default=get_utcnow, )

    ae_grade = models.CharField(
        verbose_name="Grade AE severity (intensity)",
        max_length=30,
        choices=AE_GRADE)

    rating = models.CharField(
        verbose_name="Investigator causality rating against the "
                     "Investigational Product(s)",
        max_length=30,
        choices=YES_NO,)

    action_taken = models.CharField(
        verbose_name="Action taken with regard to Investigational Product(s)",
        max_length=50,
    )
    study_withdrawal = models.CharField(
        verbose_name="AE caused participant's withdrawal from the study?",
        max_length=10,
        choices=YES_NO,)

    outcome = models.CharField(
        verbose_name="Outcome",
        max_length=50,
    )

    """""Serious Adverse Event (SAE)"""""

    date_met_criteria = models.DateTimeField(
        verbose_name="Date Adverse Event(AE) met criteria for Serious "
                     "Adverse Event(SAE)",
        default=get_utcnow, )

    date_aware_of = models.DateTimeField(
        verbose_name="Date investigator became aware of serious Adverse Event",
        default=get_utcnow, )

    reasons_serious = models.TextField(
        verbose_name="Reasons Adverse Event is serious",
    )

    was_hospitalized = models.CharField(
        verbose_name="Was the participant hospitalised?",
        max_length=10,
        choices=YES_NO, )

    date_hospitalized = models.DateField(
        verbose_name="Date of hospitalisation",
        default=get_utcnow, )

    participant_discharged = models.CharField(
        verbose_name="Has the participant been discharged?",
        max_length=10,
        choices=YES_NO, )

    date_discharged = models.DateField(
        verbose_name="Date of discharge",
        default=get_utcnow,)

    probable_death_cause = models.CharField(
        verbose_name="Probable cause of death",
        max_length=50,
    )

    date_of_death = models.DateField(
        verbose_name="Date of discharge",
        default=get_utcnow, )

    performed_autopsy = models.CharField(
        verbose_name="Was an autopsy performed?",
        max_length=10,
        choices=YES_NO, )

    class Meta:
        verbose_name = "Adverse Events"
        verbose_name_plural = "Adverse Events"
