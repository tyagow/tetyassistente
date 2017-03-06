import datetime
from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from src.reports.models import Report, REPORT_TYPES


class ReportForm(forms.ModelForm):
    timestamp = forms.DateTimeField(label=_('Horário'), input_formats=["%d.%m.%Y - %H:%M"], initial=(timezone.now()-datetime.timedelta(hours=3)).strftime("%d.%m.%Y - %H:%M "))
    type = forms.ChoiceField(label=_('Tipo de report'), choices=REPORT_TYPES, initial=1, widget=forms.Select(),)

    class Meta:
        model = Report
        fields = ['type', 'content', 'timestamp']
        labels = {
            'type': _('Tipos de report'),
        }
