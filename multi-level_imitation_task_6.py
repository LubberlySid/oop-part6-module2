class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        return f"Animal: {self.name}\nSpecies: {self.species}"


class Mammal(Animal):
    def __init__(self, name, species, diet_type):
        super().__init__(name, species)
        self.diet_type = diet_type

    def display_info(self):
        super().display_info()
        return f"{super().display_info()}\nDiet Type: {self.diet_type}"


class Carnivore(Mammal):
    def __init__(self, name, species, diet_type, teeth_count):
        super().__init__(name, species, diet_type)
        self.teeth_count = teeth_count

    def display_info(self):
        super().display_info()
        return f"{super().display_info()}\nTeeth count: {self.teeth_count}"


class Lion(Carnivore):
    def __init__(self, name, species, diet_type, teeth_count, mane_size):
        super().__init__(name, species, diet_type, teeth_count)
        self.mane_size = mane_size

    def display_info(self):
        super().display_info()
        return f"{super().display_info()}\nMane size: {self.mane_size}"


lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

print(lion.display_info())
print("-------------------------")
print(carnivore.display_info())
print("-------------------------")
print(mammal.display_info())
