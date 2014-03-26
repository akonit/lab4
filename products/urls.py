from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from products import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^search/$', views.filteredIndexView, name='search'),
    url(r'^(?P<pk>\d+)/add_opinion/$', views.addOpinion, name='opinion'),
    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),
    url(r"^(\d+)/$", views.post),
)