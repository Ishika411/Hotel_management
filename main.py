from booking_manager import BookingManager
from customer import Customer
from hotel import Hotel
from payment import CashPayment, CardPayment
from room import SuiteRoom, DeluxeRoom, StandardRoom


hotel = Hotel("Valley View Hotel")

hotel.add_room(StandardRoom(101))
hotel.add_room(StandardRoom(102))
hotel.add_room(DeluxeRoom(201))
hotel.add_room(SuiteRoom(301))

manager = BookingManager(hotel)

c1 = Customer("Ishika", "9876543210")
c2 = Customer("Vaishnavi", "9123456780")

manager.make_booking(c1, "Standard", 3, CashPayment())
manager.make_booking(c2, "Suite", 2, CardPayment("1234567890123456"))

print("Available rooms:")
for r in hotel.available_rooms():
    print(r)