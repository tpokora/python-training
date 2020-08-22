from django.urls import include, path
from rest_framework import routers

from tracker import views

app_name = 'tracker'

router = routers.DefaultRouter()
router.register(r'trackers', views.TrackerList)
router.register(r'records', views.RecordList)

urlpatterns = [
    path('', views.TrackersView.as_view(), name='trackers'),
    path('<int:pk>/', views.TrackerDetailView.as_view(), name='tracker_detail'),
    path('api/', include(router.urls)),
]
