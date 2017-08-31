from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import resolve_url
from django.test import TestCase

from src.reports.models import Report, REPORT_TYPES, FOOD, FEELING, Sentiment, SENTIMENT_TYPE_CHOICES, SENTIMENT_GOOD, \
    validate_range
from src.reports.tests_reports.factory import make_report_model, make_user_model, make_sentiment_model


class ReportModelTest(TestCase):
    """
    Modelo Report deve guardar informações sobre um usuario feitas em um certo horario
    Report
    """
    def setUp(self):
       self.report = make_report_model()

    def test_created(self):
        self.assertTrue(Report.objects.exists())

    def test_has_timestamp_not_blank(self):
        field = self.report._meta.get_field('timestamp')
        self.assertFalse(field.blank)

    def test_type_default_is_FEELING(self):
        field = self.report._meta.get_field('type')
        self.assertEqual(field.default, FEELING)

    def test_type_food_choices(self):
        """Test type 1 choice"""
        self.report.type = FOOD
        self.assertEqual(self.report.get_type_display(), REPORT_TYPES[FOOD][1])

    def test_tipo_choices_feeling(self):
        """Test type 2 choice"""
        self.report.type = FEELING
        self.assertEqual(self.report.get_type_display(), REPORT_TYPES[FEELING][1])

    def test_type_should_be_limited(self):
        """:type must be limited to 1, 2"""
        self.report.type = -1
        self.assertRaises(ValidationError, self.report.full_clean)

    def test_content_not_blank(self):
        field = Report._meta.get_field('content')
        self.assertFalse(field.blank)
        report = Report(type=1, user=make_user_model())
        self.assertRaises(ValidationError, report.full_clean)

    def test_str_representation(self):
        self.assertEqual(str(self.report), '{} - {}'.format(self.report.get_type_display(), self.report.content))

    def test_get_absolute_url(self):
        url = resolve_url('reports:detail', pk=self.report.id)
        self.assertEqual(url, self.report.get_absolute_url())

    def test_has_user_related(self):
        user = User.objects.first()
        self.assertEqual(self.report.user, user)

    def test_report_type_default_is_FELLING(self):
        field = Report._meta.get_field('type')
        self.assertEqual(field.default, FEELING)


class SentimentModelTest(TestCase):
    """
    Sentiment must have these fields:
    type: can be 1 on 2 and have choices
    score: integer from 0 - 5
    report: each sentiment has a report foreignkey

    """

    def setUp(self):
        self.sentiment = make_sentiment_model()

    def test_create(self):
        self.assertTrue(Sentiment.objects.exists())

    def test_type_has_choices(self):
        field = Sentiment._meta.get_field('type')
        self.assertEqual(field.choices, SENTIMENT_TYPE_CHOICES)

    def test_type_default_is_SENTIMENT_GOOD(self):
        field = Sentiment._meta.get_field('type')
        self.assertEqual(field.default, SENTIMENT_GOOD)

    def test_score_cant_be_blank(self):
        field = Sentiment._meta.get_field('score')
        self.assertFalse(field.blank)

    def test_score_validator_only_acepts_0_5_range(self):
        with self.assertRaises(ValidationError):
            validate_range(6)
            validate_range(-1)
        validate_range(0)
        validate_range(1)
        validate_range(2)
        validate_range(3)
        validate_range(4)
        validate_range(5)

    def test_has_report_relation(self):
        self.assertIsInstance(self.sentiment.report, Report)

    def test_report_cant_be_blank(self):
        field = Sentiment._meta.get_field('report')
        self.assertFalse(field.blank)


