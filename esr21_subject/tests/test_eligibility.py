from django.test import TestCase, tag
from edc_constants.constants import NO, YES

from ..models.eligibility import Eligibility


@tag('eligibility')
class TestEligibility(TestCase):

    """
    Participant age >= 40 and <= 60 is eligible else ineligible
    """

    @tag('valid_age_eligibility')
    def test_valid_participant_eligibility(self):
        """Participant age > 18 are eligible"""
        eligiblity = Eligibility(age_in_years=40)
        self.assertTrue(eligiblity.is_eligible)

    @tag('age_ineligibility')
    def test_under_age_participant_ineligibility(self):
        """Participant age < 18 are ineligible"""
        eligiblity = Eligibility(age_in_years=16)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Participant is under 18', eligiblity.error_message)

    @tag('test_received_receipt_any_vaccines_ineligibility')
    def test_received_receipt_any_vaccines_ineligibility(self):
        eligiblity = Eligibility(age_in_years=41, received_vaccines=NO,
                                 any_vaccine_receipt=YES)
        self.assertFalse(eligiblity.is_eligible)

    @tag('test_received_receipt_any_vaccines_eligibility')
    def test_received_receipt_any_vaccines_eligibility(self):
        eligiblity = Eligibility(age_in_years=41, received_vaccines=NO,
                                 any_vaccine_receipt=NO)
        self.assertTrue(eligiblity.is_eligible)
