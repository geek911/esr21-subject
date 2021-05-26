from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow

from ..identifiers import ScreeningIdentifier
from .eligibility import Eligibility


class EligibilityConfirmation(NonUniqueSubjectIdentifierFieldMixin,
                              SiteModelMixin, BaseUuidModel):

    identifier_cls = ScreeningIdentifier

    screening_identifier = models.CharField(
        verbose_name="Eligibility Identifier",
        max_length=36,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    age_in_years = models.IntegerField(
        verbose_name='What is the participants age?',
        help_text='(Years)', )

    ineligibility = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    # is updated via signal once subject is consented
    is_consented = models.BooleanField(
        default=False,
        editable=False)

    def __str__(self):
        return self.screening_identifier

    def save(self, *args, **kwargs):
        eligibility_criteria = Eligibility(self.age_in_years)
        self.is_eligible = eligibility_criteria.is_eligible
        self.ineligibility = eligibility_criteria.error_message
        if not self.screening_identifier:
            self.screening_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'esr21_subject'
        verbose_name = 'Eligibility Confirmation'
        verbose_name_plural = 'Eligibility Confirmation'
