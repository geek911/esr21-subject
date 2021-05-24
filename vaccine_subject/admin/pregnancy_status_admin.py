from django.contrib import admin
from django.db import models
from django.forms import Textarea

from edc_model_admin import audit_fieldset_tuple
from ..forms import AdverseEventsForm
from ..models import PregnancyStatus


@admin.register(PregnancyStatus)
class PregnancyStatusAdmin(admin.ModelAdmin):
    form = AdverseEventsForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
            )
        }),
        ('Maternal Medical History', {
            'fields': (
                'chronic_condition',
                'who_diagnosed',
                'who',
                'participant_chronic',
                'participant_chronic_other',
                'participant_medications',
                'participant_medications_other',
                'sero_positive',
                'if_sero_positive',
                'hiv_infected',
                'know_hiv_status',
                'cd4_known',
                'lowest_known_cd4',
                'date_cd4_test',
                'is_estimated',
            )

        }),
        ('Maternal Obstetric History', {
            'fields': (
                'prev_pregnancies',
                'pregs_24wks_or_more',
                'lost_before_24wks',
                'lost_after_24wks',
                'live_children',
                'children_died_b4_5yrs',
                'children_deliv_before_37wks',
                'children_deliv_aftr_37wks',
                'comments',
            )
        }),

        audit_fieldset_tuple
    )

    radio_fields = {'chronic_condition': admin.VERTICAL,
                    'who_diagnosed': admin.VERTICAL,
                    'sero_positive': admin.VERTICAL,
                    'hiv_infected': admin.VERTICAL,
                    'know_hiv_status': admin.VERTICAL,
                    'cd4_known': admin.VERTICAL,
                    'is_estimated': admin.VERTICAL,
                    }
    filter_horizontal = ('participant_chronic', 'who',
                         'participant_medications',)
