from django.utils.translation import ugettext_lazy as _

from edc_constants.constants import (OTHER, NOT_APPLICABLE, UNKNOWN, POS, NEG,
                                     IND, MALE, FEMALE)
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
from edc_visit_tracking.constants import MISSED_VISIT, COMPLETED_PROTOCOL_VISIT

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

AESI_CATEGORY = (
    ('generalized_convulsion', 'Generalized convulsion'),
    ('guillain_barre_syndrome', 'Guillain-Barre syndrome'),
    ('acute_disseminated', 'Acute disseminated encephalomyelitis'),
    ('other_neuro_events', 'Other neurologic events'),
    ('thrombotic', 'Thrombotic or thromboembolic or neurovascular events'),
    ('Thrombocytopenia', 'Thrombocytopenia'),
    ('vasculitides', 'Vasculitides'),
    ('anaphylaxis', 'Anaphylaxis'),
    ('vaccine_assoc_resp_disease',
     'Vaccine-associated enhanced respiratory disease'),
    ('immune_mediated_cond', 'Potential immune-mediated conditions'),
)

AGREE_DISAGREE = (
    ('strongly_disagree', 'Strongly disagree'),
    ('undecided', 'Undecided'),
    ('strongly_agree', 'Strongly agree'),
)

CONTRACEPTIVES = (
    ('iud', 'IUD'),
    ('diaphragm', 'Diaphragm'),
    ('pill', 'Contraceptive pill'),
    ('barrier_method', 'Barrier Method'),
    ('abstention', 'Abstention'),
    (OTHER, 'Other, specify'),
)

EMPLOYMENT_STATUS = (
    ('formal-wage_employment_part_time', 'Formal wage employment (Part-time)'),
    (
        'formal_wage_employment-full_time)',
        'Formal wage employment (full-time)'),
    ('self_employed_full_time)', 'Self employed (full time)'),
    ('self_employed_part_time)', 'Self employed (part time)'),
    ('piece_job', 'Piece job'),
    ('Seasonal_employment', 'Seasonal employment'),
    (OTHER, 'Other (specify)'),)

GENDER_OTHER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
    (OTHER, _('Other')),
)

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

MARITAL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Cohabiting', 'Cohabiting'),
    ('Widowed', 'Widowed'),
    ('Divorced', 'Divorced'),
    (OTHER, 'Other, specify'))

MODE_TRANSPORT = (
    ('public_transport', 'Public Transport'),
    ('private_transport', 'Private Transport')
)

OUTCOME = (
    ('not_resolved', 'Not recovered/ not resolved'),
    ('resolved', 'Recovered / resolved'),
    ('resolved_with_sequelae', 'Recovered / resolved with sequelae'),
    ('resolving', 'Recovering / resolving'),
    ('fatal', 'Fatal'),
    (UNKNOWN, UNKNOWN),
)

POS_NEG_IND = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (IND, 'Indeterminate')
)

PREGNANCY_TEST_TYPE = (
    ('urine_serum', 'Urine/Serum'),
    ('hgg', 'HCG'),
)

REASON_NOT_DRAWN = (
    ('not_collected', 'Not collected'),
    ('not_required', 'Not required at this visit'),
    ('measurement_skipped', 'Measurement skipped at this visit'),
    ('subject_refused', 'Subject refused'),
    ('equipment_malfunction', 'Equipment malfunction'),
    ('staff_unavailable', 'Staff unavailable'),
    ('no_further_information', 'No further information'),
)

ROUTE = (
    ('intramuscular', 'Intramuscular'),
    ('oral', 'Oral'),
)

INFECTION_STATUS = (
    ('seronegative', 'Seronegative'),
    ('seropositive', 'Seropositive'),
)

SETTLEMENT_TYPE = (
    ('urban', 'Urban'),
    ('rural', 'Rural'),
)

STATUS = (
    ('resolved', 'Resolved'),
    ('ongoing', 'Ongoing'),
)

TEMP_UNITS = (
    ('celcius', 'Celcius (ºC)'),
    ('fahrenheit', 'Fahrenheit (ºF)'),
)

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
    (NOT_APPLICABLE, 'Not applicable'),
)

HOSPITALIZATION_REASON = (
    ('', 'COVID-19 related symptoms'),
    (OTHER, 'Other'),
)

HOSPITALIZATION_OUTCOME = (
    ('expired', 'Expired'),
    ('hospice_care', 'Home: Hospice Care'),
    ('self_care', 'Home: Self Care'),
    ('hospice_medical_facility', 'Hospice Medical Facility'),
    ('inpatient_rehabilitation', 'Inpatient Rehabilitation'),
    ('intermediate_care_facility', 'Intermediate Care Facility'),
    ('medical_advice', 'Left Against Medical Advice'),
    ('long_term_care_hospital', 'Long Term Care Hospital'),
    ('nursing_facility', 'Nursing Facility'),
    ('unit_ward_change', 'Unit/Ward Change'),
)

VACCINATION_LOCATION = (
    ('left_deltoid', 'Left deltoid'),
    ('right_deltoid', 'Right deltoid'),
    (OTHER, 'Other, specify'),
)

VISIT_INFO_SOURCE = (
    ('clinic_visit_w_subject', 'Clinic visit with participant'),
    ('other_contact_w_subject',
     'Other contact with participant (i.e telephone call)'),
    ('contact_w_health_worker', 'Contact with health care worker'),
    ('Contact_w_family_design',
     'Contact with family or designated person who can provide information'),
    (OTHER, 'Other,specify'),
)

VISIT_REASON = (
    (SCHEDULED, 'Scheduled visit/contact'),
    (MISSED_VISIT, 'Missed Scheduled visit'),
    (UNSCHEDULED, 'Unscheduled visit/contact'),
    (LOST_VISIT, 'Lost to follow-up (use only when taking subject off study)'),
    (COMPLETED_PROTOCOL_VISIT, 'Subject has completed the study'),
)
