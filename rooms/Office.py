from .Room import Room


class Office(Room):

    def __init__(self, name):
        self.name = name
        self.allocations = []

    def get_type(self):
        return 'office'
