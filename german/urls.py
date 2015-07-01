from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import like

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^like/(?P<id>\d+)/(?P<update>(0|1))', like),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^feedback/', include('feedback_form.urls')),
    url(r'^', include('zinnia.urls', namespace='zinnia')),
)
