import time

print(" __________________________")
print("|     Primezahlenzähler    |")
print("|__________________________|")
print()
time.sleep(1)

tries = int(input("Bis zur welcher Zahl sollen die Primzahlen ermittelt werden: "))

print(" __________________________")
print("|      Zähler startet      |")
print("|__________________________|")
time.sleep(1)

zeitanfang = int(time.time())
print(" __________________________")
print("|       Zähler läuft       |")
print("|__________________________|")

zahl = 1

print
for x in range(tries):
    if zahl > 1:
        for i in range(2, int(zahl/2)+1):
            if (zahl % i) == 0:
                           
                break
        else:
            #print("It is a prime number")
            with open('Primezahlen.txt', 'a') as f:
                f.write(str(zahl) + "\n")
            
            
        zahl+=1
    else:
        zahl+=1
zeitende = int(time.time())
zeit = zeitende-zeitanfang
print(" __________________________")
print("|       Zähler fertig      |")
print("        Zeit: "+ str(zeit) + " Sekunden")
print("|__________________________|")
print()