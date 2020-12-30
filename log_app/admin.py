from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.LogTreeModel)
class LogTreeModelAdmin(admin.ModelAdmin):
    list_display = ("log_id","latitude","longitude","pin_code","tree_girth","time_of_logging","logged_by_user","logged_tree")
    search_fields = ("log_id","latitude","longitude","pin_code","tree_girth","time_of_logging","logged_by_user","logged_tree")

