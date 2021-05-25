from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'Vaccine Subject'
    site_title = 'Vaccine Subject'
    index_title = 'Vaccine Subject'


vaccine_subject_admin = AdminSite(name='vaccine_subject_admin')
