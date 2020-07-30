from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tracker.views import TrackerList


urlpatterns = [
    path('trackers/', TrackerList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
