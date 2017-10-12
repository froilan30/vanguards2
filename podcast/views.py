from django.shortcuts import render
from django.views import generic
from .models import Series, Preaching




class PodcastIndexView(generic.ListView):
    template_name = 'podcast/index.html'
    model = Series
    context_object_name = 'series'


    # def get_queryset(self):
    #     queryset = super(PodcastIndexView, self).get_queryset()
    #     title = Series.objects.get(pk)
    #


class PodcastDetailView(generic.DetailView):
    template_name = 'podcast/detail.html'
    model = Series
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super(PodcastDetailView, self).get_context_data(**kwargs)
        context1= Series.objects.get(slug=self.kwargs['slug'])
        context['preaching_list'] = Preaching.objects.filter(series_title=context1.pk)
        return context







# baka magamit ko
#
# class CourseContentListView(ListView):
#
#     model = Content
#     context_object_name = 'content_list'
#     template_name = 'content/content_list.html'
#
#     def get_queryset(self):
#         queryset = super(CourseContentListView, self).get_queryset()
#         course_name = self.kwargs.get('course_name')
#         course = Course.objects.get(course_name=course_name)
#         queryset = queryset.filter(course=course)
#         return queryset
