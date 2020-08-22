from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from tracker import views

router = routers.DefaultRouter()
router.register(r'trackers', views.TrackerList)
router.register(r'records', views.RecordList)

urlpatterns = [
    path('', views.TrackersView.as_view(), name='trackers'),
    path('api/', include(router.urls)),
]
