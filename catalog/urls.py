from django.conf.urls import url
from . import views

app_name = 'catalog'
urlpatterns = [
    #url(r'^$', views.index , name='index'),
    url(r'^$', views.index , name='index'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]