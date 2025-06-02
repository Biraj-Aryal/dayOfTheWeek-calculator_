from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar, name='gregorian_calendar'),
]
