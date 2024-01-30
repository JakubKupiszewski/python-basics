countries_and_capitals ={"Polska": "Kraków", "Niemcy": "Berlin", "Czechy": "Praga"}

try:
   print(2/ 2)
   print(countries_and_capitals["USA"])

except KeyError:
   print("Nie znaleziono klucza")
except ZeroDivisionError:
   print("Nie dziel przez zero")
finally:
   print("To wykona się zawsze")
# W zależności od błędu wyświetlamy keyerror itd...
print("Jestem tutaj zawsze")