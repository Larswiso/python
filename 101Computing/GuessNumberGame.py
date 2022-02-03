import random

gedachteZachl = random.randint(1,100)
userGeuss = -1

while userGeuss != gedachteZachl:
    userGeuss = int(input("Schätzen Sie eine Zahl: "))

    if userGeuss > gedachteZachl:
        print("niedriger")
    elif userGeuss < gedachteZachl:
        print("höher")
    elif userGeuss == gedachteZachl:
        print("Genau richtig!")