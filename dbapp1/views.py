from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def signin(request):
    if request.method=="POST":
      username1=request.POST['uname']
      password1=request.POST['psw'] 

      s = auth.authenticate(username=username1,password=password1)
      if s is None:
          return redirect('signin')
      else:
          return redirect('/')
    else:
         return render(request,'index.html')

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
