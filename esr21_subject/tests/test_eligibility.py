from django.test import TestCase, tag

from ..models.eligibility import Eligibility


class TestEligibility(TestCase):

    """
    Participant age >= 40 and <= 60 is eligible else ineligible
    """
    @tag('valid_age_eligibility')
    def test_valid_participant_eligibility(self):
        eligiblity = Eligibility(age_in_years=40)
        self.assertTrue(eligiblity.is_eligible)

    """Participant age < 40 are in eligible"""
    @tag('under_age_eligibility')
    def test_under_age_participant_ineligibility(self):
        eligiblity = Eligibility(age_in_years=31)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Participant is under 40', eligiblity.error_message)

    """Participant age > 60 are in eligible"""
    @tag('invalid_over_age_eligibility')
    def test_over_age_participant_ineligibility(self):
        eligiblity = Eligibility(age_in_years=61)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Participant is too old (>60)', eligiblity.error_message)
