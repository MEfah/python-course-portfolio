from django.urls import path

from jobs.views import IndexJobsListView, JobsDetailView

urlpatterns = [
    path("", IndexJobsListView.as_view(), name="jobs"),
    path("<int:pk>/", JobsDetailView.as_view(), name="job"),
]
