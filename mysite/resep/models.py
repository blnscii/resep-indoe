from django.db import models

# Create your models here.
class Tempat(models.Model):
    nama = models.CharField(max_length=50)
    thumb = models.URLField(blank=True, null=True)
    alamat = models.TextField()
    kontak = models.IntegerField()
    
    def __str__(self):
        return self.nama
    

class Resep(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.URLField(blank=True, null=True)
    key   = models.CharField(max_length=100)
    times = models.CharField(max_length=50)
    step  = models.TextField()
    ingredient = models.TextField()
    
    def __str__(self):
        return self.title
    