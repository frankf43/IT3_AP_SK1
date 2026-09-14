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


zvire = Zvire("Luděk", 22)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.zvuk())
print(zvire.predstavSe())
print(zvire.kdeJsi())
print(zvire.jdiNa("Škola"))

zvire2 = Zvire("Amálka", 5, "na zahradě")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstavSe())
print(zvire2.kdeJsi())
print(zvire2.jdiNa("oběd"))