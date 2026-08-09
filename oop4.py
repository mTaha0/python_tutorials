#class attributes and class methods


class Person:
    number_of_people = 0 
    gravity = -9.8

    def __init__(self,name):
        self.name = name
        self.number_of_people = 8

    @classmethod
    def get_number_of_people(cls):
        cls.number_of_people = 5
        return cls.number_of_people

p1 = Person("taha")
p2 = Person("emin")
print(p1.number_of_people)
print(p2.number_of_people)
Person.get_number_of_people()

print(Person.number_of_people)

