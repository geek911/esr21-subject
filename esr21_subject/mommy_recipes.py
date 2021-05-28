from .models import EligibilityConfirmation, InformedConsent
from edc_constants.constants import YES
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
    national_identity=seq('123427675'),
    is_literate=YES,
    reviewed_consent=YES,
    answered_all_questions=YES,
    asked_questions=YES,
    have_verified=YES,
    copy_of_consent=YES)
