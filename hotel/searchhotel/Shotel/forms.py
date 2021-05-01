from django import forms  
from Shotel.models import Hotels 

class HotelForm(forms.ModelForm):  
    class Meta:  
        model = Hotels  
        fields = "__all__" 
        widgets = {
            'rooms' : forms.CheckboxSelectMultiple(),
        }
        