from django.db import models
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from edc_protocol.validators import date_not_before_study_start

from .model_mixins import CrfModelMixin
from ..choices import POS_NEG_IND


class RapidHIVTesting(CrfModelMixin):

    rapid_test_done = models.CharField(
        verbose_name='Was a rapid test processed?',
        choices=YES_NO,
        max_length=3)

    result_date = models.DateField(
        validators=[
            date_not_before_study_start,
            date_not_future, ],
        verbose_name='Date of rapid test',
        blank=True,
        null=True)

    result = models.CharField(
        verbose_name='What is the rapid test result?',
        choices=POS_NEG_IND,
        max_length=15,
        blank=True,
        null=True)

    comments = models.CharField(
        verbose_name='Comment',
        max_length=250,
        blank=True,
        null=True)

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Rapid HIV Testing'
        verbose_name_plural = 'Rapid HIV Testing'
