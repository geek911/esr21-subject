from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager, SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow


# from .model_mixins import SearchSlugModelMixin


class EligibilityCheckList(NonUniqueSubjectIdentifierFieldMixin,
                           SiteModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(
        verbose_name="Subject ID",
        max_length=36,
        unique=True, )

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    age_in_years = models.IntegerField(
        verbose_name='What is the participants age?',
        help_text='(Years)', )

    class Meta:
        verbose_name = "EligibilityCheckList"
        verbose_name_plural = "EligibilityCheckList"
