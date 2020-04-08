from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment

from .models import *


class CrewA(admin.ModelAdmin):
    readonly_fields = ['current_profile_picture']
    list_display = ('full_name', 'skill', 'active', 'profile_picture')
    list_filter = ('active',)
    search_fields = ['full_name', 'skill']
    fieldsets = (
        (None, {
            'fields': (('profile_picture', 'current_profile_picture'), ('full_name', 'skill', 'active'))
        }),
    )


class PortfoliosA(admin.ModelAdmin):
    readonly_fields = ['current_big_image_or_video', 'current_image1', 'current_image2', 'current_image3',
                      'current_image4', 'current_image5', 'current_image6']
    date_hierarchy = 'date_created'
    list_display = ('title', 'date_modified', 'active')
    list_filter = ('service', 'active')
    search_fields = ['title']
    fieldsets = (
        (None, {
            'fields': ('service', 'title', ('big_image_or_video', 'current_big_image_or_video'))
        }),
        ('بیشتر', {
            'classes': ('collapse',),
            'fields': (
                ('image1', 'current_image1'), ('image2', 'current_image2'), ('image3', 'current_image3'),
                ('image4', 'current_image4'),
                ('image5', 'current_image5'), ('image6', 'current_image6'))
        }),
    )


class ServiceA(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_filter = ('active',)
    search_fields = ['title']


class PortfolioDescriptionA(admin.ModelAdmin):
    list_display = ('title', 'short_description')


# class PortfolioDescriptionB(SummernoteModelAdmin):
#     summernote_fields = '__all__'
#
#
# class PortfolioDescriptionC(PortfolioDescriptionA, PortfolioDescriptionB):
#     pass


class AboutUsDescriptionA(admin.ModelAdmin):
    list_display = ('title', 'short_description')


# class AboutUsDescriptionB(SummernoteModelAdmin):
#     summernote_fields = '__all__'
#
#
# class AboutUsDescriptionC(AboutUsDescriptionA, AboutUsDescriptionB):
#     pass


class LandingDescriptionA(admin.ModelAdmin):
    list_display = ('title', 'short_description')


# class LandingDescriptionB(SummernoteModelAdmin):
#     summernote_fields = '__all__'
#
#
# class LandingDescriptionC(LandingDescriptionA, LandingDescriptionB):
#     pass


# admin.site.unregister(Attachment)
admin.site.register(Crew, CrewA)
admin.site.register(Service, ServiceA)
admin.site.register(Portfolio, PortfoliosA)
admin.site.register(PortfolioDescription, PortfolioDescriptionA)
admin.site.register(AboutUsDescription, AboutUsDescriptionA)
admin.site.register(LandingDescription, LandingDescriptionA)

admin.site.site_header = "سینپه گروپ"
admin.site.site_title = "سینپه گروپ"
admin.site.index_title = "پنل مدیریت"
