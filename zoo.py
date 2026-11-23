import random
from datetime import datetime


class Animal:
    def __init__(self, species: str, name: str, birthYear: int, checkupYear: int = 0, energy: int = 100):
        self.species = species
        self.name = name
        self.birthYear = birthYear
        self.checkupYear = checkupYear
        self.energy = energy

    def __str__(self):
        return f"{self.species} {self.name} ({self.birthYear}) - energie: {self.energy}%"

    def play(self):
        usage = random.randint(5, 20)
        if self.energy >= usage:
            self.energy -= usage
            return f"{self.species} {self.name} spotřeboval při hře {usage}% energie a zbývá mu {self.energy}%"
        else:
            return f"{self.species} {self.name} je moc unavený. Potřebuje {usage}% energie, ale má jen {self.energy}%"

    def feed(self):
        filled = 100 - self.energy
        self.energy = 100
        return f"{self.species} {self.name} byl nakrmen a doplnil {filled}% energie."

    def vetCheck(self):
        if self.checkupYear < datetime.now().year:
            return f"{self.species} {self.name} musí k veterináři - platnost prohlídky skončila v roce {self.checkupYear}"
        else:
            return f"{self.species} {self.name} má prohlídku v pořádku. Další kontrola bude za následující počet let: {self.checkupYear - datetime.now().year}"


animal1 = Animal("Lev", "Alex", 2016, 2026, 85)
animal2 = Animal("Zebra", "Marty", 2018, 2022)
animal3 = Animal("Žirafa", "Melman", 2014, 2028, 10)
animal4 = Animal("Lev", "Simba", 2020, 2024, 40)

# testování výpisu
print(animal1)
print(animal2)
print(animal3)

# testování aktivity (hry)
print(animal1.play())
print(animal2.play())
print(animal3.play())

# testování po aktivitě
print(animal1)
print(animal2)
print(animal3)

# testování krmení
print(animal1.feed())
print(animal2.feed())
print(animal3.feed())

# testování po nakrmení
print(animal1)
print(animal2)
print(animal3)

# testování veterinární kontroly
print(animal1.vetCheck())
print(animal2.vetCheck())
print(animal3.vetCheck())


class Zoo:
    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def addAnimal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Do {self.name} bylo přidáno zvíře: {animal.species} {animal.name}")

    def showAnimals(self):
        if len(self.animals) == 0:
            print(f"{self.name} je prázdná!")
        else:
            print(f"Zvířata v {self.name}:")
            for animal in self.animals:
                print(" -->", animal)

    def oldestAnimal(self):
        if len(self.animals) == 0:
            return None
        # lambda sáhne do objektu a vrátí konkrétní birthYear (nejmenší rok = nejstarší zvíře)
        theOldest = min(self.animals, key=lambda a: a.birthYear)
        return theOldest

    def avgEnergy(self):
        if len(self.animals) == 0:
            return 0
        # projde všechna zvířata, vezme vlastnost energy a posčítá je v sumě
        return sum(animal.energy for animal in self.animals) / len(self.animals)

    # --- ROZŠÍŘENÁ PRÁCE S LISTY (pouze pomocí již použitých nástrojů) ---

    def hungryAnimals(self, limit: int = 50):
        # Vytvoří a vrátí nový list zvířat, která mají energii pod stanoveným limitem
        hungry = []
        for animal in self.animals:
            if animal.energy < limit:
                hungry.append(animal)
        return hungry

    def animalsForCheckup(self):
        # Vytvoří a vrátí nový list zvířat, která musí letos nebo zpětně k veterináři
        needVet = []
        for animal in self.animals:
            if animal.checkupYear < datetime.now().year:
                needVet.append(animal)
        return needVet

    def countSpecies(self, targetSpecies: str):
        # Spočítá, kolik zvířat daného druhu v listu je (filtrování do pomocného listu + len)
        found = []
        for animal in self.animals:
            if animal.species == targetSpecies:
                found.append(animal)
        return len(found)


fZoo = Zoo("Filipova Zoo")

fZoo.addAnimal(animal1)
fZoo.addAnimal(animal2)
fZoo.addAnimal(animal3)
fZoo.addAnimal(animal4)

print("---Obsah Zoo---")
fZoo.showAnimals()

print("---Aktivita specifického zvířete---")
print(fZoo.animals[2].play())

print("---Aktivita všech zvířat---")
for animal in fZoo.animals:
    print(animal.play())

print("---Stav energie po aktivitě---")
fZoo.showAnimals()

print("---Průměrný stav energie---")
print(f"{fZoo.avgEnergy():.1f}%")

print("---Nejstarší zvíře---")
oldest = fZoo.oldestAnimal()
if oldest:
    print(f"Nejstarší zvíře v Zoo je {oldest.species} {oldest.name} ({oldest.birthYear})")

print("---Hromadná veterinární kontrola---")
for animal in fZoo.animals:
    print(animal.vetCheck())

print("---Zvířata s energií pod 80 % (filtrování do nového listu)---")
unavenaZvirata = fZoo.hungryAnimals(80)
for animal in unavenaZvirata:
    print(" --> Potřebuje dokrmit:", animal)

print("---Zvířata čekající na veterináře (filtrování do nového listu)---")
proVet = fZoo.animalsForCheckup()
for animal in proVet:
    print(" --> Nutná kontrola:", animal.species, animal.name)

print("---Počet lvů v Zoo---")
print(f"Počet lvů: {fZoo.countSpecies('Lev')}")