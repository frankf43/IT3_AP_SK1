class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass

zvire = Zvire("Luděk", 22)
print(zvire.jmeno)
print(zvire.vek)