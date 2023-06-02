class User:
    def __init__(self, id, name, connected_room):
        self.id = int(id)
        self.name = str(name)
        self.connected_room = bool(connected_room)