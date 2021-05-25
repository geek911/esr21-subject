from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'esr21_subject'
    verbose_name = 'ESR21 Subject CRFs'
    admin_site_name = 'esr21_subject_admin'
