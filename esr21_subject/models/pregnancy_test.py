from django.db import models
from edc_constants.choices import POS_NEG, YES_NO
from edc_base.model_validators.date import datetime_not_future

from .model_mixins import CrfModelMixin


class Pregnancy(CrfModelMixin):

    preg_performed = models.CharField(
        verbose_name='Was the pregnancy test performed?',
        max_length=20,
        choices=YES_NO,
        help_text=(
            'The language used for the consent process will '
            'also be used during data collection.'))

    preg_date = models.DateTimeField(
        verbose_name='Date of pregnancy test',
        validators=[datetime_not_future, ],
        help_text=' (DD MMM YYYY)')

    result = models.CharField(
        verbose_name='Result',
        choices=POS_NEG,
        max_length=20)

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Pregnancy Test'
        verbose_name_plural = 'Pregnancy Test'
