from django.db import models

from .model_mixins import CrfModelMixin
from ..choices import AGREE


class Covid19PreventiveBehaviors(CrfModelMixin):

    people_sneezing = models.CharField(
        verbose_name='It really bothers me when people sneeze '
                     'without covering their mouths',
        max_length=20,
        choices=AGREE,)

    avoid_touching = models.CharField(
        verbose_name='I avoid touching door handles and staircase railing at '
                     'public locations',
        max_length=20,
        choices=AGREE, )

    dislike_face_mask = models.CharField(
        verbose_name='I dislike wearing face mask because of the way it '
                     'looks and/or feels',
        max_length=20,
        choices=AGREE, )

    temperature = models.CharField(
        verbose_name='I want peoples temperature to be taken before they '
                     'enter public places',
        max_length=20,
        choices=AGREE, )

    crowded_places = models.CharField(
        verbose_name='I dont mind going to very crowded places',
        max_length=20,
        choices=AGREE, )

    self_isolate = models.CharField(
        verbose_name='I would self-isolate myself at home if needed',
        max_length=20,
        choices=AGREE, )

    use_hand_sanitizer = models.CharField(
        verbose_name='I frequently use hand sanitizer and/or wash my hands '
                     'after shaking someones hand',
        max_length=20,
        choices=AGREE, )

    avoid_public_places = models.CharField(
        verbose_name='I avoid going to public places',
        max_length=20,
        choices=AGREE, )

    class Meta(CrfModelMixin.Meta):
        app_label = 'esr21_subject'
        verbose_name = 'COVID Preventive Behaviors'
        verbose_name_plural = 'COVID Preventive Behaviors'
