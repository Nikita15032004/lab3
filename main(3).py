
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
guests = int(input("Enter guests quantity: "))
dishes = int(input("Enter dishes quantity: "))

total_cost = 0
count = 0

while count < dishes:
    price = float(input(f"Enter price of dish {count + 1}: "))
    total_cost += price
    count += 1

average_price = total_cost / dishes

person_cost = total_cost / guests

print(f"Average dish price: {average_price:.2f}")
print(f"Person cost: {person_cost:.2f}")



#----------------------------------------
#Zad. 5
print(List(range(80, -1, -4)))

#----------------------------------------
#Zad. 6
while True:
    number = int(input("Enter number: "))
    if number < 0:
        print("You entered negative number! The ghost will come for you! ")
        break
    else:
        print(f"You entered: {number}")


#----------------------------------------
#Zad. 7 - A
n = int(input("Enter students quantity: "))
total_points = 0
count = 0
i = 0

while i < n:
    points = float(input(f"Enter points for student number {i + 1}: "))
    if points < 0 or points > 100:
        print("Points should be from 0 to 100")
        continue
    total_points += points
    count += 1
    i += 1

average = total_points / count
print(f"Average points in group: {average:.2f}")


#----------------------------------------
#Zad. 7 - B
total_points = 0
count = 0

while True:
    points = float(input(f"Enter points for students {count + 1} (or -1 to end the programm): "))
    if points == -1:
        break
    if points < 0 or points > 100:
        print("Points should be from 0 to 100")
        continue
    total_points += points
    count += 1

average = total_points / count if count > 0 else 0
print(f"Average points in group: {average:.2f}")


#----------------------------------------
#Zad. 8
text = "Python jest super"

print("Zerowy:", text[0])
print("Ostatni:", text[-1])
print("Co drugi od zerowego:", text[::2])
print("Co trzeci od pierwszego:", text[1::3])
print("Od dziesiątego do ostatniego:", text[10:])
print("Od końca do początku:", text[::-1])



#----------------------------------------
#zad 9
name = input("Enter your name: ")
print("Witaj", name)

#----------------------------------------
age = input("Enter your age: ")
print("Twój wiek to:", age)

#----------------------------------------
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
initials = first_name[0].upper() + last_name[0].upper()
print("Initials:", initials)

#----------------------------------------
string = input("Enter a string: ")
for _ in range(5):
    print(string)

#----------------------------------------
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
string3 = string1 + string2
print("Concatenated string:", string3)


#----------------------------------------
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
string_united = string1+ string2
half_length = len(string_united) // 2
result = string_united[:half_length]
print("First half of the first string:", result)