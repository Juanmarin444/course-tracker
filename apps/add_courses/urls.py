from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
]
