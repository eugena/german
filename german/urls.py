from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import like, german_test

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^like/(?P<entry_id>\d+)/(?P<vote>\w+)', like),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^', include('zinnia.urls', namespace='zinnia')), )
