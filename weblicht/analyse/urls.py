from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^words/$', views.words, name='words'),
    url(r'^sentences/$', views.sentences, name='sentences'),
    url(r'^morph/$', views.morph, name='morph_analysis'),
    url(r'^$', views.index, name='index'),
]
