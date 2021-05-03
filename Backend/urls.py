"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Travel Space Admin'
admin.site.site_title = 'Travel Space Admin Panel'
admin.site.index_title = 'Welcome To Travel Space Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('dbapp2.urls')),
    path("Shotel/",include('Shotel.urls')),
    path("dbapp2/",include('dbapp2.urls')),
    path('Bus/', include('Bus.urls')),
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)