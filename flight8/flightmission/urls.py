from django.urls import path

from flightmission.views import index_view


app_name = 'flightmission'
urlpatterns = [
    path('', index_view, name='index'),
]