import abc


class Person:

    __metaclass__ = abc.ABCMeta

    # a person should say whether he is a fellow or staff.
    @abc.abstractmethod
    def get_type(self):
        raise NotImplementedError
