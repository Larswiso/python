# Passwörter erstellen lassen
# Passwörter überprüfen lassen nach Sicherheit
# Passwörten in 'Passwörter.txt' speichern





import random

#-----------------------------------------------------------------------------------




chars = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"         #Zeichen

def genPWD():
    password_länge = int(input("Wie viele Zeichen soll das Passwort haben: "))
    
    for x in range(0,1):
        password = ""
        for x in range(0, password_länge):                                  #Passwort wird generiert
            password_char = random.choice(chars)
            password = password + password_char
        print("Dein Passwort: ", password)



    safePWD = input("Wollen Sie ihr erstelltes Passwort speichern (ja oder nein): " )      #Möglickeit erstelltes Passwort  zu speichern

    if safePWD == "ja":
        ask_zweck = input("Für welchen Zweck (z.B. eine Website): ")
        ask_username = input("Benutzername: ")
        ask_email = input("E-Mail Adresse : ")

    
        with open('Passwörter.txt', 'a') as f:
            f.write(ask_zweck + "|" + ask_email + ask_username + "|" + password + "\n") #1. Zweck 2. E-Mail Adresse 3. Benutzername 4. Passwort
            print("Daten wurden gespeichert")

    elif safePWD == "nein":
        print("")
    else:
        print("Falsche Eingabe")

#------     



def checkPWD():
    inp_ckeck_pwd = input("Bitte geben Sie ein ihr Passwort ein: ")

    lowercase = False
    uppercase = False
    zahl = False
    sonderderzeichen = False
    länge = False
    score = 0

    for character in inp_ckeck_pwd:
        if character in "abcdefghijklmnopqrstuvwxyz":
            lowercase = True
        elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True
        elif character in "1234567890":
            zahl = True
        else:
            sonderderzeichen = True
    
    if lowercase==True and uppercase==True:
        score=score + 10
    if zahl==True and (lowercase==True or uppercase == True):
        score=score + 10
    if sonderderzeichen==True:
        score=score + 10
    if len(inp_ckeck_pwd) >= 10:
        score=score + 5


    if score < 10:
        print("\n""Sehr schlechtes Passwort.")
    elif score < 20:
        print("\n""nicht ausreichendes Passwort.")
    elif score < 30:
        print("\n""gutes Passwort.")
    elif score < 40:
        print("\n""Sicheres Passwort")

#-----

def addPWD():
    ask_zweck = input("Für welchen Zweck (z.B. eine Website): ")
    ask_username = input("Benutzername: ")
    ask_email = input("E-Mail Adresse: ")
    ask_password = input("Passwort: ")
    
    with open('Passwörter.txt', 'a') as f:
        f.write(ask_zweck + "|" + ask_email + ask_username + "|" + ask_password + "\n") #1. Zweck 2. E-Mail Adresse 3. Benutzername 4. Passwort
        print("Daten wurden gespeichert")


#-----------------------------------------------------------------------------------

while True:
    whatDo = input("\n""Was wollen Sie machen (g = Passwortgenerator, c=Passwortüberprüfer, s=Passwortspeicher, q=Programm verlasen): ")

    if whatDo == "g":
        genPWD()
    elif whatDo == "c":
        checkPWD()
    elif whatDo == "s":
        addPWD()
    elif whatDo == "q":
        quit()
    else:
        print("Falsche Eingabe")
