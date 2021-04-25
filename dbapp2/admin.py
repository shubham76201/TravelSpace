from django.contrib import admin

# Register your models here.
from .models import Signup
from .models import Train
admin.site.register(Signup)
admin.site.register(Train)