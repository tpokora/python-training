from django.urls import include, path
from rest_framework import routers

from tracker import views

app_name = 'tracker'

router = routers.DefaultRouter()
router.register(r'trackers', views.TrackerList)
router.register(r'records', views.RecordList)

urlpatterns = [
    path('', views.TrackersView.as_view(), name='trackers'),
    path('create', views.create_tracker, name='create_tracker'),
    path('<int:pk>/', views.TrackerDetailView.as_view(), name='tracker_detail'),
    path('<int:tracker_id>/create_record', views.add_record, name='tracker_create_record'),
    path('api/', include(router.urls)),
]
