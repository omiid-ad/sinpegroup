from django.contrib import admin

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


class AboutUsDescriptionA(admin.ModelAdmin):
    list_display = ('title', 'short_description')


class LandingDescriptionA(admin.ModelAdmin):
    list_display = ('title', 'short_description')


admin.site.register(Crew, CrewA)
admin.site.register(Service, ServiceA)
admin.site.register(Portfolio, PortfoliosA)
admin.site.register(PortfolioDescription, PortfolioDescriptionA)
admin.site.register(AboutUsDescription, AboutUsDescriptionA)
admin.site.register(LandingDescription, LandingDescriptionA)
