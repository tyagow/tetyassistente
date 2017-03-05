from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from src.reports.forms import ReportForm
from src.reports.models import Report


class ReportListView(ListView):
    model = Report


class ReportDetailView(DetailView):
    model = Report


class ReportCreateView(CreateView):
    model = Report
    # fields = ['content', 'type', 'timestamp']
    form_class = ReportForm

