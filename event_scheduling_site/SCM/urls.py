from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from scmapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^$',views.index,name='index'),
    path('scm/',include('scmapp.urls')),
    path('admin/', admin.site.urls),
    path('', include('scmapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
