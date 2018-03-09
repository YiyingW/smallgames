from django.conf.urls import url

from . import views

app_name = 'games'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/(?P<game_id>[0-9]+)$', views.detail, name='detail'),
    
]