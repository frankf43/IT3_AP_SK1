class NPC:
    def __init__(self, jmeno:str, energie:int):
        self.jmeno = jmeno
        self.energie = energie
        pass

    def predstav_se(self):
        return f"Zde NPC {self.jmeno}"

    def vyraz_na(self, cil):
        if self.energie >= 10:
            self.energie -= 10
            return f"Jdu na cíl {cil}. Zbývá mi energie: {self.energie}"
        else:
            return f"{self.jmeno} nemá dostatek energie pro přesun."


npc = NPC("Hynek Židlík", 10)
print(npc.predstav_se())
print(npc.vyraz_na("Praha"))
print(npc.vyraz_na("Brno"))

class Chodec(NPC):
    def __init__(self, jmeno:str, energie:int, domovska_ctvrt:str):
        super().__init__(jmeno, energie)
        self.domovska_ctvrt = domovska_ctvrt

    def predstav_se(self):
        return f"Zde chodec {self.jmeno}, rajón: {self.domovska_ctvrt}"

    def vyraz_na(self, cil:str):
        if self.energie >= 30:
            self.energie -= 30
            return f"Zahajuji náročný pěší pochod k cíli {cil}. Zbývá energie {self.energie}"
        else:
            return f"{self.jmeno}: Nedostatek energie pro pěší pochod. Je potřeba alespoň 30 a má {self.energie}"

class Policista(NPC):
    def __init__(self, jmeno, energie, zbran_tasena:bool = False):
        super().__init__(jmeno, energie)
        self.zbran_tasena = zbran_tasena

    def predstav_se(self):
        return f"Zde policista LSPD {self.jmeno}"

    def tas_nebo_skryj_zbran(self):
        self.zbran_tasena = not self.zbran_tasena
        if self.zbran_tasena:
            return f"{self.jmeno}: ZBRAŇ TASENA"
        else:
            return f"{self.jmeno}: ZBRAŇ Skryta V POUZDŘE"

class RidicAutobusu(NPC):
    def __init__(self, jmeno, energie):
        super().__init__(jmeno, energie)
        self.cestujici = []

    def naber_cestujici(self, jmeno_cestujiciho:str):
        self.cestujici.append(jmeno_cestujiciho)
        return f"Do autobusu řidiče {self.jmeno} nastoupil cestující: {jmeno_cestujiciho}"

npc1 = Chodec("Big Smoke", 20, "Grove Street")
print(npc1.vyraz_na("Čtvrť Balas"))
print("="*40)
npc2 = Policista("Frank Tenpenny", 100)
print(npc2.tas_nebo_skryj_zbran())
print(npc2.predstav_se())
print(npc2.tas_nebo_skryj_zbran())
print("="*40)
npc3 = RidicAutobusu("František", 50)
print(npc3.naber_cestujici("Ondřej Čadek"))
print(npc3.naber_cestujici("Karl von bahnhof"))
print(npc3.cestujici)
print(npc3.naber_cestujici("Carl Johnson (CJ)"))
print(npc3.cestujici)
print("="*40)

skupina_npc = [npc1, npc2, npc3]
spolecny_cil = "Domů"

for postava in skupina_npc:    # for led in leds
    print(postava.predstav_se())    #led.on()
    print(postava.vyraz_na(spolecny_cil))
    print("-"*40)