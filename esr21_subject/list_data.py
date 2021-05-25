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
}

preload_data = PreloadData(
    list_data=list_data)
