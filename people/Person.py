import abc


class Person:

    __metaclass__ = abc.ABCMeta

    # should return true if person has a room.
    def get_allocated(self):
        return self.allocated

    # set the allocated property of a person.
    def set_allocated(self, status):
        self.allocated = status

    # a person should say whether he is a fellow or staff.
    @abc.abstractmethod
    def get_type(self):
        pass
