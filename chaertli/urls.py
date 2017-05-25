from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='chaertli-index'),
    url(r'^list/$', views.ChaertliListView.as_view(), name='chaertli-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ChaertliDetailView.as_view(), name='chaertli-detail')
]