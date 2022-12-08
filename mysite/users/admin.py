from django.contrib import admin
from .models import Biodata

# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    # untuk membuat tabel yang rapi pada tabel dashboard admin
    list_display = ('user', 'nama', 'telp', 'alamat')
    # untuk search data pada tabel dashboard admin
    search_fields = ('user', 'nama')
    
    admin.site.register(Biodata, )