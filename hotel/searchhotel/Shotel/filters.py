#filters.py
from django.contrib.auth.models import User
import django_filters
from Shotel.models import Hotels 
 
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Hotels
        exclude = ['profile']
        fields = "__all__" 