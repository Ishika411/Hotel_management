from booking import Booking
from hotel import Hotel

class BookingManager:
    def __init__(self, hotel: Hotel):
        self.hotel = hotel

    def make_booking(self, customer, room_type, days, payment_method):
        room = self.hotel.find_available_room(room_type)

        if room is None:
            print("❌ No rooms available of this type!\n")
            return None

        if room.book():
            booking = Booking(customer, room, days, payment_method)
            booking.confirm()
            return booking

        print("❌ Room is already booked!\n")
        return None

    def checkout(self, booking: Booking):
        booking.room.checkout()
        print(f"Room #{booking.room.room_number} is now available.\n")
