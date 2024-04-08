from django.db import models

# Create your models here.


class Person_login(models.Model):
    full_name = models.CharField(max_length=30)
    password = models.IntegerField()

    