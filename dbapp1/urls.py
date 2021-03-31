from django.contrib import admin
from django.urls import path
from dbapp1 import views

urlpatterns=[ 
    
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('contact', views.contact,name='contact'),
]
   