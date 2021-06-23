from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from edc_protocol.validators import date_not_before_study_start

from .list_models import MedicationIndication
from .model_mixins import CrfModelMixin
from ..choices import AE_GRADE, UNIT_OPTIONS


class AdverseEvent(CrfModelMixin):
    """Concomitant Medications"""

    medication = models.CharField(
        verbose_name='Medication',
        max_length=25,
        help_text='Please use generic drug name or trade name for combination drugs')

    indication = models.ManyToManyField(
        MedicationIndication,
        verbose_name='Indication',
        max_length=25,
        help_text='Please tick all that apply')

    indication_other = OtherCharField(
        verbose_name='if \'Prophylaxis\' or \'Other\' above, please specify')

    ae_number = models.CharField(
        verbose_name=('If indication is \'Adverse Event,\' select the corresponding Adverse '
                      'event number'),
        max_length=25,
        choices=AE_GRADE)

    dose = models.CharField(
        max_length=5,)

    unit = models.CharField(
        max_length=25,
        choices=UNIT_OPTIONS)
