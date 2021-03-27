from django.shortcuts import render, redirect
from dbapp2.models import Signup
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method=="POST":
        username= request.POST.get('username1')
        first_name= request.POST.get('firstname1')
        last_name= request.POST.get('lastname1')
        email= request.POST.get('email')
        password= request.POST.get('password')
        
        x=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        x.save()
        print("User Created")
        return redirect('/')

    else:
      return render(request,'signup.html')

def index(request):
    return render(request, 'index.html')

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

def hotel(request):
    return render(request, 'LandingPage.html')