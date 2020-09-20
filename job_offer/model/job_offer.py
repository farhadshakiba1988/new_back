from itertools import chain

from django.db import models

from const.model.const import Const


class JobOffer(models.Model):
    SELECT = [
        'department__title',
        'job_title__title',
        'org_level__title',
        'workplace__title',
        'education__title',
        'reason__title',
    ]

    # Gender Field Choices
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, 'مرد',),
        (GENDER_FEMALE, 'زن',),
    )

    # Status Field Choices
    class Sts(models.IntegerChoices):
        NOT_ACCEPT = -1, 'تایید نشده'
        ACTIVE = 1, 'تایید'
        ARCHIVED = 2, 'آرشیو شده'

    department = models.ForeignKey(Const, on_delete=models.CASCADE, related_name='department_idd')
    job_title = models.ForeignKey(Const, on_delete=models.CASCADE, related_name='job_title')
    org_level = models.ForeignKey(Const, on_delete=models.CASCADE, related_name='org_level', null=True)
    workplace = models.ForeignKey(Const, on_delete=models.CASCADE, related_name='workplace', null=True)
    description = models.TextField(max_length=2024, null=True)
    skills = models.JSONField(null=True)
    education = models.ForeignKey(Const, on_delete=models.CASCADE, related_name='education', null=True)
    work_experience = models.PositiveSmallIntegerField(null=True)
    reason = models.ForeignKey(Const, on_delete=models.CASCADE, related_name='reason', null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    sts = models.IntegerField(default=Sts.NOT_ACCEPT, choices=Sts.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
