from .Person import Person


class Fellow(Person):

    # create a fellow.
    def __init__(self, name, opt_in=False):
        self.name = name
        self.opt_in = opt_in
        self.allocated = False

    def get_type(self):
        return 'fellow'
