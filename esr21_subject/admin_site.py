from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'ESR21 Subject'
    site_title = 'ESR21 Subject'
    index_title = 'ESR21 Subject'


esr21_subject_admin = AdminSite(name='esr21_subject_admin')
