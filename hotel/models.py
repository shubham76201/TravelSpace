from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
# Create your models here.


class Room(models.Model):
    ROOM_CATEGORIES=(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} for {self.capacity} people'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin = models.DateTimeField(null=True)
    checkout = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.checkin} to {self.checkout}'

    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBookingView', args=[self.pk, ])

