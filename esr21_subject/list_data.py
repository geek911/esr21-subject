from edc_constants.constants import OTHER

from edc_list_data import PreloadData

list_data = {
    'esr21_subject.saecriteria': [
        ('death', 'Death'),
        ('life_threatening', 'Life-threatening'),
        ('hospitalization', 'Initial or prolonged hospitalization'),
        ('birth_defects', 'Congenital anomaly/birth defect'),
        ('incapacity', 'Persistent or significant disability/incapacity'),
        (OTHER, 'Other important medical event'),
    ],
    'esr21_subject.subjectrace': [
        ('american', 'American Indian or Alaska Native'),
        ('asian', 'Asian'),
        ('african', 'Black or African American'),
        ('pacific_islander', 'Native Hawaiian or Other Pacific Islanders'),
        ('white', 'White'),
    ],
    'esr21_subject.covidsymptoms': [
        ('cough', 'Cough'),
        ('fever', 'Fever'),
        ('myalgia', 'Myalgia'),
        ('diarrhea', 'Diarrhea'),
        ('dyspnea', 'Dyspnea'),
        ('fatigue_or-Malaise', 'Fatigue or Malaise'),
        ('difficulty_in_breathing', 'Difficulty in breathing'),
        ('loss_of_smell', 'Loss of Smell'),
        ('loss_of_taste', 'Loss of Taste'),
        ('chills', 'Chills'),
        ('body_aches', 'Body aches'),
        ('headache', 'Headache'),
        ('sore_throat', 'Sore Throat'),
        ('vomiting', 'Vomiting'),
        ('congestion', 'Congestion'),
        ('runny_nose', 'Runny Nose'),
        ('nausea', 'Nausea'),
        ('hospitalization_outcome', 'Hospitalization Outcome'),
    ],
    'esr21_subject.symptomaticinfections': [
        ('dry_cough', 'Dry Cough'),
        ('fever', 'Fever'),
        ('fatigue', 'Fatigue'),
        ('loss_of_smell', 'Loss of Smell'),
        ('loss_of_taste', 'Loss of Taste'),
        ('body_aches', 'Body aches'),
        ('headache', 'Headache'),
        ('shortness_of_breath', 'Shortness of breath'),
    ],
}

preload_data = PreloadData(
    list_data=list_data)
