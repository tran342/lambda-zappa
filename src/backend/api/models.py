import json

from django.db import models
from model_utils.choices import Choices

FIELD_TYPE = Choices(
    ('text', 'Text'),
    ('number', 'Number'),
    ('date', 'Date'),
    ('enum', 'Enum')
)


class DataField(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    is_required = models.BooleanField()
    field_type = models.CharField(choices=FIELD_TYPE, max_length=10)
    enum_values = models.TextField(null=True, blank=True)

    def get_enum_values(self):
        if self.enum_values:
            try:
                return json.loads(self.enum_values)
            except:
                return None

        return None

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.field_type)


class RiskType(models.Model):
    name = models.CharField(max_length=100)
    fields = models.ManyToManyField(DataField)

    def __unicode__(self):
        return u'%s' % self.name


class RiskValue(models.Model):
    risk_type = models.ForeignKey(RiskType)
    data_field = models.ForeignKey(DataField)
    text_value = models.TextField(null=True)
    number_value = models.BigIntegerField(null=True)
    date_value = models.DateTimeField(null=True)
    enum_value = models.TextField(null=True)
