import datetime
from django.conf import settings
from django.db import models

# Create your models here.
from django.shortcuts import resolve_url as r
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

REPORT_TYPES = (
    (1, _('Alimentação')),
    (2, _('Como estou me sentido?')),
)
FOOD = 0
FEELING = 1


class Report(models.Model):
    timestamp = models.DateTimeField(_('Criado'), default=(timezone.now()-datetime.timedelta(hours=3)))
    content = models.TextField(_('Conteúdo'),  null=False, blank=False)
    type = models.IntegerField(choices=REPORT_TYPES, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reports')

    def __str__(self):
        return '{} - {}'.format(self.get_type_display(), self.content)

    def get_absolute_url(self):
        return r('reports:detail', pk=self.id)