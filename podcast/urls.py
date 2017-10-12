from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$',views.PodcastIndexView.as_view(),name='index'),
    url(r'^(?P<slug>[\w-]+)/',views.PodcastDetailView.as_view(),name='detail')
]