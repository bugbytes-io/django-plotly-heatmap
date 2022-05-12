from django.contrib import admin
from core.models import Repository, Commit 

admin.site.register(Repository)
admin.site.register(Commit)