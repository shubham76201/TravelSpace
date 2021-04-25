from django.db import models

class Signup(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.CharField(max_length=600)
    date = models.DateField()

    def __str__(self):
        return self.name
class Locations(models.Model):
    Source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    Date=models.DateField()

class Train(models.Model):
    Train_No = models.IntegerField()
    Train_Source = models.CharField(max_length=255)
    Train_Destination = models.CharField(max_length=255)
    Train_Name = models.CharField(max_length=255)
    Train_Type = models.CharField(max_length=255)
    def __str__(self):
        return self.Train_Name
        return self.Train_Source