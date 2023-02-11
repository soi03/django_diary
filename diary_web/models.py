from django.db import models

# Create your models here.

class Myinfo(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    birth = models.DateTimeField('date published')
    age = models.IntegerField()

class Write(models.Model):
    date = models.DateField()
    title = models.CharField('',max_length=200)
    content = models.CharField('',max_length=500)

