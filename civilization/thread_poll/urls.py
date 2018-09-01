from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'boards/(?P<board_id>[0-9]+)/polls/(?P<poll_id>[0-9]+)$',
        views.thread_poll, name="thread_poll"),
    url(r'boards/(?P<board_id>[0-9]+)/new_poll/$',
        views.new_poll, name="new_poll"),
]
