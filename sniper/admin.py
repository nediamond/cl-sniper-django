from django.contrib import admin
from models import *

@admin.register(CLSniper)
class CLSniperAdmin(admin.ModelAdmin):
    fields = ('owner', ('site', 'query'), ('min_price', 'max_price'))
    list_display = ('id','query','owner', 'site')

@admin.register(Hit)
class Hit(admin.ModelAdmin):
    list_display = ('post_name', 'sniper', 'url')