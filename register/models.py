from django.db import models

# Create your models here.
class Person(models.Model):
    full_name = models.CharField(max_length=30)
    usern_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_no = models.IntegerField()
    password = models.IntegerField()
    con_password = models.IntegerField()
