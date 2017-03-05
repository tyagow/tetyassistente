from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import resolve_url
from django.test import TestCase

from src.reports.models import Report, REPORT_TYPES, FOOD, FEELING


class ReportModelTest(TestCase):
    """
    Modelo Report deve guardar informações sobre um usuario feitas em um certo horario
    Report
    """
    def setUp(self):
        user = User.objects.create(username='tety', password='123456')
        self.report = Report(type=1, user=user)
        self.report.save()

    def test_created(self):
        self.assertTrue(Report.objects.exists())

    def test_has_timestamp_not_blank(self):
        field = self.report._meta.get_field('timestamp')
        self.assertFalse(field.blank)

    def test_type_food_choices(self):
        """Test type 1 choice"""
        self.assertEqual(self.report.get_type_display(), REPORT_TYPES[FOOD][1])

    def test_tipo_choices_feeling(self):
        """Test type 2 choice"""
        self.report.type = REPORT_TYPES[FEELING][0]
        self.assertEqual(self.report.get_type_display(), REPORT_TYPES[FEELING][1])

    def test_type_should_be_limited(self):
        """:type must be limited to 1, 2"""
        self.report.type = -1
        self.assertRaises(ValidationError, self.report.full_clean)

    def test_content_not_blank(self):
        field = self.report._meta.get_field('content')
        self.assertFalse(field.blank)
        self.assertRaises(ValidationError, self.report.full_clean)

    def test_str_representation(self):
        self.assertEqual(str(self.report), '{} - {}'.format(self.report.get_type_display(), self.report.content))

    def test_get_absolute_url(self):
        url = resolve_url('reports:detail', pk=self.report.id)
        self.assertEqual(url, self.report.get_absolute_url())

    def test_has_user_related(self):
        user = User.objects.first()
        self.assertEqual(self.report.user, user)