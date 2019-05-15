#from django.conf.urls import url
from django.conf.urls import url
from . import views

#no more regular expressions >>> much simpler URL Patterns
#each app will have its own URL
# paths that start with 'admin'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
];
