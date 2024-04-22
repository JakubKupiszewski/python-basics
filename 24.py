tablica = ["-","-","-",
           "-","-","-",
           "-","-","-"]
wybrany_gracz = "X"
wygrany = None
działanie_gry = True

def tablica_wyswietlana(tablica):
    print(tablica[0] + "  |  " + tablica[1] + "  |  " + tablica[2])
    print("-------------")
    print(tablica[3] + "  |  " + tablica[4] + "  |  " + tablica[5]) 
    print("-------------")     
    print(tablica[6] + "  |  " + tablica[7] + "  |  " + tablica[8])

def zmiana_gracza():
    global wybrany_gracz
    if wybrany_gracz == "X":
        wybrany_gracz = "O"
    else:
        wybrany_gracz = "X"

def player_input(tablica):
    poprawny_input = False
    while poprawny_input == False:
        inp = int(input("Wybierz liczbe w skali 1-9: "))
        if (inp >= 1 and inp <= 9) and (tablica[inp-1] == "-"):
            tablica[inp-1] = wybrany_gracz
            poprawny_input = True
            zmiana_gracza()
        else:
            poprawny_input = False
            print("To miejsce jest zajęte przez gracza!")

def sprawdzenie_w_poziome(tablica):
    global wygrany 
    if tablica[0] == tablica[1] == tablica[2] and tablica[0] != "-":
        wygrany = tablica[0]
        return True
    elif tablica[3] == tablica[4] == tablica[5] and tablica[3] != "-":
        wygrany = tablica[3]
        return True
    elif tablica[6] == tablica[7] == tablica[8] and tablica[6] != "-":
        wygrany = tablica[6]
        return True
    
def sprawdzenie_w_pionie(tablica):
    global wygrany
    if tablica[0] == tablica[3] == tablica[6] and tablica[0] != "-":
        wygrany = tablica[0]
        return True
    elif tablica[1] == tablica[4] == tablica[7] and tablica[1] != "-":
        wygrany = tablica[1]
        return True
    elif tablica[2] == tablica[5] == tablica[8] and tablica[2] != "-":
        wygrany = tablica[2]
        return True
    
def sprawdzenie_w_skosach(tablica):
    global wygrany
    if tablica[0] == tablica[4] == tablica[8] != "-":
        wygrany = tablica[0]
        return True
    elif tablica[2] == tablica[4] == tablica[6] != "-":
        wygrany = tablica[2]
        return True
    
def sprawdź_remis(tablica):
    global działanie_gry
    if "-" not in tablica:
        tablica_wyswietlana(tablica)
        print("Remis")
        działanie_gry = False
        exit()

def sprawdź_wygrana():
    if sprawdzenie_w_poziome(tablica) or sprawdzenie_w_pionie(tablica) or sprawdzenie_w_skosach(tablica):
        print(f"Wygrał {wygrany}")
        exit()

            
while działanie_gry:
    tablica_wyswietlana(tablica)
    player_input(tablica)
    sprawdź_wygrana()
    sprawdź_remis(tablica)