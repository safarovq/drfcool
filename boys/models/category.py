from django.db import models
from common.models import BaseModel


class Category(BaseModel):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
