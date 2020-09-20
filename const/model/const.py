from django.db import models


class Const(models.Model):
    title = models.TextField(max_length=100)
    k = models.PositiveSmallIntegerField()
    active = models.BooleanField(null=True)
