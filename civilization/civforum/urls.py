from django.conf.urls import url

from . import views

urlpatterns = [
    url('boards/$', views.boards, name="boards"),
    url(r'boards/(?P<board_id>[0-9]+)/$', views.board, name="board"),
    url('tracker/', views.tracker),
]
