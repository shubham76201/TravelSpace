from django.shortcuts import render
from django.views.generic import ListView
from .models import Room, Booking

class RoomList(ListView):
    model =  Room

class BookingList(ListView):
    model = Booking