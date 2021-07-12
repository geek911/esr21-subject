from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_facility.import_holidays import import_holidays
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy
from ..models import OnSchedule


@tag('vs')
class TestVisitScheduleSetup(TestCase):

    databases = '__all__'

    def setUp(self):
        import_holidays()

    def test_consented_onschedule(self):
        """Assert that a participant is put onschedule for main study.
        """

        mommy.make_recipe(
            'esr21_subject.eligibilityconfirmation',)

        informed_consent = mommy.make_recipe(
            'esr21_subject.informedconsent',
            subject_identifier='123-9876')

        self.assertEqual(OnSchedule.objects.filter(
            subject_identifier=informed_consent.subject_identifier,
            schedule_name='esr21_sub_enrol_schedule').count(), 1)

        self.assertEqual(OnSchedule.objects.filter(
            subject_identifier=informed_consent.subject_identifier,
            schedule_name='esr21_sub_fu_schedule').count(), 1)

    def test_illness_onschedule(self):
        """Assert that a participant is put onschedule for illness visits if
         they test positive for Covid 19.
        """

        mommy.make_recipe(
            'esr21_subject.eligibilityconfirmation',)

        informed_consent = mommy.make_recipe(
            'esr21_subject.informedconsent',
            subject_identifier='123-9877')

        mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(visit_code='1000'),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

        mommy.make_recipe(
            'esr21_subject.covid19_symptomatic_infections',
            infection_status='seropositive',)

        self.assertEqual(OnSchedule.objects.filter(
            subject_identifier=informed_consent.subject_identifier,
            schedule_name='esr21_enrol_schedule').count(), 1)
