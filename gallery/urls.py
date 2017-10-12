from django.conf.urls import url,include
from photologue import views



urlpatterns= [
    url(r'^$',views.GalleryArchiveIndexView.as_view(template_name='gallery/gallery.html'),name='galleryindex'),


]


