from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tracker.views import TrackerList, RecordList, RecordListByTrackerName

urlpatterns = [
    path('trackers/', TrackerList.as_view()),
    path('records/', RecordList.as_view()),
    path('records/<tracker_name>/', RecordListByTrackerName.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
