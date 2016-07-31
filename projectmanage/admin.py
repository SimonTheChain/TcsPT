from django.contrib import admin
from .models import Provider, Project, Rejection

admin.site.register(Provider)
admin.site.register(Project)
admin.site.register(Rejection)
