from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def signin(request):
    if request.method=="POST":
      username1=request.POST['uname']
      password1=request.POST['psw'] 

      user = auth.authenticate(username=username1,password=password1)
      if user is not None:
          auth.login(request,user)
          return redirect('/')
      else:
        return redirect('signin')
        #return render(request,'LandingPage.html', context={'temp4' : username1})
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