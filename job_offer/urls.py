from django.urls import path
from . import api

urlpatterns = [
    path('/', api.ConstAPIView.as_view()),
    path('/<int:pk>', api.ConstAPIView.as_view()),
    path('/create', api.ConstAPIView.as_view()),
]
