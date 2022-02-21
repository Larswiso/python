import math
import numpy as np
from openpyxl import Workbook, load_workbook


inp_t1 = input("t1: ")
inp_t2 = input("t2: ")
inp_r1 = float(input("r1 in cm: "))
inp_r2 = float(input("r2 in cm: "))
inp_Rho = float(input("Rho in cm: "))
inp_h = float(input("h in cm: "))
inp_R = float(input("R in cm: "))

list_t1 = inp_t1.split()
 
list_t1 = list(map(float, list_t1))

year = list_t1[0]
mon = list_t1[1]
day = list_t1[2]
hour = list_t1[3]
min = list_t1[4]
sec = list_t1[5]

year= year*31536000
mon = mon*2628000
day = day*86400
hour = hour*3600
min = min*60

list_t2 = inp_t2.split()
 
list_t2 = list(map(float, list_t2))

year2 = list_t2[0]
mon2 = list_t2[1]
day2 = list_t2[2]
hour2 = list_t2[3]
min2 = list_t2[4]
sec2 = list_t2[5]

year2= year2*31536000
mon2 = mon2*2628000
day2 = day2*86400
hour2 = hour2*3600
min2 = min2*60

erg1 = year + mon + day + hour + min + sec
erg2 = year2 + mon2 + day2 + hour2 + min2 + sec2
total_time_sec = erg2 - erg1
total_time_day = total_time_sec/86400

breitengrad = math.degrees(np.arcsin(inp_h/inp_R))
#breitengrad = 90.0 - breitengrad

sin_01 =  math.degrees(np.arcsin(inp_r1/inp_Rho))
sin_02 =  math.degrees(np.arcsin(inp_r2/inp_Rho))

alpha = sin_01 + sin_02
umlaufdauer = (360/alpha)*total_time_day

inp_r1 = str(inp_r1)
inp_r2 = str(inp_r2)
inp_Rho = str(inp_Rho)
inp_h = str(inp_h)
alpha = str(round(alpha, 2))
umlaufdauer = str(round(umlaufdauer, 3))
zeitdifferenz = str(round(total_time_day, 3))
breitengrad = str(round(breitengrad, 2))

print(f"R: {inp_R}")
print(f"Rho: {inp_Rho}")
print(f"h: {inp_h}")
print(f"r1: {inp_r1}")
print(f"Breitengrad: {breitengrad}°")
print(f"überschrittene Winkel(Alpha): ~{alpha}°")
print("=======================================")
print(f"Sonenrotation: ~{umlaufdauer} Tage")

if float(umlaufdauer) > 24.0 and float(umlaufdauer) < 34.5:
    with open('Res/Sonnenrotationexcel.txt', 'a') as f:
        f.write(zeitdifferenz + " Tage"+ "|" + inp_Rho +"px"+ "|" + inp_h +"px"+ "|" + inp_r1 + "px"+"|"+ inp_r2 + "px"+"|" + breitengrad + "|" + alpha + "|" + umlaufdauer +" Tage"+"\n")
    with open('Res/Sonnenrotation.txt', 'a') as f:
        f.write(zeitdifferenz + "|" + inp_Rho + "|" + inp_h + "|" + inp_r1 +"|"+ inp_r2 + "|" + breitengrad +"|" + alpha +"|" + umlaufdauer+"\n")
else:
    print("\n"+"Fehler: [Umlaufdauer unmöglich!]"+"\n"+"-------------------------------"+"\n"+"Daten wurden nicht gespeichert!"+"\n"+"Auf Wiedersehen!")

wb = Workbook()
ws = wb.active
ws.title = "Data"

ws.append(["Zeitdifferenz", "Rho", "Höhe", "Pos. von Mittelachse (r1)", "Pos. von Mittelachse (r2)", "Breitengrad", "Winkel", "Sonnenrotation"])


with open('Res/Sonnenrotationexcel.txt', 'r') as f:
        for line in f.readlines():
           data = line.strip()
           wert = data.split("|")
           ws.append(wert)



wb.save("Sonnenflecken-Daten.xlsx")
print("")
print("Daten wurden in Excel gespeichert")
print("")
