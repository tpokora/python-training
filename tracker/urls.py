from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from tracker import views

router = routers.DefaultRouter()
router.register(r'trackers', views.TrackerList)
router.register(r'records', views.RecordList)

urlpatterns = [
    url(r'^', include(router.urls)),
]
