from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from src.core import views as core_views
from src.reports.views import ReportListView, ReportCreateView, ReportDetailView

urlpatterns = [

    url(r'^create$', login_required(ReportCreateView.as_view()), name='create'),
    url(r'^(?P<pk>\d+)$', login_required(ReportDetailView.as_view()), name='detail'),
    url(r'^$', login_required(ReportListView.as_view()), name='list'),
]


