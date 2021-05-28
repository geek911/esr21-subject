from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import esr21_subject_admin

app_name = 'esr21_subject'

urlpatterns = [
    path('admin/', esr21_subject_admin.urls),
    path('', RedirectView.as_view(url='admin/'), name='home_url'),
]
