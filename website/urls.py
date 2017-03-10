from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^language/(?P<language_name>[\w]+)/$', views.language),
    url(r'^media/(?P<media_id>[0-9]+)/$', views.media),
]
