
class Pet:

    def __init__(self, species, name, vaccine):
        self.species=species
        self.name=name
        self.vaccine=vaccine


def decorator(func):
    def wrapper(pet):
        if pet.vaccine == False:
            print(f"Your pet {pet.name}, species {pet.species}, is not not vaccinated, \ntherefore, it cannot travel")
        else:       
            func(pet)
    return wrapper


@decorator
def can_travel(pet):
    print(f"Your pet {pet.name}, species {pet.species} is vaccinated, \ntherefore, it can travel.")



cat=Pet("Feline","Lucky", True)
can_travel(cat)

dog=Pet("Canidae","Small", False)

can_travel(dog)

