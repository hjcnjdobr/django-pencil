from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('django_pencil.views',
    url(r'upload/$', 'upload_image', name='upload'),

)