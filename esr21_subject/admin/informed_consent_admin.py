from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple
from ..forms import InformedConsentForm
from ..models import InformedConsent
from ..admin_site import esr21_subject_admin


@admin.register(InformedConsent, site=esr21_subject_admin)
class InformedConsentAdmin(admin.ModelAdmin):
    form = InformedConsentForm

    fieldsets = (
        (None, {
            'fields': ('consent_datetime',
                       'first_name',
                       'last_name',
                       'language',
                       'is_literate',
                       'witness_fname',
                       'witness_lname',
                       'date_of_birth',
                       'is_estimated',
                       'national_identity',
                       'identity_type',)
        }),
        ('Review Questions', {
            'fields': (
                'reviewed_consent',
                'answered_all_questions',
                'asked_questions',
                'have_verified',
                'copy_of_consent',
            )
        }),

        audit_fieldset_tuple
    )

    radio_fields = {'language': admin.VERTICAL,
                    'is_literate': admin.VERTICAL,
                    'gender': admin.VERTICAL,
                    'identity_type': admin.VERTICAL,
                    'reviewed_consent': admin.VERTICAL,
                    'answered_all_questions': admin.VERTICAL,
                    'asked_questions': admin.VERTICAL,
                    'have_verified': admin.VERTICAL,
                    'copy_of_consent': admin.VERTICAL,
                    'is_estimated': admin.VERTICAL,
                    }
