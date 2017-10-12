from django.contrib import admin
from .models import Series,Preaching

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','date_month')
    list_filter = ('created','date_month')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'created'
    ordering = ('date_month','title')


admin.site.register(Series,SeriesAdmin)


class PreachingAdmin(admin.ModelAdmin):
    list_display = ('title', 'series_title', 'preacher', 'active', 'date_preached')
    list_filter = ('active', 'preacher', 'series_title', 'date_preached')
    search_fields = ('title',)
    date_hierarchy = 'created'
    ordering = ('date_preached','active')


admin.site.register(Preaching, PreachingAdmin )


