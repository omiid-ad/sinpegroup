from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


class CrewA(admin.ModelAdmin):
    list_display = ('full_name', 'skill', 'active', 'profile_picture')
    list_display_links = ['profile_picture']
    list_filter = ('active',)
    search_fields = ['full_name', 'skill']
    fieldsets = (
        (None, {
            'fields': ('profile_picture', ('full_name', 'skill', 'active'))
        }),
    )


class PortfoliosA(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = (
        'title', 'date_modified', 'active', 'big_image_or_video', 'image1', 'image2', 'image3', 'image4', 'image5',
        'image6')
    list_filter = ('service', 'active')
    search_fields = ['title']
    fieldsets = (
        (None, {
            'fields': ('service', 'title', ('big_image_or_video'))
        }),
        ('بیشتر', {
            'classes': ('collapse',),
            'fields': ('image1', 'image2', 'image3', 'image4', 'image5', 'image6')
        }),
    )


class ServiceA(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_filter = ('active',)
    search_fields = ['title']


class PortfolioDescriptionA(admin.ModelAdmin):
    list_display = ('title', 'short_description')


class PortfolioDescriptionB(SummernoteModelAdmin):
    summernote_fields = '__all__'


class PortfolioDescriptionC(PortfolioDescriptionA, PortfolioDescriptionB):
    pass


class AboutUsDescriptionA(admin.ModelAdmin):
    list_display = ('title', 'short_description')


class AboutUsDescriptionB(SummernoteModelAdmin):
    summernote_fields = '__all__'


class AboutUsDescriptionC(AboutUsDescriptionA, AboutUsDescriptionB):
    pass


class LandingDescriptionA(admin.ModelAdmin):
    list_display = ('title', 'short_description')


class LandingDescriptionB(SummernoteModelAdmin):
    summernote_fields = '__all__'


class LandingDescriptionC(LandingDescriptionA, LandingDescriptionB):
    pass


admin.site.register(Crew, CrewA)
admin.site.register(Service, ServiceA)
admin.site.register(Portfolio, PortfoliosA)
admin.site.register(PortfolioDescription, PortfolioDescriptionC)
admin.site.register(AboutUsDescription, AboutUsDescriptionC)
admin.site.register(LandingDescription, LandingDescriptionC)
