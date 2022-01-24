import csv
from operator import index

from django.core.management.base import BaseCommand
from edc_base.utils import get_utcnow

import pandas as pd

from ...models import PersonalContactInfo, DemographicsData, InformedConsent, VaccinationDetails


class Command(BaseCommand):

    help = 'Export vaccine data'

    def district_check(self, location):
        location = location.lower()
        switcher = {
            "gaborone": "South East",
            "maun": "Ngamiland",
            "francistown": "North East",
            "phikwe": " Central",
            "serowe": "Central",
        }
        return switcher.get(location, "no location")

    def handle(self, *args, **kwargs):

        vaccinations_tuple = ('received_dose_before', 'vaccination_site',
                              'vaccination_date',)
        vaccinations = VaccinationDetails.objects.filter(received_dose='Yes').only(
            *vaccinations_tuple)
        count = 0
        toCSV = []
        for vaccination in vaccinations:
            obj_dict = vaccination.__dict__

            consent = InformedConsent.objects.filter(
                subject_identifier=vaccination.subject_visit.subject_identifier).last()
            first_name = consent.first_name
            last_name = consent.last_name
            dob = consent.dob
            gender = consent.get_gender_display()
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
                employment_status = demographics.get_employment_status_display()
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
                district = self.district_check(location)
            obj_dict.update(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                dob=dob,
                subject_cell=subject_cell,
                identity_number=identity_number,
                covidzone=f"Greater {location} Zone",
                district=district,
                physical_address=physical_address,
                occupation=occupation,
                dose_type="Astra-Zeneca",
                )
            obj_dict.pop('id')
            obj_dict.pop('_state')
#             obj_dict.pop('form_as_json')
            obj_dict.pop('subject_visit_id')
            toCSV.append(obj_dict)
            count += 1

        df = pd.DataFrame(toCSV)
        df_mask = df.copy()
        df_mask2 = df_mask.rename(
            columns={'received_dose_before': 'Received Dose', 'dose_type': 'Dose Vaccine Type',
                     'vaccination_site': 'Vaccination Site',
                     'vaccination_date': 'Date Vaccinated', 'first_name': 'Firstname',
                     'last_name': 'Surname', 'gender': 'Sex', 'dob': 'Date of Birth',
                     'subject_cell': 'Mobile Number', 'identity_number': 'Identity Number',
                     'covidzone': 'Covid Zone', 'district': 'District',
                     'physical_address': 'Address', 'occupation': 'Occupation', })

        timestamp = get_utcnow().strftime("%m%d%Y%H%M%S")
        df_mask2.to_csv('~/source/vaccinations_' + timestamp + '.csv', index=False)
