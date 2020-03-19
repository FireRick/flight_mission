from django.urls import path

from flightmission.views import (
    index_view, mission_detail_view, mission_upload_view, mission_upload_done_view,
)

app_name = 'flightmission'
urlpatterns = [
    path('', index_view, name='index'),
    path('mission/<int:mission_id>/', mission_detail_view, name='mission_detail'),
    path('mission_upload/', mission_upload_view, name='mission_upload'),
    path('mission_upload/done/', mission_upload_done_view, name='mission_upload_done'),
]