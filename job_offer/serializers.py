from django.db.models import QuerySet
from django.forms import model_to_dict
from rest_framework import serializers

from job_offer.model.job_offer import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):
    HIDDEN = []
    VISIBLE = []

    class Meta:
        fields = ['department_id', 'job_title_id', 'department__title']
        model = JobOffer

    def save(self):
        _input = self.initial_data
        _record = JobOffer.objects.create(**{k: _input[k] for k in _input.keys() & self.Meta.fields})
        return model_to_dict(_record, exclude=self.HIDDEN),

    @staticmethod
    def to_dict(data: QuerySet):
        return data.values(*JobOfferSerializer.VISIBLE)
