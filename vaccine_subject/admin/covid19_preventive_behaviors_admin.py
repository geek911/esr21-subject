from django.contrib import admin

from edc_model_admin import ModelAdminBasicMixin
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..forms import Covid19PreventiveBehaviorsForm
from ..models import Covid19PreventiveBehaviors


@admin.register(Covid19PreventiveBehaviors)
class Covid19PreventiveBehaviorsAdmin(ModelAdminBasicMixin,
                                      SimpleHistoryAdmin,
                                      admin.ModelAdmin):
    form = Covid19PreventiveBehaviorsForm
    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'people_sneezing',
                'avoid_touching',
                'dislike_face_mask',
                'temperature',
                'crowded_places',
                'self_isolate',
                'use_hand_sanitizer',
                'avoid_public_places',)}),
        audit_fieldset_tuple)

    radio_fields = {'people_sneezing': admin.VERTICAL,
                    'avoid_touching': admin.VERTICAL,
                    'dislike_face_mask': admin.VERTICAL,
                    'temperature': admin.VERTICAL,
                    'crowded_places': admin.VERTICAL,
                    'self_isolate': admin.VERTICAL,
                    'use_hand_sanitizer': admin.VERTICAL,
                    'avoid_public_places': admin.VERTICAL,
                    }
