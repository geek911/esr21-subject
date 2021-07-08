from edc_constants.constants import OTHER

from edc_list_data import PreloadData

list_data = {
    'esr21_subject.saecriteria': [
        ('death', 'Death'),
        ('life_threatening', 'Life-threatening'),
        ('hospitalization', 'Initial or prolonged hospitalization'),
        ('incapacity', 'Persistent or significant disability/incapacity'),
        ('birth_defects', 'Congenital anomaly/birth defect'),
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
        ('muscle_aches', 'Muscle aches'),
        ('sore_throat', 'Sore throat'),
        ('chills', 'Chills'),
        ('congestion', 'Congestion'),
        ('runny_nose', 'Runny nose'),
        ('nausea', 'Nausea'),
        ('vomiting', 'Vomiting'),
        ('diarrhoea', 'Diarrhoea'),
        ('difficulty_breathing', 'Difficulty breathing')
    ],

    'esr21_subject.symptoms': [
        ('fever', 'Fever'),
        ('dry_cough', 'Dry Cough'),
        ('fatigue', 'Fatigue'),
        ('loss_of_taste_or_smell', 'Loss of taste or smell'),
        ('headache', 'Headache'),
        ('muscle_or_joint_pain', 'Muscle or joint pain'),
        ('shortness_of_breath', 'Shortness Of Breath'),
        ('difficulty_breathing_or_shortness_of_breath', 'Difficulty breathing or shortness of breath'),
        ('chest_pain_or_pressure', 'Chest pain or pressure'),
        ('loss_of_speech_or_movement', 'Loss of speech or movement'),
        (OTHER, 'Other')
    ],
    'esr21_subject.diseases': [
        ('HIV', 'HIV'),
        ('malignancy', 'malignancy'),
        ('chronic_disease', 'Chronic Disease'),
        ('chronic_obstructive_pulmonary_disease_and_other_chronic_lung_diseases',
         'Chronic obstructive pulmonary disease and other chronic lung diseases'),
        ('hypertension', 'Hypertension'),
        ('coronary_artery_disease', 'Coronary artery disease'),
        ('cardiomyopathy', 'Cardiomyopathy'),
        ('pulmonary_hypertension', 'Pulmonary hypertension'),
        ('obesity', 'Obesity'),
        (OTHER, 'Other')
    ]

}

preload_data = PreloadData(
    list_data=list_data)
