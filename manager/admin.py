from django.contrib import admin
from .models import *


class ContenAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','body')
    search_fields = ('title',)


admin.site.register(Content,ContenAdmin)
