from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    created = models.DateField()
    active = models.BooleanField()
