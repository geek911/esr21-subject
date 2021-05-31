from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .modeladmin_mixins import CrfModelAdminMixin
from ..forms import PregnancyStatusForm
from ..models import PregnancyStatus
from ..admin_site import esr21_subject_admin


@admin.register(PregnancyStatus, site=esr21_subject_admin)
class PregnancyStatusAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PregnancyStatusForm

    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 500,
                   'cols': 70,
                   'style': 'height: 7em;'})},
    }

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'report_datetime',
                'start_date_menstrual_period',
                'expected_delivery',
                'using_contraceptives',
                'birth_defects',
                'if_yes',
            )
        }),
        ('Pregnancy History', {
            'fields': (
                'number_prev_pregnancies',
                'number_normal_pregnancies',
                'number_miscarriages',
                'risk_factor',
                'family_history',
            )

        }),
    )

    radio_fields = {'using_contraceptives': admin.VERTICAL,
                    'birth_defects': admin.VERTICAL, }
