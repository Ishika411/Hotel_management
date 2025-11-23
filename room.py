from abc import ABC, abstractmethod
class Room(ABC):
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.is_available = True

    def book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def checkout(self):
        self.is_available = True

    @abstractmethod
    def room_type(self):
        pass

    def __str__(self):
        return f"{self.room_type()} Room #{self.room_number} | Price: {self.price} | Available: {self.is_available}"

class StandardRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, price=2000)

    def room_type(self):
        return "Standard"

class DeluxeRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, price=3500)

    def room_type(self):
        return "Deluxe"

class SuiteRoom(Room):
    def __init__(self, room_number):
        super().__init__(room_number, price=6000)

    def room_type(self):
        return "Suite"
