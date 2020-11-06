from django.contrib import admin
from project.models import Project, Brief, Client, Comment, PImage

# Register your models here.
admin.site.register(Project)
admin.site.register(Brief)
admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(PImage)