from django.contrib import admin
from .models import Dataref
from .models import Project

# Register your models here.
@admin.register(Dataref)
class DatarefAdmin(admin.ModelAdmin):
    list_display = ('data_ref_project', 'data_ref_name')
    ordering = ('data_ref_project','data_ref_name')
    search_fields = ('data_ref_project', 'data_ref_name')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name',)
    ordering = ('project_name',)
    search_fields = ('project_name',)
