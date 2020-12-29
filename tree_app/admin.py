from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.TreeModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("tree_name","tree_scientific_name","tree_preciousness","added_by_user")
    search_fields = ("tree_name","tree_scientific_name","tree_preciousness","added_by_user")

