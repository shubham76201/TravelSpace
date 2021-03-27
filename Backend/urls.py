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

admin.site.site_header = 'Shubham Shop Admin'
admin.site.site_title = 'Shubham Shop Admin Panel'
admin.site.index_title = 'Welcome To Shubhams Shoppe Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
    path("about",include('home.urls')),
    path("service",include('home.urls')),
    path("contact",include('home.urls')),
    path("dbapp2/",include('dbapp2.urls')),
]

