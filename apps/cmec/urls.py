from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^pmp', views.pmp, name='pmp'),
    url(r'^ilamb', views.ilamb, name='ilamb'),
    url(r'^results', views.results, name='results'),
    url(r'^mean', views.mean, name='mean'),
    url(r'^variability', views.variability, name='variability'),
    ]
