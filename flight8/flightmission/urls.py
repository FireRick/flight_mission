from django.urls import path

from flightmission.views import index_view, mission_detail_view


app_name = 'flightmission'
urlpatterns = [
    path('', index_view, name='index'),
    path('mission/<int:mission_id>/', mission_detail_view, name='mission_detail'),
]