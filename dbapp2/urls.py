from django.contrib import admin
from django.urls import path
from dbapp2 import views

urlpatterns={
    path('', views.index,name='index'),
    path('admin/',admin.site.urls),
    path('signup',views.signup,name='signup')
}