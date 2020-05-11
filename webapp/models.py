from django.db import models

# Create your models here.
class Iklan(models.Model):
    nama = models.CharField(max_length=200)
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.judul

    