from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='chaertli-index'),
    url(r'^list/$', views.ChaertliListView.as_view(), name='chaertli-list'),
]