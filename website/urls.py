from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^language/(?P<language_name>.+)/$', views.language),
    url(r'^media/(?P<media_id>[0-9]+)/$', views.media),
    url(r'codes/$', views.codes_list),
]
