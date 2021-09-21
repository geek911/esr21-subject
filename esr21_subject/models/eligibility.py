from edc_constants.constants import YES
MIN_AGE_OF_CONSENT = 40


class Eligibility:

    def __init__(self, age_in_years=None, received_vaccines=None, any_vaccine_receipt=None,
                ** kwargs):
        """ checks if participant is eligible otherwise
            error message is the reason for eligibility test failed."""
        self.error_message = []
        self.age_in_years = age_in_years
        self.received_vaccines = received_vaccines
        self.any_vaccine_receipt = any_vaccine_receipt

        if self.age_in_years < MIN_AGE_OF_CONSENT:
            self.error_message.append(
                'Participant is under {}'.format(MIN_AGE_OF_CONSENT))
        if self.received_vaccines == YES:
            self.error_message.append(
                'Participant received vaccines other than licensed influenza vaccines')
        if self.any_vaccine_receipt == YES:
            self.error_message.append(
                'Participant has a planned receipt of any vaccines')
        self.is_eligible = False if self.error_message else True

    def __str__(self):
        return "Screened, age ({})".format(self.age_in_years)
