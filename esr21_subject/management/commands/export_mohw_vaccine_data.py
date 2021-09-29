import csv

from django.core.management.base import BaseCommand

from ...models import PersonalContactInfo, DemographicsData, InformedConsent, VaccinationDetails
from edc_base.utils import get_utcnow


class Command(BaseCommand):
    help = 'Export vaccine data'

    def handle(self, *args, **kwargs):

        vaccinations = VaccinationDetails.objects.filter(received_dose='Yes')
        exclude_fields = [
            'created', 'modified', 'user_created', 'user_modified',
            'hostname_created', 'hostname_modified', 'revision', 'device_created',
            'device_modified', 'id', 'site_id', 'consent_model',
            'consent_version', 'report_datetime']
        count = 0
        toCSV = []
        for vaccination in vaccinations:
            obj_dict = vaccination.__dict__

            for key in exclude_fields:
                del obj_dict[key]
            consent = InformedConsent.objects.filter(
                subject_identifier=vaccination.subject_visit.subject_identifier).last()
            first_name = consent.first_name
            last_name = consent.last_name
            dob = consent.dob
            country = None
            employment_status = None
            subject_cell = None
            
            identity_number = consent.identity
            identity_type = consent.identity_type
            
            demographics = DemographicsData.objects.filter(
                subject_visit__subject_identifier=vaccination.subject_visit.subject_identifier).last()
            if demographics:
                country = demographics.country
                employment_status = demographics.employment_status
            
            try:
                personal_contact = PersonalContactInfo.objects.get(
                    subject_identifier=vaccination.subject_visit.subject_identifier)
            except PersonalContactInfo.DoesNotExist:
                pass
            else:
                subject_cell = personal_contact.subject_cell
            obj_dict.update(
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                country=country,
                employment_status=employment_status,
                subject_cell=subject_cell,
                identity_number=identity_number,
                identity_type=identity_type
                )
            obj_dict.pop('_state')
            obj_dict.pop('form_as_json')
            obj_dict.pop('subject_visit_id')
            toCSV.append(obj_dict)
            count += 1

        keys = toCSV[0].keys()
        timestamp = get_utcnow().strftime("%m%d%Y%H%M%S")
        with open('vacinations_' + timestamp + '.csv', 'w', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(toCSV)

        self.stdout.write(self.style.SUCCESS(f'Total exported: {count}.'))

