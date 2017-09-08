from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from src.reports.views import ReportListView, ReportCreateView, ReportDetailView, ReportDeleteMixin, UpdateReportView

urlpatterns = [

    url(r'^create$', login_required(ReportCreateView.as_view()), name='create'),
    url(r'^(?P<pk>\d+)$', login_required(ReportDetailView.as_view()), name='detail'),
    url(r'^edit/(?P<pk>\d+)$', login_required(UpdateReportView.as_view()), name='update'),
    url(r'^delete/(?P<pk>\d+)$', login_required(ReportDeleteMixin.as_view()), name='delete'),
    url(r'^$', login_required(ReportListView.as_view()), name='list'),
]


