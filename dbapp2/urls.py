from django.contrib import admin
from django.urls import path
from dbapp2 import views

urlpatterns=[path('', views.index,name='index'),
    
    path('signup',views.signup,name='signup'),
    path('contact', views.contact,name='contact'),
    path('hotel', views.hotel,name='hotel'),
    path('index', views.index,name='index'),
    path('train', views.train,name='train'),
    path('train1', views.train1,name='train1'),
    ]
    
