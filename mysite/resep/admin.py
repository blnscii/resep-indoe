from django.contrib import admin
from resep.models import *

# Register your models here.
class TempatAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'kontak']
admin.site.register(Tempat, TempatAdmin)

class ResepAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumb', 'key', 'times', 'desc', 'ingredient']
admin.site.register(Resep)
