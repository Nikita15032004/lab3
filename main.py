
#----------------------------------------
#Zad. 1
def kontrol_paliwa():
    paliwo = 100
    paliwo_zuzycie = 10
    czas = 0

    while paliwo > 0:
        print(f"Pozostalo paliwa: {paliwo} litrow")
        paliwo -= paliwo_zuzycie
        czas += 1



    print("Koniec lotu.")
kontrol_paliwa()

#----------------------------------------
#Zad. 2
liczba = 2
lizchnik = 0
listaPerwz = []
while lizchnik < 10:
    for i in range(2, liczba):
        if liczba % i == 0:
            break
    else:
        listaPerwz.append(str(liczba))
        lizchnik += 1
    liczba += 1
print(", ".join(listaPerwz))


#----------------------------------------
#Zad. 3
#
ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
numery = [1, 2, 3, 4, 5]
mieszkania = ["/1", "/2", "/3", "/4", "/5", "/6", "/7", "/8", "/9", "/10"]
for ulica in ulice:
    for numer in numery:
        for mieszkanie in mieszkania:
            print("Ullica", ulica, "numer", numer, "mieszkanie", mieszkanie)


#----------------------------------------
#Zad. 4


#----------------------------------------
#Zad. 5
print(List(range(80, -1, -4)))