import json

from django.db.models import Q
from django.http import JsonResponse
from rest_framework import serializers, routers, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from table_engine.src.table_engine import TableEngine
from ..model.person import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first', 'last', 'active', 'created']


class PersonRest(APIView):
    """
    Person list and create person
    """
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        table_engine = TableEngine(Person.objects, json.loads(request.body)).init_cols(['id']).execute()
        return JsonResponse(table_engine, safe=False)

