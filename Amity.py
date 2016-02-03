from helpers.generate import populate_rooms


# The main model. Represents Amity the place, and all its constituents.
class Amity(object):

    def __init__(self):
        rooms = populate_rooms()
        self.offices = rooms['offices']
        self.living = rooms['living']
        self.people = []
