from django.urls import path
from Shotel import views 
from dbapp2 import views
from . import views
from .views import show, details
urlpatterns = [
    path('show', show.as_view()),
    path('user_list', views.search),
    path('details/<int:id>', details.as_view()),
    
]