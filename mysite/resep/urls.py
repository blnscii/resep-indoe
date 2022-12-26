from django.urls import path, include
from . views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('resep', resep, name='tresep'),
    path('detail_resep/<str:key>', resep_detil, name='resep_detil'),
    path('tempat', tempat, name='tempat'),
    path('tambah-lokasi', tambah_lokasi, name='tambah_lokasi'),
    path('ubah-lokasi/<int:id>', ubah_lokasi, name='ubah_lokasi'),
    path('hapus-lokasi/<int:id>', hapus_lokasi, name='hapus_lokasi'),        

]
