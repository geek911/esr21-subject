from edc_constants.constants import OTHER, NOT_APPLICABLE, UNKNOWN


ACTION_TAKEN = (
    ('dose_not_changed', 'Dose not changed'),
    ('drug_withdrawal', 'Drug withdrawal'),
    (NOT_APPLICABLE, NOT_APPLICABLE),
    (UNKNOWN, UNKNOWN),
)

AE_GRADE = (
    ('mild', 'Mild (Grade 1)'),
    ('moderate', 'Moderate (Grade 2)'),
    ('severe', 'Severe (Grade 3)'),
    ('life_threatening', 'Life-threatening (Grade 4)'),
    ('fatal', 'Fatal (Grade 5)'),
)
AGREE = (
    ('strongly_disagree', 'Strongly disagree'),
    ('undecided', 'Undecided'),
    ('strongly_agree', 'Strongly agree'),)

HOSPITALIZATION_STATUS = (
    ('er', 'ER'),
    ('regular_ward', 'Regular Ward'),
    ('icu_hdu', 'ICU/HDU'),
)

IDENTITY_TYPE = (
    ('country_id', 'Country ID number'),
    ('country_id_rcpt', 'Country ID receipt'),
    ('passport', 'Passport'),
    (OTHER, 'Other'),
)

LANGUAGE = (
    ('setswana', 'Setswana'),
    ('setswana', 'English'),
)

OUTCOME = (
    ('not_resolved', 'Not recovered/ not resolved'),
    ('resolved', 'Recovered / resolved'),
    ('resolved_with_sequelae', 'Recovered / resolved with sequelae'),
    ('resolving', 'Recovering / resolving'),
    ('fatal', 'Fatal'),
    (UNKNOWN, UNKNOWN),
)

ROUTE = (
    ('intramuscular', 'Intramuscular'),
    ('oral', 'Oral'),
)

STATUS = (
    ('resolved', 'Resolved'),
    ('ongoing', 'Ongoing'),)

TREATMENT_RELATIONSHIP = (
    ('related', 'Related'),
    ('not_related', 'Not Related'),
)

REASON = (
    ('not_collected', 'Not collected'),
    ('not_required', 'Not required at this visit'),
    ('measurement_skipped', 'Measurement skipped at this visit'),
    ('subject_refused', 'Subject refused'),
    ('equipment_malfunction', 'Equipment malfunction'),
    ('staff_unavailable', 'Staff unavailable'),
    ('no_information', 'No further information'),
)

VACCINATION_LOCATION = (
    ('left_deltoid', 'Left deltoid'),
    ('right_deltoid', 'Right deltoid'),
    (OTHER, 'Other, specify'),
)
