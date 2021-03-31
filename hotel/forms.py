from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES=(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    checkin = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"])
    checkout = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"])
