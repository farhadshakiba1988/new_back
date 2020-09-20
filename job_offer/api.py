import json

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from table_engine.src.table_engine import TableEngine
from .model.job_offer import JobOffer
from .serializers import JobOfferSerializer


class ConstAPIView(APIView):
    """APIView for the Const class"""

    serializer_class = JobOfferSerializer

    def post(self, request: Request, *args, **kwargs):
        if request.path.endswith('/create'):
            return self._create(request, *args, **kwargs)
        else:
            return self._list(request, *args, **kwargs)

    def put(self, request, pk, format=None):
        print(pk)
        return Response(pk)

    def _create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save())

    def _list(self, request, *args, **kwargs):
        _query = JobOffer.objects
        table_engine = TableEngine(_query, json.loads(request.body)).init_cols(['sts']).execute()
        return Response(table_engine)
