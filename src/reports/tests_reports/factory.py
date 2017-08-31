from django.contrib.auth.models import User

from src.reports.models import Report, Sentiment
import uuid


def make_user_model():
    return User.objects.create(username='User - {}'.format(uuid.uuid4().hex), password='123456')


def make_report_model():
    user = make_user_model()
    report = Report(user=user, content='Content test')
    report.full_clean()
    report.save()
    return report


def make_sentiment_model():
    sentiment = Sentiment(score=3, report=make_report_model())
    sentiment.full_clean()
    sentiment.save()
    return sentiment