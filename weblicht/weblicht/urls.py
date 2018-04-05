from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^words/?$', views.words, name='words'),
    url(r'^sentences/?$', views.sentences, name='sentences'),
    url(r'^morph/?$', views.morph, name='morph_analysis'),
    url(r'^$', TemplateView.as_view(template_name="documentation.html")),
]
