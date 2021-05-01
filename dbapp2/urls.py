from django.contrib import admin
from django.urls import path
from dbapp2 import views
from . import views
app_name='home'
urlpatterns=[path('',views.home,name="hom" ),
    
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('hotel', views.hotel,name='hotel'),
    path('index', views.index,name='index'),
    path('train', views.train,name='train'),
    path('train1', views.train1,name='train1'),
    path('logout', views.logout,name='logout'),
    path('addR/',views.addR,name="addR"),
    path('addST/',views.addST),
    path('addT/',views.addT),
    path('addRT/',views.addRT),
    path('search/addRT/',views.addRT),
    path('search/',views.search),
    path('search/trains',views.getTrains),
    path('search/schedule/',views.schedule),
    path('search/schedule/cancel',views.cancel),
    path('search/schedule/trains',views.getTinfo),
    path('search/search/trains/cva/', views.cva),
    path('search/book1/', views.book1),
    path('search/book1/book/', views.book),
    path('search/cancel/',views.cancel),
    path('search/pnr/cancel/',views.cancel),
    path('search/cancel/cancel/cn/',views.cn),
    path('search/pnr/',views.pnr,name="pnr"),
    path('search/schedule/pnr/',views.pnr,name="pnr"),
    ]
    
