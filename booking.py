import uuid
from datetime import datetime
from payment import PaymentMethod


class Booking:
    def __init__(self, customer, room, days, payment_method: PaymentMethod):
        self.booking_id = str(uuid.uuid4())[:8]
        self.customer = customer
        self.room = room
        self.days = days
        self.total_amount = room.price * days
        self.date = datetime.now()
        self.payment_method = payment_method

    def confirm(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"Customer: {self.customer}")
        print(f"Room: {self.room.room_type()} #{self.room.room_number}")
        print(f"Days: {self.days}")
        print(f"Total Amount: ₹{self.total_amount}")
        self.payment_method.pay(self.total_amount)
        print("Booking confirmed!\n")
