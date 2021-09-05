from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_facility.import_holidays import import_holidays
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy
from ..models import OnSchedule, OnScheduleIll


@tag('vs')
class TestVisitScheduleSetup(TestCase):

    databases = '__all__'

    def setUp(self):
        import_holidays()

    def test_consented_onschedule_subcohort(self):
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

    @tag('vs0')
    def test_consented_onschedule_mainstudy(self):
        """Assert that a participant is put onschedule for main study.
        """
        for i in range(3001):
            mommy.make_recipe(
                'esr21_subject.eligibilityconfirmation',)

            mommy.make_recipe(
                'esr21_subject.informedconsent',
                subject_identifier=f'123-987{i}')

        self.assertEqual(OnSchedule.objects.filter(
            subject_identifier='123-9873000',
            schedule_name='esr21_sub_enrol_schedule').count(), 1)

        self.assertEqual(OnSchedule.objects.filter(
            subject_identifier='123-9873000',
            schedule_name='esr21_sub_fu_schedule').count(), 1)

    @tag('vs1')
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

        visit = mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(visit_code='1007'),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

        mommy.make_recipe(
            'esr21_subject.covid19symptomaticinfections',
            subject_visit=visit,
            symptomatic_experiences=YES)

        self.assertEqual(OnScheduleIll.objects.filter(
            subject_identifier=informed_consent.subject_identifier,
            schedule_name='esr21_illness_schedule').count(), 1)

    @tag('vs2')
    def test_illness_not_onschedule(self):
        """Assert that a participant is not put onschedule for illness visits if
         they test positive for Covid 19 and they are already on an illness schedule.
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

        visit1 = mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(visit_code='1007'),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

        mommy.make_recipe(
            'esr21_subject.covid19symptomaticinfections',
            subject_visit=visit1,
            symptomatic_experiences=YES)

        self.assertEqual(OnScheduleIll.objects.filter(
            subject_identifier=informed_consent.subject_identifier,
            schedule_name='esr21_illness_schedule').count(), 1)

        visit2 = mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(visit_code='1014'),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

        mommy.make_recipe(
            'esr21_subject.covid19symptomaticinfections',
            subject_visit=visit2,
            symptomatic_experiences=YES)

        self.assertEqual(OnScheduleIll.objects.filter(
            subject_identifier=informed_consent.subject_identifier,
            schedule_name='esr21_illness1_schedule').count(), 0)

    @tag('vs3')
    def test_illness2_onschedule(self):
        """Assert that a participant is put onschedule for second illness visits if
         they test positive for Covid 19 for the second time.
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

        visit1 = mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(visit_code='1007'),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

        mommy.make_recipe(
            'esr21_subject.covid19symptomaticinfections',
            subject_visit=visit1,
            symptomatic_experiences=YES)

        self.assertEqual(OnScheduleIll.objects.filter(
            subject_identifier=informed_consent.subject_identifier,
            schedule_name='esr21_illness_schedule').count(), 1)

        mommy.make_recipe(
            'esr21_subject.offschedule',
            schedule_name='esr21_illness_schedule',
            consent_version='1',
            subject_identifier=informed_consent.subject_identifier)

        visit2 = mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(visit_code='1014'),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

        mommy.make_recipe(
            'esr21_subject.covid19symptomaticinfections',
            subject_visit=visit2,
            symptomatic_experiences=YES)

        self.assertEqual(OnScheduleIll.objects.filter(
            subject_identifier=informed_consent.subject_identifier,
            schedule_name='esr21_illness2_schedule').count(), 1)
