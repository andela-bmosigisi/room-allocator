# incharge of all the allocating.
# Populates an amity object.
from people.Fellow import Fellow
from people.Staff import Staff


def allocate_people(amity):
    """Receives an amity object and allocates people to
    rooms and living spaces.
    """
    p_count = 0
    p_length = len(amity.people)
    people_over = p_length == 0
    # allocate people to offices
    for office in amity.offices:
        if people_over is True:
            break
        while office.has_space():
            office.allocate_person(amity.people[p_count])
            p_count += 1
            if (p_count > p_length):
                people_over = True
                break

    # first, get a list of opt-in fellows.
    fellows = [person for person in amity.people if person.get_type ==
               'fellow' and person.opt_in is True]
    # reset counters.
    p_length = len(fellows)
    people_over = p_length == 0
    p_count = 0
    for living in amity.living:
        if people_over is True:
            break
        while living.has_space():
            living.allocate_person(fellows[p_count])
            p_count += 1
            if (p_count > p_length):
                people_over = True
                break


def populate_people(amity, input_file):
    """Take an amity object and an input file and populate the
    people property of the amity object.

    Arguments:
    amity - an object representing amity, with a people property.
    input_file - the path to the input file.
    """
    with open(input_file, 'r') as f:
        for line in f:
            tokens = line.split
            name = tokens[0] + ' ' + tokens[1]
            if tokens[2] == 'STAFF':
                amity.people.append(Staff(name))
            elif tokens[2] == 'FELLOW' and tokens[3] == 'Y':
                amity.people.append(Fellow(name, True))
            else:
                amity.people.append(Fellow(name, False))
