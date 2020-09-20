from django.urls import path, include
from person.views import test_view

test = [
    path('person', test_view.PersonRest.as_view()),
]

urlpatterns = test
