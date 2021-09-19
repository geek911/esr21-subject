from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import OMANG, FEMALE, MALE, NO, YES
from edc_facility.import_holidays import import_holidays
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy


@tag('rg')
class TestRuleGroups(TestCase):

    def setUp(self):
        import_holidays()

        self.eligibility = mommy.make_recipe(
            'esr21_subject.eligibilityconfirmation')

        self.consent_options = {
            'screening_identifier': self.eligibility.screening_identifier,
            'consent_datetime': get_utcnow(),
            'version': 1,
            'dob': (get_utcnow() - relativedelta(years=45)).date(),
            'first_name': 'TEST ONE',
            'last_name': 'TEST',
            'initials': 'TOT',
            'identity': '123425678',
            'confirm_identity': '123425678',
            'identity_type': OMANG,
            'gender': FEMALE}

        self.subject_consent = mommy.make_recipe(
            'esr21_subject.informedconsent',
            **self.consent_options)

        mommy.make_recipe(
            'esr21_subject.screeningeligibility',
            subject_identifier=self.subject_consent.subject_identifier)

        self.subject_identifier = self.subject_consent.subject_identifier

        self.subject_visit = mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(
                visit_code='1000',
                subject_identifier=self.subject_consent.subject_identifier),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

    @tag('rg1')
    def test_pregnancy_form_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='esr21_subject.pregnancystatus',
                subject_identifier=self.subject_identifier,
                visit_code='1000',
                visit_code_sequence='0').entry_status, REQUIRED)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='esr21_subject.pregnancytest',
                subject_identifier=self.subject_identifier,
                visit_code='1000',
                visit_code_sequence='0').entry_status, NOT_REQUIRED)

    def test_pregnancy_status_form_not_required(self):

        eligibility = mommy.make_recipe(
            'esr21_subject.eligibilityconfirmation')

        consent_options = {
            'screening_identifier': eligibility.screening_identifier,
            'consent_datetime': get_utcnow(),
            'version': 1,
            'dob': (get_utcnow() - relativedelta(years=45)).date(),
            'first_name': 'JOHN',
            'last_name': 'DOE',
            'initials': 'JD',
            'identity': '123415678',
            'confirm_identity': '123415678',
            'identity_type': OMANG,
            'gender': MALE}

        subject_consent = mommy.make_recipe(
            'esr21_subject.informedconsent',
            **consent_options)

        mommy.make_recipe(
            'esr21_subject.screeningeligibility',
            subject_identifier=subject_consent.subject_identifier)

        mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(
                visit_code='1000',
                subject_identifier=subject_consent.subject_identifier),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='esr21_subject.pregnancystatus',
                subject_identifier=subject_consent.subject_identifier,
                visit_code='1000',
                visit_code_sequence='0').entry_status, NOT_REQUIRED)

    def test_pregnancy_test_not_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='esr21_subject.pregnancytest',
                subject_identifier=self.subject_identifier,
                visit_code='1000',
                visit_code_sequence='0').entry_status, NOT_REQUIRED)

    @tag('pt1')
    def test_pregnancy_test_required(self):
        self.consent_options['dob'] = (get_utcnow() - relativedelta(years=55)).date()
        self.consent_options['identity'] = '111125678'
        self.consent_options['confirm_identity'] = '111125678'

        subject_consent = mommy.make_recipe(
            'esr21_subject.informedconsent',
            **self.consent_options)

        mommy.make_recipe(
            'esr21_subject.screeningeligibility',
            subject_identifier=subject_consent.subject_identifier)

        subject_visit = mommy.make_recipe(
            'esr21_subject.subjectvisit',
            appointment=Appointment.objects.get(
                visit_code='1000',
                subject_identifier=subject_consent.subject_identifier),
            report_datetime=get_utcnow(),
            reason=SCHEDULED)

        mommy.make_recipe(
            'esr21_subject.pregnancystatus',
            subject_visit=subject_visit,
            post_menopausal=NO,
            surgically_sterilized=NO)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='esr21_subject.pregnancytest',
                subject_identifier=subject_consent.subject_identifier,
                visit_code='1000',
                visit_code_sequence='0').entry_status, REQUIRED)
