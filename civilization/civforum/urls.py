from django.conf.urls import url

from . import views

urlpatterns = [
    url('boards/$', views.boards, name="boards"),
    url(r'boards/(?P<board_id>[0-9]+)/$', views.board, name="board"),
    url(r'boards/(?P<board_id>[0-9]+)/(?P<thread_id>[0-9]+)/(?P<page_number>[0-9]+)/$', views.thread, name="thread"),
    url('newthread_redirect/(?P<board_id>[0-9]+)/$', views.newthread_redirect,
        name="newthread_redirect"),
    url('newthread/(?P<board_id>[0-9]+)/$', views.newthread, name="newthread"),
    url('newpost/(?P<board_id>[0-9]+)/(?P<thread_id>[0-9]+)/$', views.newpost, name="newpost"),
    url('tracker/', views.tracker),
    url('search/', views.search, name="search"),
    url('export/', views.export, name="export"),
]
