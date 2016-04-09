import abc


class Room:

    __metaclass__ = abc.ABCMeta

    # return a list of allocated people.
    def get_allocations(self):
        return self.allocations

    # add a person to the allocations list.
    def allocate_person(self, person):
        if (person.get_type() == 'staff' and self.get_type() == 'living'):
            return False

        elif (person.get_type() == 'fellow' and not person.opt_in):
            return False

        # Avoid double allocations.
        elif (person in self.people):
            return False

        else:
            if (person.allocated):
                return False
            self.allocations.append(person)
            person.allocated = True
            return True

    # a room should say whether it is living or office.
    @abc.abstractmethod
    def get_type(self):
        raise NotImplementedError
