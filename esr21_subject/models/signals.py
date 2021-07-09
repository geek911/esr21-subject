from django.apps import apps as django_apps
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .informed_consent import InformedConsent
from .covid19_symptomatic_infections import Covid19SymptomaticInfections


@receiver(post_save, weak=False, sender=InformedConsent,
          dispatch_uid='informed_consent_on_post_save')
def informed_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """ Put participant on schedule post consent """
    if not raw:
        if created:
            instance.registration_update_or_create()

        onschedule_model = 'esr21_subject.onschedule'
        put_on_schedule('esr21_enrol_schedule', instance=instance,
                        onschedule_model=onschedule_model)

        put_on_schedule('esr21_fu_schedule', instance=instance,
                        onschedule_model=onschedule_model)


@receiver(post_save, weak=False, sender=Covid19SymptomaticInfections,
          dispatch_uid='informed_consent_on_post_save')
def covid19_symptomatic_infections_on_post_save(sender, instance, raw, created, **kwargs):

    if not raw and instance.infection_status == 'seropositive':

        onschedule_model = 'esr21_subject.onscheduleill'

        put_on_schedule('esr21_illness_schedule', instance=instance,
                        onschedule_model=onschedule_model)


def put_on_schedule(schedule_name, onschedule_model, instance=None):

    if instance:

        _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
            onschedule_model=onschedule_model, name=schedule_name)

        onschedule_model_cls = django_apps.get_model(onschedule_model)

        try:
            onschedule_model_cls.objects.get(
                subject_identifier=instance.subject_identifier,
                schedule_name=schedule_name)
        except onschedule_model_cls.DoesNotExist:
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.consent_datetime,
                schedule_name=schedule_name)
        else:
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier,
                schedule_name=schedule_name)
