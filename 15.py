class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstawienie(self, powitanie = "Cześć"):
        return powitanie + ", jestem " + self.imie + " lat " + str(self.wiek) + "."
    
username = Czlowiek("Sebastian", 24)
print(username.imie)
print(username.przedstawienie(powitanie = "Witam"))
username2 = Czlowiek("Adrian", 18)
username2.imie = "Adrian"
print(username2.przedstawienie())