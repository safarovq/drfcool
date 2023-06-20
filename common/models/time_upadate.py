from django.db import models


class TimeUpdate(models.Model):
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
