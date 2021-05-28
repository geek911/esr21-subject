MIN_AGE_OF_CONSENT = 40
MAX_AGE_OF_CONSENT = 60


class Eligibility:

    def __init__(self, age_in_years=None, **kwargs):
        """ checks if participant is eligible otherwise
            error message is the reason for eligibility test failed."""
        self.error_message = []
        self.age_in_years = age_in_years
        if self.age_in_years < MIN_AGE_OF_CONSENT:
            self.error_message.append(
                'Participant is under {}'.format(MIN_AGE_OF_CONSENT))
        if self.age_in_years > MAX_AGE_OF_CONSENT:
            self.error_message.append(
                'Participant is too old (>{})'.format(MAX_AGE_OF_CONSENT))
        self.is_eligible = False if self.error_message else True

    def __str__(self):
        return "Screened, age ({})".format(self.age_in_years)
