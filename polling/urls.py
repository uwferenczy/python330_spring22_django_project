from django.urls import path
from polling.views import PollDetailView, PollListView

urlpatterns = [
    path("", PollListView.as_view(), name="poll_index"),
    path("polls/<int:pk>", PollDetailView.as_view(), name="poll_detail")
    # path('', list_view, name="poll_index"),
    # path('polls/<int:poll_id>', detail_view, name="poll_detail")  # polling/polls/1
]
