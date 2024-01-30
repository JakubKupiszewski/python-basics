#TWORZENIE NOWEGO PLIKU:
file = open("countries_and_capitals.txt", "w+")

countries_and_capitals = {"Poland": "Krakow",
                         "Czechia": "Prague", "German": "Berlin"}

for country, capitals in countries_and_capitals.items():
   file.write(country + " - " + capitals + "\n")

file.close()