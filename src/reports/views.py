from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.views.generic import ListView

from src.reports.forms import ReportForm
from src.reports.mixins import ObjectOnwerMixin, RedirectSuccessURLMixin, NextParameterMixin
from src.reports.models import Report


class ReportListView(ListView):
    model = Report

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-timestamp')


class ReportDetailView(DetailView):
    model = Report


class ReportDeleteMixin(NextParameterMixin, RedirectSuccessURLMixin, ObjectOnwerMixin, DeleteView):
    model = Report
    success_url = '/report/'


class UpdateReportView(ObjectOnwerMixin, UpdateView):

    model = Report
    form_class = ReportForm

    success_url = '/report/'


class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
