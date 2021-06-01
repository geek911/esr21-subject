from django.db import models

from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin


class MedicalHistory(CrfModelMixin):

    relevant_history = models.CharField(
        verbose_name='Does the subject have any relevant Medical History?',
        max_length=10,
        choices=YES_NO, )

    diagnosis = models.CharField(
        verbose_name='Medical History Diagnosis',
        max_length=32, )

    start_date = models.DateField(
        verbose_name='Start Date (DD MMM YYYY)', )

    end_date = models.DateField(
        verbose_name='End Date (DD MMM YYYY)', )

    ongoing = models.CharField(
        verbose_name='Ongoing',
        max_length=32, )

    on_medication = models.CharField(
        verbose_name='Is the subject taking medication related to '
                     'this condition?',
        max_length=10,
        choices=YES_NO,
        help_text='(If Yes,please record on CM form)')

    cm_log_line = models.CharField(
        max_length=200,
        verbose_name='CM log line')

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'Medical History'
        verbose_name_plural = 'Medical History'
