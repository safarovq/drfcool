from django.db import models
from common.models import BaseModel, TimeUpdate


class Boys(BaseModel, TimeUpdate):
    category = models.ForeignKey('boys.category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Boy'
        verbose_name_plural = 'Boys'
