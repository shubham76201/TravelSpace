from django.shortcuts import render, redirect
from dbapp2.models import Signup
from dbapp2.models import Locations
from dbapp2.models import Train
from django.contrib.auth.models import User
import requests
import json
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
    return render(request, 'hotel.html')

def train1(request):
    url = "https://trains.p.rapidapi.com/"

    payload = "{\r\"search\": \"Rajdhani\"\r}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "aed6b86374mshef490530de895fcp135547jsnb0954a5a6d1b",
        'x-rapidapi-host': "trains.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    y=json.loads(response.text)
    context={'y1':y}
    #print(y[0]['train_num'])

    return render(request,'train1.html',context)
    #, context={'temp' : y[4]['name']})

def train(request):
    if request.method=="POST":
      Source = request.POST.get('from')
      To = request.POST.get('to')
      date = request.POST.get('CheckIn')
      obj = Locations.objects.create(Source=Source,destination=To,Date=date)
      uploads = Train.objects.filter(Train_No=10222)
      
      return render(request, 'Ticket.html', {'upload':uploads})
      
    else:
        return render(request, 'train.html')

