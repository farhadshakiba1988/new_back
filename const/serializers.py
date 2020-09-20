from django.db.models import QuerySet
from django.forms import model_to_dict
from rest_framework import serializers

from .interfaces import IConst
from .model.const import Const


class ConstSerializer(serializers.ModelSerializer):
    HIDDEN = ['active']
    VISIBLE = ['title', 'id', 'k']
    active = serializers.BooleanField(default=True)

    class Meta:
        model = Const
        fields = ['title', 'active']

    def save(self):
        _input = self.initial_data
        return model_to_dict(IConst.set(
            **{k: _input[k] for k in _input.keys() & ('title', 'key', 'left')}
        ), exclude=self.HIDDEN)

    @staticmethod
    def to_dict(data: QuerySet):
        return data.values(*ConstSerializer.VISIBLE)
