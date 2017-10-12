from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^',include('home.urls',namespace='home',app_name='home')),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blog.urls',namespace='blog',app_name='blog')),
    url(r'^podcast/',include('podcast.urls',namespace='podcast',app_name='podcast')),
    url(r'^gallery/',include('gallery.urls',namespace='gallery')),
    url(r'^gallery/',include('photologue.urls', namespace='photologue'))
]


#iistore nya ang mga media habang hindi pa nakaup yung site
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

