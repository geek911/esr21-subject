from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from datetime import datetime
from dateutil.tz import gettz


class AppConfig(DjangoAppConfig):
    name = 'esr21_subject'
    verbose_name = 'ESR21 Subject CRFs'
    admin_site_name = 'esr21_subject_admin'

    def ready(self):
        from .models import informed_consent_on_post_save


if settings.APP_NAME == 'esr21_subject':
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfigs
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfigs):
        protocol = 'ADZ1222'
        protocol_name = 'ADZ 1222 - ESR-21-21311'
        protocol_number = '1222'
        protocol_title = ''
        study_open_datetime = datetime(
            2021, 4, 15, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))
