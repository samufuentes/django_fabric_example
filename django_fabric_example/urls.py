from django.conf.urls import patterns, include, url

import auto_deploy

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_fabric_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url( r'^autodeploy/', include('auto_deploy.urls', namespace='auto_deploy')),

    url(r'^admin/', include(admin.site.urls)),
)
