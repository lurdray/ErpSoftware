from django.contrib import admin
from project.models import Project, Brief, Client

# Register your models here.
admin.site.register(Project)
admin.site.register(Brief)
admin.site.register(Client)