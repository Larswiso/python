import random
import time

print(" __________________________")
print("|Doppel-Sechs-Würfel-Spiel |")
print("|__________________________|")
time.sleep(1)


tries_dice1 = 0
tries_dice2 = 0

print("")
username1 = str(input("Spieler 1, wie wollen Sie heißen? "))
username2 = str(input("Spieler 2, wie wollen Sie heißen? "))



start = True
    

while start:

    number1 = number=random.randint(1,6)
    print(number)
    number2 = number=random.randint(1,6)
    print(number)
    tries_dice1 = tries_dice1 + 1

    if number2 == 6 and number1 == 6:
        start = False
        print("\n""Versuche: "+str(tries_dice1))

start = True

print("")
print("Jetzt ist "+username2+" an der Reihe.")
time.sleep(3)
print("")

while start:

    number1 = number=random.randint(1,6)
    print(number)
    number2 = number=random.randint(1,6)
    print(number)
    tries_dice2 = tries_dice2 + 1
    if number2 == 6 and number1 == 6:
        start = False
        print("\n""Versuche: "+str(tries_dice2))

print("")
if tries_dice1 < tries_dice2:
    print("Sieger: "+ username1)
if tries_dice1 > tries_dice2:
    print("Sieger: "+ username2)
if tries_dice1 == tries_dice2:
    print("Unentschieden")