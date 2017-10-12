from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Series(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    logo = models.FileField()
    date_month = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('podcast:detail', args=[self.slug])

    def __str__(self):
        return self.title




class Preaching(models.Model):
    title = models.CharField(max_length=250)
    series_title = models.ForeignKey(Series,on_delete=models.CASCADE)
    preacher = models.CharField(max_length=80)
    audio_file = models.FileField()
    active = models.BooleanField(default=True)
    date_preached = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title +'-'+ self.preacher





