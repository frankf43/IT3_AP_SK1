import random

class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass
    def zvuk(self):
        return "???"

    def predstavSe(self):
        return f"Jmenuji se {self.jmeno}, je mi {self.vek} let."

    def kdeJsi(self):
        return f"Jsem v místě zvaném {self.misto}"

    def jdiNa(self, nMisto:str):
        self.misto = nMisto
        return f"Přesunul jsem se na {nMisto}. {self.kdeJsi()}"

class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno

    def zvuk(self):
        return "Haf, haf!"

    def aport(self):
        return f"{self.jmeno} přinesl míček!"

    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekl před tvým kartáčem!"
        else:
            return f"{self.jmeno} se nechal vyčesat."

    def predstavSe(self):
        return f"{super().predstavSe()} jsem {self.plemeno}"

class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva

    def zvuk(self):
        return "Mňau, mňau"

    def utok(self):
        return f"Kočka {self.jmeno} tě naštvaně poškrábala!"

    def pohladit(self):
        if(random.randint(0,1) > 0):
            return self.utok()
        else:
            return f"{self.jmeno} se nechala pohladit a teď spokojeně vrní."

class Papousek(Zvire):
    def __init__(self, jmeno, vek, barvaPeri, misto = "klec"):
        super().__init__(jmeno, vek, misto)
        self.barvaPeri = barvaPeri

    def zvuk(self):
        return "Krák, krák!"

    def opakuj(self, slovo:str):
        return f"{self.jmeno} opakuje: {slovo}! {slovo}!"

class Had(Zvire):
    def __init__(self, jmeno, vek, delkaCm:int, jedovaty:bool, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.delkaCm = delkaCm
        self.jedovaty = jedovaty

    def zvuk(self):
        return "Sssssssss"

    def ustknuti(self):
        if self.jedovaty:
            return f"POZOR! {self.jmeno} tě uštknul a je jedovatý!"
        else:
            return f"{self.jmeno} tě kousnul, ale naštěstí není jedovatý!"

    def predstavSe(self):
        if self.jedovaty:
            typ = "jedovatý"
        else:
            typ = "škrtič"

        return f"Ssssss ... já jsem {self.jmeno}, měřím {self.delkaCm} a jsem {typ}"

betka = Had("Bětka", 8, 250, True, "terárium")
print(betka.zvuk())
print(betka.ustknuti())
print(betka.predstavSe())
print("-"*20)

loko = Papousek("Loko", 5, "modré")
print(loko.zvuk())
print(loko.opakuj("Komorous"))
print("-"*20)

micka = Kocka("Micka", 2, "zrzavá", "košíček")
print(micka.jdiNa("parapet okna"))
print("-" * 20)

    

radegast = Pes("Radegast", 2, "Australský ovčák", "na gauči")

print(radegast.jmeno)
print(radegast.plemeno)
print(radegast.zvuk())
print(radegast.predstavSe())
print(radegast.aport())
print(radegast.vycesat())
print(radegast.kdeJsi())



print("-" * 20)

zvire = Zvire("Luděk", 22)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.zvuk())
print(zvire.predstavSe())
print(zvire.kdeJsi())
print(zvire.jdiNa("Škola"))
print("-" * 20)

zvire2 = Zvire("Amálka", 5, "na zahradě")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstavSe())
print(zvire2.kdeJsi())
print(zvire2.jdiNa("oběd"))
print("-" * 20)

zoo = [radegast, micka, loko, betka]

for obyvatel in zoo:
    print(obyvatel.zvuk())
    print(obyvatel.predstavSe()) #polymorfismus
    print("-" * 20)