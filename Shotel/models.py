from django.db import models
from django import forms
import datetime
# Create your models here.
CITIES_CHOICES = (
    ('Mumbai', 'Mumbai'),
    ("New Delhi", "New Delhi"),
    ("Kolkata", "Kolkata"),
    ("Chennai", "Chennai"),
    ("Bengaluru", "Bengaluru"),
)
ROOM_CHOICES=(
    ('AC', 'AC Rooms'),
    ('N-AC', 'Non-AC Rooms'),
    ('Deluxe', 'Deluxe Rooms'),
    ('S-Deluxe', 'Super Deluxe Rooms'),
)
class Hotels(models.Model):
    profile = models.ImageField(upload_to = "images/",default="", null=True )
    hname = models.CharField(max_length=100) 
    city = models.CharField(max_length=100, choices=CITIES_CHOICES, null=True)
    nbeds = models.IntegerField(null=True)
    address = models.TextField(default="null")
    rooms = models.CharField(max_length=100, choices=ROOM_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    hemail = models.EmailField(null=True)
    hcontact = models.CharField(max_length=10, null=True)
    mdescription = models.TextField(null=True)
    title1 = models.CharField(max_length=20, null=True)
    descp1= models.CharField(max_length=90, null=True)
    title2 = models.CharField(max_length=20, null=True)
    descp2 = models.CharField(max_length=90, null=True)
    title3 = models.CharField(max_length=20, null=True)
    descp3 = models.CharField(max_length=90, null=True)
    

    class Meta:  
        db_table = "hotels"
