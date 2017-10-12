from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse



#
# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager,self).get_queryset().filter(status='active')
#
#
#
# class Album(models.Model):
#     STATUS_CHOICES = {
#         ('draft','Draft'),
#         ('active','Active'),
#     }
#
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique_for_date='publish')
#     description = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#
#     active = PublishedManager()
#
#
#     def get_absolute_url(self):
#         return reverse()
#
#     def __str__(self):
#         return self.title
#
#
#
