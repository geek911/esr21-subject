from edc_action_item import site_action_items
from edc_locator.action_items import SubjectLocatorAction as BaseSubjectLocatorAction

CONTACT_INFORMATION_ACTION = 'submit-personal-contact-information'


class PesronalContactInformationAction(BaseSubjectLocatorAction):
    name = CONTACT_INFORMATION_ACTION
    display_name = 'Submit Personal Contact Information'
    reference_model = 'esr21_subject.subjectlocator'
    admin_site_name = 'esr21_subject_admin'


site_action_items.register(PesronalContactInformationAction)
