def Textdateigröße():
    Anzahl_Bits_pro_Zeichen = int(input("Anzahl Bits pro Zeichen: "))
    Anzahl_Zeichen = int(input("Anzahl Zeichen: "))

    rechnung = (Anzahl_Bits_pro_Zeichen*Anzahl_Zeichen)/8

    if rechnung  >= 1000000:
        result =rechnung /1000000
        print("Geschätze Dateigröße: "+ str(result) +"MB")

    elif rechnung  >= 1000:
        result =rechnung /1000
        print("Geschätze Dateigröße: "+ str(result) +"KB")
    

def Bildateigröße():
    Farbtiefe = int(input("Farbtiefe: "))
    Breite_in_Pixel = int(input("Breite in Pixel: "))
    Höhe_in_Pixel = int(input("Höhe in Pixel: "))

    rechnung = (Farbtiefe*Breite_in_Pixel*Höhe_in_Pixel)/8

    if rechnung  >= 1000000:
        result =rechnung /1000000
        print("Geschätze Dateigröße: "+ str(result) +"MB")

    elif rechnung  >= 1000:
        result =rechnung /1000
        print("Geschätze Dateigröße: "+ str(result) +"KB")

def Sounddateigröße():
    Abtastrate = int(input("Abtastrate: "))
    Dauer = int(input("Dauer: "))
    Bittiefe = int(input("Bittiefe: "))
    Anzahl_der_Kanäle = int(input("Anzahl der Kanäle: "))


    rechnung = (Abtastrate*Dauer*Bittiefe*Anzahl_der_Kanäle)/8

    if rechnung  >= 1000000:
        result =rechnung /1000000
        print("Geschätze Dateigröße "+ str(result) +"MB")

    elif rechnung  >= 1000:
        result =rechnung /1000
        print("Geschätze Dateigröße: "+ str(result) +"KB")


def Filmdatei():
    Farbtiefe = int(input("Farbtiefe: "))
    Breite_in_Pixel = int(input("Breite in Pixel: "))
    Höhe_in_Pixel = int(input("Höhe in Pixel: "))
    Bildrate = int(input("Bildrate: "))
    Dauer = int(input("Dauer in Minuten: "))

    Dauer = Dauer*60

    rechnung = (((Farbtiefe*Breite_in_Pixel*Höhe_in_Pixel)*Bildrate)*Dauer)/8

    if rechnung  >= 1000000000:
        result =rechnung /1000000000
        print("Geschätze Dateigröße: "+ str(result) +"GB")

    elif rechnung  >= 1000000:
        result =rechnung /1000000
        print("Geschätze Dateigröße: "+ str(result) +"MB")

    elif rechnung  >= 1000:
        result =rechnung /1000
        print("Geschätze Dateigröße: "+ str(result) +"KB")
        


userinp = int(input("1=Textdateigröße, 2=Bildateigröße, 3=Sounddateigröße: "))

if userinp == 1:
    Textdateigröße()
elif userinp == 2:
    Bildateigröße()
elif userinp == 3:
    Sounddateigröße()
elif userinp == 4:
    Filmdatei()
else:
    print("Falsche Eingabe")