from django.db import models
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin


class SampleCollection(CrfModelMixin):

    sample_collected = models.CharField(
        verbose_name='Sample collection:',
        choices=YES_NO,
        max_length=3)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Sample Collection'
        verbose_name_plural = 'Sample Collection'
