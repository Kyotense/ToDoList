from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.db import models
import datetime

PRIORITY_CHOICES = (
  (1, 'Low'),
  (2, 'Normal'),
  (3, 'High'),
)

class Item(models.Model):
    title = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    #completed = models.BooleanField(default=False)
    #user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-priority', 'title']

    class Admin:
        pass
