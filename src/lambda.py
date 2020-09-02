people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]


def f(person: dict):
    return person["name"]


people.sort(key=lambda person: person["name"])  # key=lambda person: person["name"] same thing key=f
print(people)
