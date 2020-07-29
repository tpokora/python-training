from rest_framework.routers import DefaultRouter

from tracker.views import TrackerList

router = DefaultRouter()
router.register(r'trackers', TrackerList, basename='tracker')

urlpatterns = router.urls
