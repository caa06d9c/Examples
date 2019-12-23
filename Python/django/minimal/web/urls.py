from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('', include('root.urls')),
    path('db/', include('db.urls')),
    re_path('echo.*', include('echo.urls')),
    path('admin/', admin.site.urls)
]
