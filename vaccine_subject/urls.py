from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import vaccine_subject_admin

urlpatterns = [
    path('admin/', vaccine_subject_admin.urls),
    path('', RedirectView.as_view(url='admin/'), name='home_url'),
]
