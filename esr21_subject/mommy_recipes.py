from .models import EligibilityConfirmation, InformedConsent, SubjectVisit
from .models import Covid19SymptomaticInfections, OffSchedule, PregnancyStatus
from .models import RapidHIVTesting, OffScheduleIll, ScreeningEligibility
from edc_base.utils import get_utcnow
from edc_constants.constants import ALIVE, YES, ON_STUDY, PARTICIPANT
from edc_visit_tracking.constants import SCHEDULED
from faker import Faker
from model_mommy.recipe import Recipe, seq

fake = Faker()

eligibilityconfirmation = Recipe(
    EligibilityConfirmation,
    age_in_years=40)

informedconsent = Recipe(
    InformedConsent,
    first_name=fake.first_name,
    last_name=fake.last_name,
    identity=seq('123427675'),
    confirm_identity=seq('123427675'),
    is_literate=YES,
    consent_to_participate=YES,
    optional_sample_collection=YES)

screeningeligibility = Recipe(
    ScreeningEligibility)

subjectvisit = Recipe(
    SubjectVisit,
    report_datetime=get_utcnow(),
    reason=SCHEDULED,
    study_status=ON_STUDY,
    survival_status=ALIVE,
    info_source=PARTICIPANT)

rapidhivtesting = Recipe(
    RapidHIVTesting,
    )

pregnancystatus = Recipe(
    PregnancyStatus,
    )

covid19symptomaticinfections = Recipe(
    Covid19SymptomaticInfections)

offschedule = Recipe(
    OffSchedule)

offscheduleill = Recipe(
    OffScheduleIll)
