from django.db import models
from .uuid import UUIDModel


class BaseModel(UUIDModel):
    name = models.CharField(max_length=255, verbose_name='Name: ')
    description = models.TextField(max_length=255, verbose_name='Description: ')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
