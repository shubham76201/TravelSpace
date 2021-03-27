from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'about.html')

# For the about Page 
def service(request):
    return render(request,'service.html')

# For the about Page 
def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name=name , email=email , phone=phone , desc=desc , date = datetime.today())
        contact.save()
        messages.success(request, ' Profile details updated.')
    return render(request,'contact.html')