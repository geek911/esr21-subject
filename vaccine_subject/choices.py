from django.utils.translation import ugettext_lazy as _
from edc_constants.constants import FAILED_ELIGIBILITY, YES, NO, OTHER, \
    ON_STUDY, OFF_STUDY, DONT_KNOW, MALE, FEMALE
from edc_constants.constants import NEG, POS, IND


LANGUAGE = (
    ('Setswana', 'Setswana'),
    ('Setswana', 'English'),
)
#
IDENTITY_TYPE = (
    ('country_id', 'Country ID number'),
    ('country_id_rcpt', 'Country ID receipt'),
    ('passport', 'Passport'),
    (OTHER, 'Other'),
)

STATUS = (
    ('Resolved', 'Resolved'),
    ('ongoing', 'Ongoing'),
)
AE_GRADE = (
    ('mild_AE', 'Mild AE'),
    ('moderate_AE', 'Moderate AE'),
    ('severe_AE', 'Severe AE'),
    ('life-threatening', 'Life-threatening or Disabling AE'),
    ('Death_related', 'Death related to AE'),
)
AGREE = (
    ('strongly_disagree', 'Strongly disagree'),
    ('undecided', 'Undecided'),
    ('strongly_agree', 'Strongly agree'),
)
