from rest_framework.response import Response
from rest_framework.views import APIView

from .interfaces import IConst
from .serializers import ConstSerializer


class ConstAPIView(APIView):
    """APIView for the Const class"""

    serializer_class = ConstSerializer

    def get(self, request, *args, **kwargs):
        _key = request.GET['key'] if 'key' in request.GET else None
        _left = request.GET['left'] if 'left' in request.GET else None
        if _key is None and _left is not None:
            export = IConst.get_by_left(_left)
        else:
            export = IConst.get_by_key(_key)
        return Response(ConstSerializer.to_dict(export))

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save())

    def put(self, request, pk, format=None):
        print(pk)

        return Response(pk)
