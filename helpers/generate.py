import random
from faker import Faker
from rooms.Office import Office
from rooms.Living import Living


faker = Faker()


def populate_rooms():
    offices = []
    living = []
    for i in range(10):
        offices.append(Office(faker.word()))
        living.append(Living(faker.word()))

    return {
        'offices': offices,
        'living': living
    }


def generate_file(number, file_path):
    output_file = open(file_path, 'w')
    for _ in range(number):
        person_name = faker.first_name().upper()
        person_name = person_name + ' ' + faker.last_name().upper()
        # import a random number from 1 to 100
        num = random.randint(1, 100)
        # have a bias to ensure more fellows are generated.
        num = 0 if num < 70 else 1
        line = ''
        # if number is 0, generate staff.
        if (num == 0):
            line = person_name + ' STAFF\n'
        # otherwise, generate fellow.
        else:
            line = person_name + ' FELLOW'
            choice = 'Y' if random.randint(0, 1) == 0 else 'N'
            line = line + ' ' + choice + '\n'
        output_file.write(line)
    output_file.close()
