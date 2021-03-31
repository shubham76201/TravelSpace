import datetime
from hotel.models import Room, Booking


def check_availability(room, checkin, checkout):
    avail_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if (booking.checkin > checkout or booking.checkout < checkin):
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
