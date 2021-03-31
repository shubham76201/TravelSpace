from django.contrib import admin
from django.urls import path
from dbapp3 import views


urlpatterns=[path('logout/', views.logout,name='logout'),
    
]