import csv

from django.core.management.base import BaseCommand

from ...models import PersonalContactInfo, DemographicsData, InformedConsent, VaccinationDetails
from edc_base.utils import get_utcnow

class Command(BaseCommand):
    help = 'Export vaccine data'

    def district_check(location):
        switcher = {
            "gaborone": "South East",
            "maun": "Ngamiland",
            "francistown": "North East",
            "phikwe": " Central",
            "serowe": "Central",
        }
        return print(switcher.get(location, "no location"))


    def handle(self, *args, **kwargs):
        vaccinations_tuple = ('received_dose_before', 'vaccination_site',
                              'vaccination_date', 'lot_number', 'expiry_date',
                              'provider_name')
        vaccinations = VaccinationDetails.objects.filter(received_dose='Yes').only(
            *vaccinations_tuple)
        count = 0
        toCSV = []
        columnNames = ['Programinstanceid',	'Firstname', 'Surname',	'Sex', 'Date_of_birth',	'Mobile_number',
        	'ID Number', 'Covid Zone', 'District',
        	'City_Village',	'Plot_Ward', 'Occupation', 'Employer',
            'DOSE1_organisationunitid', 'DOSE1_vaccinesite',
            'Dose1_district', 'DOSE1_date_vaccinated', 'DOSE1_vaccinetype',
            'DOSE2_organisationunitid',	'DOSE2_vaccinesite', 'dose2_district',
            'DOSE2_date_vaccinated', 'DOSE2_vaccinetype']

        newColumnNames = ['Firstname', 'Surname','Sex', 'Date_of_birth', 'Mobile_number',
        	'ID Number', 'Covid Zone', 'District','Address' ,'Occupation', ]  

        for vaccination in vaccinations:
            obj_dict = vaccination.__dict__

            consent = InformedConsent.objects.filter(
                subject_identifier=vaccination.subject_visit.subject_identifier).last()
            first_name = consent.first_name
            last_name = consent.last_name
            dob = consent.dob
            gender = consent.gender
            age = consent.formatted_age_at_consent
            site = consent.site.name
            country = None
            employment_status = None
            employment_status_other = None
            subject_cell = None
            occupation = None

            identity_number = consent.identity

            demographics = DemographicsData.objects.filter(
                subject_visit__subject_identifier=vaccination.subject_visit.subject_identifier).last()
            if demographics:
                country = demographics.country
                employment_status = demographics.employment_status
                employment_status_other = demographics.employment_status_other
                if employment_status_other:
                    occupation = employment_status_other
                else:
                    occupation = employment_status

            try:
                personal_contact = PersonalContactInfo.objects.get(
                    subject_identifier=vaccination.subject_visit.subject_identifier)
            except PersonalContactInfo.DoesNotExist:
                pass
            else:
                subject_cell = personal_contact.subject_cell
                physical_address = personal_contact.physical_address
                location = site[6:]
            obj_dict.update(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                dob=dob,
                subject_cell=subject_cell,
                identity_number=identity_number,
                covidzone="{} {} {}".format("Greater",location,"Zone"),
                district = self.district_check(location.lower()),
                physical_address=physical_address,
                occupation=occupation,
                )
            obj_dict.pop('id')
            obj_dict.pop('_state')
#             obj_dict.pop('form_as_json')
            obj_dict.pop('subject_visit_id')
            toCSV.append(obj_dict)
            count += 1

        # keys = toCSV[0].keys()
        timestamp = get_utcnow().strftime("%m%d%Y%H%M%S")
        with open('vacinations_' + timestamp + '.csv', 'w', newline='')  as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=newColumnNames)
            dict_writer.writeheader()
            dict_writer.writerows(toCSV)

        self.stdout.write(self.style.SUCCESS(f'Total exported: {count}.'))

