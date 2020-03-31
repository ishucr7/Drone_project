from location import Location
class Station:
    def __init__(self, name, coord):
        self.name = name
        self.location = Location(coord[0], coord[1])
