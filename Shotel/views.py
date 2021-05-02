from django.shortcuts import render, redirect
from Shotel.forms import HotelForm  
from Shotel.models import Hotels  
from django.views import View

from django.contrib.auth.models import User
from Shotel.filters import UserFilter
 
# Create your views here.
class show(View):
    def get(self, request):  
        hotels = Hotels.objects.all()  
        return render(request,"show.html",{'hotels':hotels}) 

class details(View):
    def get(self, request, id):
        hotels = Hotels.objects.get(id=id)  
        return render(request, 'details.html', {'hotels': hotels}) 

def search(request):
    user_list = Hotels.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})