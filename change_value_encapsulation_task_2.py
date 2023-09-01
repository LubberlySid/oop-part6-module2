class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def get_name(self):
        return self.__name

    def set_name(self, user_name):
        if not any(char.isdigit() for char in user_name):
            self.__name = user_name
        else:
            raise ValueError("The name cannot contain numbers")

    def get_age(self):
        return self.__age

    def set_age(self, user_age):
        if 0 <= user_age <= 120:
            self.__age = user_age
        else:
            raise ValueError("Age must be in the range from 0 to 120")


person = Person()
person.set_name("Ostap")
print(person.get_name())
print(person.get_age())
person.set_name("123John")  # ValueError
person.set_age(150)  # ValueError
