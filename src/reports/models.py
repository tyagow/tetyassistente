import datetime
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.shortcuts import resolve_url as r
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

SENTIMENT_GOOD = 0
SENTIMENT_BAD = 1

SENTIMENT_TYPE_CHOICES = (
    (SENTIMENT_GOOD, _('Good')),
    (SENTIMENT_BAD, _('Bad')),
)

FOOD = 0
FEELING = 1

REPORT_TYPES = (
    (FOOD, _('Alimentação')),
    (FEELING, _('Como estou me sentido?')),
)


class Report(models.Model):
    timestamp = models.DateTimeField(_('Criado'), default=(timezone.now() - datetime.timedelta(hours=3)))
    content = models.TextField(_('Conteúdo'), null=False, blank=False)
    type = models.IntegerField(choices=REPORT_TYPES, default=FEELING, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reports')

    def __str__(self):
        return '{} - {}'.format(self.get_type_display(), self.content)

    def get_absolute_url(self):
        return r('reports:detail', pk=self.id)


def validate_range(value):
    if value not in [0, 1, 2, 3, 4, 5]:  # Your desired conditions here
        raise ValidationError('%s Wrong Range' % value)


class Sentiment(models.Model):
    type = models.IntegerField(choices=SENTIMENT_TYPE_CHOICES, default=SENTIMENT_GOOD)
    score = models.IntegerField(validators=[validate_range])
    report = models.ForeignKey(Report, related_name='sentiments')
