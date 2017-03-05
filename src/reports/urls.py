from django.conf.urls import url

from src.core import views as core_views
from src.reports.views import ReportListView, ReportCreateView, ReportDetailView

urlpatterns = [

    url(r'^create$', ReportCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)$', ReportDetailView.as_view(), name='detail'),
    url(r'^$', ReportListView.as_view(), name='list'),
]


