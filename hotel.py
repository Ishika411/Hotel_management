class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def available_rooms(self):
        return [room for room in self.rooms if room.is_available]

    def find_available_room(self, room_type):
        for room in self.rooms:
            if room.is_available and room.room_type() == room_type:
                return room
        return None

