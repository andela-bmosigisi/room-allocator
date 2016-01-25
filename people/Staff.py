import Person


class Staff(Person.Person):

    # create a staff member.
    def __init__(self, name):
        self.name = name
        self.allocated = False

    def get_type(self):
        return 'staff'
