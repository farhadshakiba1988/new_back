from django.db import models

from const.model.const import Const


class CRel(models.Model):
    left = models.ForeignKey(Const, on_delete=models.CASCADE, related_name='left')
    right = models.ForeignKey(Const, on_delete=models.CASCADE, related_name='right')
