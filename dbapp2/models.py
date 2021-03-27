from django.db import models

class Signup(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.name
    
