"""The Amity class, which is the main
model.
"""
from helpers.generate import populate_rooms
from helpers.generate import generate_file
from helpers.allocator import populate_people
from helpers.allocator import allocate_people


class Amity(object):
    """Represents Amity and all its constituents.

    Attributes
    __________

    offices : list
        a list of all the offices in amity.
    living : list
        a list of all the living spaces in amity.
    people : list
        a list of all people, including fellows and staff in amity.
    """

    def __init__(self):
        rooms = populate_rooms()
        self.offices = rooms['offices']
        self.living = rooms['living']
        self.people = []

    def prepare_amity(self):
        """Initialise amity by generating the input file,
        populating the people and allocating them rooms.
        """
        generate_file(100, 'people_input.in')
        populate_people(self, 'people_input.in')
        allocate_people(self)

    def get_unallocated_fellows(self):
        """Return a list of opt-in fellows who did not get a
        living space.
        """
        pass

    def get_unallocated_staff(self):
        """Return a list of staff who do not have an office.
        List includes both fellows and staff.
        """
        pass
