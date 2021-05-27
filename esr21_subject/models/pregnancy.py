from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_constants.choices import POS_NEG, YES_NO


class Pregnancy(SiteModelMixin, BaseUuidModel):

    preg_performed = models.CharField(
        verbose_name='Was the pregnancy test performed?',
        max_length=20,
        choices=YES_NO,
        help_text=(
            'The language used for the consent process will '
            'also be used during data collection.')
    )

    preg_date = models.DateTimeField(
        verbose_name='Date of pregnancy test',
        help_text=' (DD MMM YYYY)')

    result = models.CharField(
        verbose_name="Result",
        choices=POS_NEG,
        max_length=20)

    class Meta:
        verbose_name = "Pregnancy"
        verbose_name_plural = "Pregnancy"
