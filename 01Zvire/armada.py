import random

class Vojak:
    def __init__(self, jmeno:str, hodnost:str, zdravi: int = 100, energie: int = 100):
        self.jmeno = jmeno
        self.hodnost = hodnost
        self.zdravi = zdravi
        self.energie = energie
        pass
    def __str__(self):
        return f"{self.hodnost} {self.jmeno} (Zdraví: {self.zdravi}%, Energie: {self.energie})"

    def trenuj(self):
        vydej = random.randint(15,30)
        if self.energie >= vydej:
            self.energie -= vydej
            return f"{self.hodnost} {self.jmeno} absolvoval běžný výcvik (ztráta {vydej}% energie)."
        else: 
            return f"Odvoláno: {self.hodnost} {self.jmeno} je příliš vyčerpán na výcvik."

    def bitva(self):
        zraneni = random.randint(10,70)
        self.zdravi -= zraneni
        if self.zdravi < 0:
            self.zdravi = 0
        return f"{self.hodnost} {self.jmeno} v bitvě utržil zranění {zraneni}% (Zbývá {self.zdravi}% zdraví)"

class Armada:
    def __init__(self, nazev:str):
        self.nazev = nazev
        self.vojaci = []
        pass
    
    def naberVojaka(self, vojak:Vojak):
        self.vojaci.append(vojak)
        print(f"Zařazen do jednotky: {vojak.hodnost} {vojak.jmeno}")

    def vypisArmadu(self):
        if len(self.vojaci) == 0:
            print(f"Jednotka {self.nazev} je prázdná!")
        else:
            print(f"---Sestava jednotky {self.nazev}---")
            for v in self.vojaci:
                print("-->",v)

    def odstranPadle(self):
        prezivsi = []
        for v in self.vojaci:
            if v.zdravi > 0:
                prezivsi.append(v)
            else:
                print(f"Padl v boji: {v.hodnost} {v.jmeno}")
        self.vojaci = prezivsi

    def hromadnaAkce(self):
        if len(self.vojaci) == 0:
            print("Nemáme žádné vojáky pro bitvu!")
            return
        print(f"Jednotka {self.nazev} vyráží do boje!")
        for v in self.vojaci:
            print(v.bitva())
        self.odstranPadle()

#test = Vojak("Karl von Bahnhof", "vojín")
#print(test)
#print(test.trenuj())
armada = Armada("Armada Leonida")
#armada.vypisArmadu()
#armada.naberVojaka(test)
#armada.vypisArmadu()
#armada.hromadnaAkce()
#armada.odstranPadle()

while True:
    print(30*"=")
    print("=== HLAVNÍ MENU VELITELE ===")
    print(30*"=")
    print("1. Nabrat vojáky")
    print("2. Výpis armády")
    print("3. Trénink vojáků")
    print("4. Hromadná bitva")
    print("5. Konec programu")
    print(30*"=")

    volba = input("Zadej číslo akce 1-5: ")

    match volba:
        case "1":
            jmeno = input("Zadej jméno vojáka: ")
            armada.naberVojaka(Vojak(jmeno,"vojín"))
        case "2":
            armada.vypisArmadu()
            pass
        case "3":
            if len(armada.vojaci) == 0:
                print("Jednotka je prázdná, nikdo netrénuje.")
            else:
                print("Homadný trénink.")
                for v in armada.vojaci:
                    print(v.trenuj())
            pass
        case "4":
            armada.hromadnaAkce()
            pass
        case "5":
            print("Velitel opouští základnu!")
            break
        case _:
            print("Neplatná volba. Zkus to znovu.")