import random
from datetime import datetime
class Car:
    def __init__(self, brand:str, model:str, year:int, stkYear:int = 0, fuel:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.stkYear = stkYear
        self.fuel = fuel

    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - palivo: {self.fuel}%"
    
    def move(self):
        usage = random.randint(5,20)
        if self.fuel >= usage:
            self.fuel -= usage
            return f"{self.brand} {self.model} spotřeboval {usage}% paliva a zbývá mu {self.fuel}"
        else:
            return f"{self.brand} {self.model} by do cíle nedojel. Potřebuje {usage}% paliva, ale má jen {self.fuel}% paliva"

    def fullFill(self):
        filled = 100 - self.fuel
        self.fuel = 100
        return f"{self.brand} {self.model} natankoval {filled}% paliva."
    
    def STK(self):
        if self.stkYear < datetime.now().year:
            return f"{self.brand} {self.model} musí na technickou - technická skončila v roce {self.stkYear}"
        else:
            return f"{self.brand} {self.brand} má technickou v pořádku. Na technickou bude muset za následující počet let: {self.stkYear - datetime.now().year}"

car1 = Car("Škoda", "Octavia 3", 2016, 2026, 85)
car2 = Car("Toyota", "Hilux", 2018, 2022)
car3 = Car("Suzuki", "Swift", 2014, 2028, 3)

#testování výpisu
print(car1)
print(car2)
print(car3)

#testování jízdy
print(car1.move())
print(car2.move())
print(car3.move())

#testování po jízdě
print(car1)
print(car2)
print(car3)

#testování tankování
print(car1.fullFill())
print(car2.fullFill())
print(car3.fullFill())

#testování po natankování
print(car1)
print(car2)
print(car3)

#testování STK
print(car1.STK())
print(car2.STK())
print(car3.STK())

class Garage:
    def __init__(self, name):
        self.name = name
        self.cars = []
    
    def addCar(self, car:Car):
        self.cars.append(car)
        print(f"Do garáže {self.name} bylo přidáno auto: {car.brand} {car.model}")
    
    def showCars(self):
        if len(self.cars) == 0:
            print(f"Garáž {self.name} je prázdná!")
        else:
            print(f"Auta v garáži {self.name}:")
            for car in self.cars:
                print(" -->", car)
        
    def oldestCar(self):
        if len(self.cars) == 0:
            return None
        theOldest = min(self.cars, key = lambda a: a.year)   #lambda je anonymní funkce. Minimum hledá podle nějakého klíče. Jenže v self.cars jsou objekty. Lambda sáhne do objektu a vrátí konkrétní year. Je to jako spreed operator.
        return theOldest
    
    def avgFuel(self):
        if len(self.cars) ==0:
            return 0
        return sum(car.fuel for car in self.cars) / len(self.cars) #projdi všechny auta a zajímá mě vlastnost fuel a ty se posčítají v sumě
    

fGarage = Garage("Filipova Garáž")

fGarage.addCar(car1)
fGarage.addCar(car2)
fGarage.addCar(car3)

print("---Obsah garáže---")
fGarage.showCars()

print("---Jízda specifického auta---")
print(fGarage.cars[2].move())

print("---Jízda všech aut---")
for car in fGarage.cars:
    print(car.move())

print("---Stav paliva po jízdě---")
fGarage.showCars()

print("---Průměrný stav paliva---")
print(f"{fGarage.avgFuel():.1f}%") #na jedno desetinné místo

print("---Nejstarší auto---")
oldest = fGarage.oldestCar()
if oldest:
    print(f"Nejstarší auto v garáži je {oldest.brand} {oldest.model} ({oldest.year})")

print("---Hromadná kontrola STK---")
for car in fGarage.cars:
    print(car.STK())