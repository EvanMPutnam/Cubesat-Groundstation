from django.contrib import admin
from .models import Dataref


# Register your models here.
@admin.register(Dataref)
class DatarefAdmin(admin.ModelAdmin):
    list_display = ('data_ref_project', 'data_ref_name')
    ordering = ('data_ref_project','data_ref_name')
    search_fields = ('data_ref_project', 'data_ref_name')
