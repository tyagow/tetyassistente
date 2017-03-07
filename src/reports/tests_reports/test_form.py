import datetime
from django.utils import timezone

from src.reports.forms import ReportForm
from src.testutlis.utils import TestFormBase


class SubscriptionFormTest(TestFormBase):

    def make_validated_form(self, **kwargs):
        valid = dict(
            type=1,
            timestamp=(timezone.now()-datetime.timedelta(hours=3)).strftime("%d.%m.%Y - %H:%M "),
            content='Conteudo report',
            user=1
        )
        data = dict(valid, **kwargs)
        form = ReportForm(data)
        form.is_valid()
        return form

    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = ReportForm()
        expected = ['type', 'content', 'timestamp']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_timestamp_invalidation_input(self):
        form = self.make_validated_form(
            timestamp='23/5/2553 - 14:34'
        )
        self.assertFormErrorCode(form, 'timestamp', 'invalid')

    def test_timestamp_invalidation_input_message(self):
        form = self.make_validated_form(
            timestamp='23/5/2553 - 14:34'
        )
        self.assertFormErrorMessage(form, 'timestamp', 'Introduza uma data/hora válida.')

    def test_timestamp_has_valid_format_to_send(self):
        form = self.make_validated_form(
            timestamp=(timezone.now()-datetime.timedelta(hours=3)).strftime("%d.%m.%Y - %H:%M ")
        )
        self.assertTrue(form.cleaned_data['timestamp'])
