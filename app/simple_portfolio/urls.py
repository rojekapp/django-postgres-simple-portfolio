from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import jobs.views

urlpatterns = [
    path("", jobs.views.home, name="home"),
    path("admin/", admin.site.urls),
    path('job/<int:job_id>',jobs.views.detail,name='detail')
] 


if bool(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)