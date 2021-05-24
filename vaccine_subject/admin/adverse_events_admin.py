from django.contrib import admin
from django.db import models
from django.forms import Textarea

from edc_model_admin import audit_fieldset_tuple
from ..forms import AdverseEventsForm
from ..models import AdverseEvents


@admin.register(AdverseEvents)
class AdverseEventsAdmin(admin.ModelAdmin):
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
                'report_date_time',
            )
        }),
        ('Adverse Event', {
            'fields': (
                'event_details',
                'start_date',
                'status',
                'resolution_date',
                'ae_grade',
                'rating',
                'action_taken',
                'study_withdrawal',
                'outcome',
            )

        }),
        ('Serious Adverse Event (SAE)', {
            'fields': (
                'date_met_criteria',
                'date_aware_of',
                'reasons_serious',
                'was_hospitalized',
                'date_hospitalized',
                'participant_discharged',
                'date_discharged',
                'probable_death_cause',
                'date_of_death',
                'performed_autopsy',
            )
        }),

        audit_fieldset_tuple
    )

    radio_fields = {'status': admin.VERTICAL,
                    'ae_grade': admin.VERTICAL,
                    'rating': admin.VERTICAL,
                    'study_withdrawal': admin.VERTICAL,
                    'was_hospitalized': admin.VERTICAL,
                    'participant_discharged': admin.VERTICAL,
                    'performed_autopsy': admin.VERTICAL,
                    }
