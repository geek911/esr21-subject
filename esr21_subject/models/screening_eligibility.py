from django.db import models
from edc_search.model_mixins import SearchSlugManager
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.model_mixins import BaseUuidModel
from .model_mixins import SearchSlugModelMixin
from edc_base.model_managers import HistoricalRecords




from edc_constants.choices import YES_NO
from edc_constants.constants import NO
from .list_models import Symptoms, Diseases
from edc_base.utils import get_utcnow
from edc_base.model_validators import datetime_not_future
from edc_base.sites import SiteModelMixin


class EligibilityConfirmationManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class ScreeningEligibility(NonUniqueSubjectIdentifierFieldMixin,SiteModelMixin,SearchSlugModelMixin, BaseUuidModel):
    
    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text='Date and time of report.')
    
    pregnancy_status = models.CharField(
        verbose_name=('Are you pregnant or nursing or do you plan to get pregnant in the next '
                    '3 months?'),
        max_length=3,
        choices=YES_NO,
        default=NO
    )

    # ADDED QUESTIONS FROM THE DOC
    thrombosis_or_thrombocytopenia = models.CharField(
        verbose_name=('Does individuals have any risk factors for or a reported history of '
                    'thrombosis and/or thrombocytopenia?'),
        max_length=3,
        choices=YES_NO,
        default=NO,
    )

    clinical_bleeding = models.CharField(
        verbose_name=('Ever experienced clinically significant bleeding, or prior history '
                    'of significant bleeding or bruising following intramuscular injections '
                    'or venepuncture?'),
        max_length=20,
        choices=YES_NO,
        default=NO,
        help_text=('(eg, factor deficiency, coagulopathy, or '
                'platelet disorder) '),
    )

    guillain_barre_syndrome = models.CharField(
        verbose_name='Any history of Guillain-Barré syndrome?',
        max_length=3,
        choices=YES_NO,
        default=NO)

    suspected_immuno_condition = models.CharField(
        verbose_name=('Any confirmed or suspected immunosuppressive or immunodeficient state '
                    '(including Asplenia)?'),
        max_length=3,
        choices=YES_NO,
        default=NO,)

    comorbidities = models.ManyToManyField(
        Diseases,
        verbose_name='Comorbidities'
    )

    comorbidities_other = models.CharField(
        verbose_name='Other specify',
        max_length=50,
        blank=True,
        null=True)

    covid_symptoms = models.ManyToManyField(
        Symptoms,
        verbose_name='Did the participant experience any symptoms?',
        blank=True)

    symptoms_other = models.TextField(
        verbose_name='If other specify',
        blank=True,
        null=True)

    history = HistoricalRecords()

    objects = EligibilityConfirmationManager()

    def __str__(self):
        return self.subject_identifier

    def natural_key(self):
        return (self.subject_identifier,)

    natural_key.dependencies = ['sites.Site']

    def save(self, *args, **kwargs):
        #check for elegibility also
        if not self.subject_identifier:
            self.subject_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)   

    class Meta:
        app_label = 'esr21_subject'
        verbose_name = 'Screening Eligibility'
        verbose_name_plural = 'Screening Eligibility'
