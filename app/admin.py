from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'date_added', 'date_modified', 'preview_url', 'project_url')

admin.site.register(Project, ProjectAdmin)
