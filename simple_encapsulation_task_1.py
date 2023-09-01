class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def get_name(self):
        return self.__name

    def set_name(self, user_name):
        self.__name = user_name

    def get_age(self):
        return self.__age

    def set_age(self, user_age):
        self.__age = user_age


person = Person()
person.set_name("Ostap")
print(person.get_name())
person.set_age(18)
print(person.get_age())
