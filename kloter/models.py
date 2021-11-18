from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    no_juz = models.IntegerField()
    nomer_kloter = models.IntegerField()
    ronde = models.IntegerField()
    telepon = models.TextField(max_length=20)
    selesai = models.BooleanField(default=False)

class NumberKloter(models.Model):
    kloter_number = models.IntegerField()
    ronde = models.IntegerField()