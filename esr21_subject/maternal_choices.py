from edc_constants.choices import YES, NO
from edc_constants.constants import OTHER, UNKNOWN


YES_NO_DNT_DWTA = (
    (YES, YES),
    (NO, NO),
    ('Dont know right now', 'I do not know right now'),
    ('DWTA', 'Don\'t want to answer'))

YES_NO_NO_PARTNER_DWTA = (
    (YES, YES),
    (NO, NO),
    ('no_partner', 'I do not currently have a partner'),
    ('DWTA', 'Don\'t want to answer'))

MARITAL_STATUS = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Cohabiting', 'Cohabiting'),
    ('Widowed', 'Widowed'),
    ('Divorced', 'Divorced'),
    (OTHER, 'Other, specify'),)

ETHNICITY = (
    ('Black African', 'Black African'),
    ('Caucasian', 'Caucasian'),
    ('Asian', 'Asian'),
    (OTHER, 'Other, specify'),)

HIGHEST_EDUCATION = (
    ('None', 'None'),
    ('Primary', 'Primary'),
    ('Junior Secondary', 'Junior Secondary'),
    ('Senior Secondary', 'Senior Secondary'),
    ('Tertiary', 'Tertiary'),)

CURRENT_OCCUPATION = (
    ('Housewife', 'Housewife'),
    ('Salaried (government)', 'Salaried (government)'),
    ('Salaried (private, not including domestic work)',
     'Salaried (private, not including domestic work)'),
    ('Domestic work (paid)', 'Domestic work (paid)'),
    ('Self-employed', 'Self-employed'),
    ('Student', 'Student'),
    ('Unemployed', 'Unemployed'),
    (OTHER, 'Other, specify'),)

MONEY_PROVIDER = (
    ('You', 'You'),
    ('Partner/husband', 'Partner/husband'),
    ('Mother', 'Mother'),
    ('Father', 'Father'),
    ('Sister', 'Sister'),
    ('Brother', 'Brother'),
    ('Aunt', 'Aunt'),
    ('Uncle', 'Uncle'),
    ('Grandmother', 'Grandmother'),
    ('Grandfather', 'Grandfather'),
    ('Mother-in-law or Father-in-law', 'Mother-in-law or Father-in-law'),
    ('Friend', 'Friend'),
    ('Work collegues', 'Work collegues'),
    ('Unsure', 'Unsure'),
    (OTHER, 'Other, specify'),)

MONEY_EARNED = (
    ('None', 'None'),
    ('P1157 per week', 'P1157 per week'),
    ('Unsure', 'Unsure'),
    (OTHER, 'Other, specify'),)

WATER_SOURCE = (
    ('Piped directly into the house', 'Piped directly into the house'),
    ('Tap in the yard', 'Tap in the yard'),
    ('Communal standpipe', 'Communal standpipe'),
    (OTHER, 'Other water source (stream, borehole, rainwater, etc)'),)

COOKING_METHOD = (
    ('Gas or electric stove', 'Gas or electric stove'),
    ('Paraffin stove', 'Paraffin stove'),
    ('Wood-burning stove or open fire', 'Wood-burning stove or open fire'),
    ('No regular means of heating', 'No regular means of heating'),)

TOILET_FACILITY = (
    ('Indoor toilet', 'Indoor toilet'),
    ('Private latrine for your house/compound',
     'Private latrine for your house/compound'),
    ('Shared latrine with other compounds',
     'Shared latrine with other compounds'),
    ('No latrine facilities', 'No latrine facilities'),
    (OTHER, 'Other, specify'),)

HOUSE_TYPE = (
    ('Formal:Tin-roofed, concrete walls',
     'Formal: Tin-roofed, concrete walls'),
    ('Informal: Mud-walled or thatched', 'Informal: Mud-walled or thatched'),
    ('Mixed formal/informal', 'Mixed formal/informal'),
    ('Shack/Mokhukhu', 'Shack/Mokhukhu'),)

KNOW_HIV_STATUS = (
    ('Nobody', 'Nobody'),
    ('1 person', '1 person'),
    ('2-5 people', '2-5 people'),
    ('6-10 people', '6-10 people'),
    ('More than 10 people', 'More than 10 people'),
    ('dont know', 'I do not know'),)

IS_DATE_ESTIMATED = (
    (NO, 'No'),
    ('Yes, estimated the Day', 'Yes, estimated the Day'),
    ('Yes, estimated Month and Day', 'Yes, estimated Month and Day'),
    ('Yes, estimated Year, Month and Day',
     'Yes, estimated Year, Month and Day'),
)
OUTCOME = (
    ('live_birth', 'Live Birth'),
    ('miscarriage', 'Miscarriage'),
    ('abortion', 'Abortion'),
)
CHILDBEARING = (
    ('post-menopausal', 'Post-Menopausal'),
    ('surgically_sterile', 'Surgically Sterile'),
    (OTHER, 'Other, specify'),)

RACE = (
    ('reported', 'Reported'),
    ('not_reported', 'Not Reported'),
    (UNKNOWN, 'Unknown'),)
