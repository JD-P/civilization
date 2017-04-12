from django.conf.urls import url

from . import views

urlpatterns = [
    url('boards/', views.boards),
    url('tracker/', views.tracker),
]
