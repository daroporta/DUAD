
from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth=date_of_birth

    @property
    def age(self):
        today = date.today()
        return (today.year - self.date_of_birth.year - ((today.month, today.day) < 
        (self.date_of_birth.month, self.date_of_birth.day)))

def decorator(func):
    def calculate_age(user):
        try:
            if user.age >= 18:
                func(user)
            else:
                print(f"You are under age, since your age is {user.age} years.")
        except Exception:
                print(f"The parameters you have entered are not valid.")
    return calculate_age

@decorator
def determine_if_adult(user):
    print(f"You are an adult, since your age is: {user.age} years")

person=User(date(2010, 9, 24))
determine_if_adult(person, 44)

person.date_of_birth= date(2001, 9, 24)
determine_if_adult(person)

