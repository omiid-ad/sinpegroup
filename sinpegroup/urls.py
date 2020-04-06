from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import settings

admin.autodiscover()
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('mainapp.urls')),
                  path('summernote/', include('django_summernote.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
