import datetime
from django import forms
from django.forms import HiddenInput
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from src.reports.models import Report, REPORT_TYPES

TIMESTAMP_FORMAT = "%d/%m/%Y %H:%M"


class ReportForm(forms.ModelForm):
    timestamp = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'onfocus': 'blur()'}),
        label=_('Horário'),
        input_formats=[TIMESTAMP_FORMAT],
        initial=(timezone.now()-datetime.timedelta(hours=3)).strftime(TIMESTAMP_FORMAT),
    )
    type = forms.ChoiceField(label=_('Tipo de report'), choices=REPORT_TYPES, initial=1, widget=forms.HiddenInput())

    class Meta:
        model = Report
        fields = ['type', 'timestamp', 'content']
        # labels = {
        #     'type': _('Tipos de report'),
        # }
