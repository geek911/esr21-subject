from edc_constants.constants import NO, YES


class SecondEligibility:
    def __init__(self,
                 substance_hypersensitivity=None,
                 pregnancy_status=None,
                 thrombosis_or_thrombocytopenia=None,
                 guillain_barre_syndrome=None,
                 suspected_immuno_condition=None,
                 clinical_bleeding=None,
                 covid_symptoms=None,
                 comorbidities=None,
                 symptoms_other=None,
                 comorbidities_other=None,
                 childbearing_potential=None,
                 birth_control=None,
                 birthcontrol_agreement=None,
                 symptomatic_infections=None,
                 symptomatic_infections_other=None,
                 symptomatic_infections_experiences=None,
                 **kwargs):
        """ checks if participant is eligible otherwise
            error message is the reason for eligibility test failed."""
        self.error_message = []

        self.substance_hypersensitivity = substance_hypersensitivity
        self.pregnancy_status = pregnancy_status
        self.thrombosis_or_thrombocytopenia = thrombosis_or_thrombocytopenia
        self.guillain_barre_syndrome = guillain_barre_syndrome
        self.suspected_immuno_condition = suspected_immuno_condition
        self.clinical_bleeding = clinical_bleeding
        self.covid_symptoms = covid_symptoms
        self.comorbidities = comorbidities
        self.symptoms_other = symptoms_other
        self.comorbidities_other = comorbidities_other
        self.childbearing_potential = childbearing_potential
        self.birth_control = birth_control
        self.birthcontrol_agreement = birthcontrol_agreement
        self.symptomatic_infections_experiences = symptomatic_infections_experiences
        self.symptomatic_infections = symptomatic_infections
        self.symptomatic_infections_other = symptomatic_infections_other

        if self.substance_hypersensitivity == YES:
            self.error_message.append(
                'Participant is hypersensitive to the active substance or to any of the '
                'excipients')
        if self.pregnancy_status == YES:
            self.error_message.append(
                'Participant is either pregnant or nursing or planning to get pregnant in the next '
                '3 months')
        if self.thrombosis_or_thrombocytopenia == YES:
            self.error_message.append(
                'Participant has a risk factors for or a reported history of '
                'thrombosis and/or thrombocytopenia')

        if self.guillain_barre_syndrome == YES:
            self.error_message.append(
                'Participant has a history of Guillain-Barré syndrome')

        if self.suspected_immuno_condition == YES:
            self.error_message.append(
                'Participant has a confirmed or suspected immunosuppressive or immunodeficient state')

        if self.clinical_bleeding == YES:
            self.error_message.append(
                'Participant has experienced clinically significant bleeding, or prior history '
                'of significant bleeding or bruising following intramuscular injections '
                'or venepuncture')

        if self.covid_symptoms:
            self.error_message.append(
                'Participant has experienced covid symptoms')

        if self.symptoms_other:
            self.error_message.append(
                'Participant has experienced other covid symptoms')

        if self.comorbidities:
            self.error_message.append(
                'Participant has comorbidities')

        if self.comorbidities_other:
            self.error_message.append(
                'Participant has other comorbidities')

        if self.symptomatic_infections_experiences == YES:
            self.error_message.append(
                'Participant has experiences symptomatic infections'
            )

        if self.symptomatic_infections:
            self.error_message.append(
                'Participant has symptomatic infections'
            )
        if self.symptomatic_infections_other:
            self.error_message.append(
                'Participant has other symptomatic infections'
            )

        if self.childbearing_potential == YES:
            if self.birth_control == NO:
                self.error_message.append(
                    'Participant is child bearing potential and not using highly-effective forms of birth control for '
                    '28 days prior to Day 0')
            elif self.birth_control == YES:
                if birthcontrol_agreement == NO:
                    self.error_message.append(
                        'Participant is child bearing potential and disagree to continue using a highly effective '
                        'form of birth control for 60 days after your last dose (injection) of the vaccine?')

        self.is_eligible = False if self.error_message else True
