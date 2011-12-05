from django.conf.urls.defaults import *
import settings

handler500 = 'djangotoolbox.errorviews.server_error'

   
# Django Admin
from django.contrib import admin
admin.autodiscover()

# Search for "dbindexes.py" in all installed apps
import dbindexer
dbindexer.autodiscover()

urlpatterns = patterns('',
    # Warmup
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    

    (
     r'^assets/(?P<path>.*)$', 
     'django.views.static.serve',  
     {'document_root': settings.MEDIA_ROOT}
    ),


    # Index
    (r'^$', 'blog.views.index'),
    
    # Django Admin
    (r'^admin/', include(admin.site.urls)),    
    
    #comments
    (r'^comments/', include('django.contrib.comments.urls')),

    #social registration
    url(
        r'^social/',
        include('socialregistration.urls', namespace = 'socialregistration')
    ),
    
    #a post
    url(
        r'^(?P<slug>.*)$', 
        'blog.views.view_post',
        name='view_blog_post'
    ),
    
)

