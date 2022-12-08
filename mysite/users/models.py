from django.db import models

# Membuat relasi antara tabel User bawaan django dengan biodata yang kita buat
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# create models
class Biodata(models.Model):
    #CASCADE berarti ketika user kita delete maka biodatanya juga akan terhapus.    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    telp = models.CharField(max_length=16, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return "{}".format(self.nama)
    
    # agar penulisan didashboard admin tidak ada penambahan s seperti biodatas
    class Meta:
        verbose_name_plural = "Biodata"