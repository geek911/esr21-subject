from django.test import TestCase, tag
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy

from ..models import OnSchedule


@tag('vs')
class TestVisitScheduleSetup(TestCase):

    databases = '__all__'

    def setUp(self):
        import_holidays()

    def test_consented_onschedule(self):
        """Assert that a pregnant woman is put on cohort a schedule.
        """

        mommy.make_recipe(
            'esr21_subject.eligibilityconfirmation',)

        informed_consent = mommy.make_recipe(
            'esr21_subject.informedconsent',)

        self.assertEqual(OnSchedule.objects.filter(
            subject_identifier=informed_consent.national_identity,
            schedule_name='esr21_enrol_schedule').count(), 1)

        self.assertEqual(OnSchedule.objects.filter(
            subject_identifier=informed_consent.national_identity,
            schedule_name='esr21_fu_schedule').count(), 1)
