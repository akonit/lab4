from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^products/', include('products.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
