from django.contrib import admin
from .models import Category, Boys


# Register your models here.
@admin.register(Boys)
class BoysAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
