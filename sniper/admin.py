from django.contrib import admin
from models import *

@admin.register(CLSniper)
class CLSniperAdmin(admin.ModelAdmin):
    fields = ('owner', ('site', 'query'), ('min_price', 'max_price'))
    list_display = ('query','owner', 'site')