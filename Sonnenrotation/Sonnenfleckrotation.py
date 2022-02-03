#---------------  Bilder auswählen  ------------------


Bild1 = 'Sonnenfleck1.1.jpg'
Bild2 = 'Sonnenfleck1.2.jpg'


#-----------------------------------------------------






import math
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, Button
import os
from pathlib import Path
from openpyxl import Workbook, load_workbook
from sympy import sign

my_ram_txt = Path('Res/Ram.txt')
if my_ram_txt.is_file():
    os.remove("Res/Ram.txt")



print("")
print("Kordinaten:")
print("---")



img = cv.imread(Bild1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)


img[dst>0.01*dst.max()]=[0,0,255]
# Punkte finden

cv.line(img,(35,512),(990,512),(0,255,255),1) #wagerecht
cv.line(img,(512,33),(512,990),(0,255,255),1) #senkrecht
# 2 Linien

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)


fig, ax = plt.subplots()
def onclick(event):
    x1, y1= event.xdata, event.ydata 

    x1 = int(x1)
    y1 = int(y1) 
    #print(x1,"|", y1)



    h = 512 - y1
     
    print(f"Höhe: {h}px")

    r1 = 512 - x1
    print(f"r1: {r1}px")
    # if r1 <= 0:
    #     r1 = abs(r1)
    # print(f"R1: {r1}px")






    with open('Res/Ram.txt', 'a') as f:
        f.write(str(h) + "|" + str(r1) + "|" + str(x1) + "|" + str(y1) +"\n")


fig.canvas.mpl_connect('button_press_event', onclick)
#click kordinaten

plt.title("EINEN Sonnenfleck auswählen und Fenster verlasen     (1/3)")
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()


#-------------------  Rho auswählen  -------------------

print("---")
img = cv.imread(Bild1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)


img[dst>0.01*dst.max()]=[0,0,255]
# Punkte finden

cv.line(img,(35,512),(990,512),(0,255,255),1) #wagerecht
cv.line(img,(512,33),(512,990),(0,255,255),1) #senkrecht
# 2 Linien

with open('Res/Ram.txt', 'r') as f:
        for line in f.readlines():
           data = line.strip()
           höhe, r_1, x_1, y_1= data.split("|")
        
        
        höhe = int(höhe)
        y_1 = int(y_1)
        cv.line(img,(35, y_1),(990, y_1),(0,255,255),1)



img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)


fig, ax = plt.subplots()
def onclick(event):
    x1, y1= event.xdata, event.ydata

    x1 = int(x1)
    y1 = int(y1) 
    #print(x1,"|", y1)



    Rho = 512 - x1
    if Rho <= 0:
        Rho = abs(Rho) 
    print(f"Rho: {Rho}px")

    with open('Res/Ram.txt', 'a') as f:
        f.write(str(Rho) + "|" + str(0) + "|" + str(0) + "|" + str(0) +"\n")


fig.canvas.mpl_connect('button_press_event', onclick)
#click kordinaten

plt.title("Rho auswählen und Fenster verlasen     (2/3)")
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()

#--------------------------------------------   Bild 2   -------------------------------------------
print("---")

img = cv.imread(Bild2)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)


img[dst>0.01*dst.max()]=[0,0,255]
# Punkte finden

cv.line(img,(35,512),(990,512),(0,255,255),1) #wagerecht
cv.line(img,(512,33),(512,990),(0,255,255),1) #senkrecht
# 2 Linien

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)


fig, ax = plt.subplots()
def onclick(event):
    x1, y1= event.xdata, event.ydata

    x1 = int(x1)
    y1 = int(y1) 
    #print(x1,"|", y1)


    r2 = 512 - x1
    print(f"r2: {r2}px")
    # if r2 <= 0:
    #     r2 = abs(r2)
    # print(f"R2: {r2}px")


    with open('Res/Ram.txt', 'a') as f:
        f.write(str(r2) + "|" + str(0) + "|" + str(0) + "|" + str(0) +"\n")


fig.canvas.mpl_connect('button_press_event', onclick)
#click kordinaten

plt.title("Gleichen rotierten Sonnenfleck auswählen und Fenster verlasen     (3/3)")
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()



#-------------------------------------------------------------------
ram_list = []

with open('Res/Ram.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            höhe, r_1, x_1, y_1= data.split("|")
            ram_list.append(höhe)
            ram_list.append(r_1)
            ram_list.append(x_1)
            ram_list.append(y_1)
        
        for x in range(6):
            ram_list.remove("0")

        #print(ram_list)
        # Liste besteht aus: h, r1, x1, y1, Rho, r2

h = ram_list[0]
r1 = ram_list[1]
Rho = ram_list[4]
r2 = ram_list[5]

os.remove("Res/Ram.txt")

with open('Res/Ram.txt', 'a') as f:
        f.write(str(h) + "|" + str(r1) + "|" + str(Rho) + "|" + str(r2) +"\n")




#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------



with open('Res/Ram.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            höhe, r_1, Rho, r_2= data.split("|")



inp_R = 478
inp_h = int(höhe)
inp_Rho = int(Rho)
inp_r1 = int(r_1)
inp_r2 = int(r_2)















print("-------------------------------")
print("Notwendige Eingaben:")
print("")

#inp_R = float(input("R in cm: "))
inp_t1 = input("t1: ")
inp_t2 = input("t2: ")
#inp_r1 = float(input("r1 in cm: "))
#inp_r2 = float(input("r2 in cm: "))
#inp_Rho = float(input("Rho in cm: "))
#inp_h = float(input("h in cm: "))


list_t1 = inp_t1.split()
 
list_t1 = list(map(float, list_t1))

year = list_t1[0]
mon = list_t1[1]
day = list_t1[2]
hour = list_t1[3]
min = list_t1[4]
sec = list_t1[5]

year= year*3153600
mon = mon*2592000
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

year2= year2*3153600
mon2 = mon2*2592000
day2 = day2*86400
hour2 = hour2*3600
min2 = min2*60

erg1 = year + mon + day + hour + min + sec
erg2 = year2 + mon2 + day2 + hour2 + min2 + sec2
total_time_sec = erg2 - erg1
total_time_day = total_time_sec/86400

print("-------------------------------")
print("Zwischenrechnungen:")
print("")


breitengrad = math.degrees(np.arcsin(inp_h/inp_R))
#breitengrad = 90.0 - breitengrad

sin_01 =  math.degrees(np.arcsin(inp_r1/inp_Rho))
sin_02 =  math.degrees(np.arcsin(inp_r2/inp_Rho))

#sin_01 = 90.0 - sin_01
#sin_02 = 90.0 - sin_02

if sign(sin_01) == sign(sin_02):
    alpha = sin_02 - sin_01
else:
    alpha = abs(sin_01) + abs(sin_02)

alpha = abs(alpha)

print(f"Sin 01: ~{round(sin_01, 2)}°")
print(f"Sin 02: ~{round(sin_02, 2)}°")
print(f"Alpha: ~{round(alpha, 2)}°")


p = ((2*math.pi)* total_time_day)/alpha

umlaufdauer = (360/alpha)*total_time_day

print("-------------------------------")
print("Ergebnisse:")
print("")

#print(f"Zeitdifferenz: {total_time_sec} Sekunden")


inp_r1 = str(inp_r1)
inp_r2 = str(inp_r2)
inp_Rho = str(inp_Rho)
inp_h = str(inp_h)
alpha = str(round(alpha, 2))
umlaufdauer = str(round(umlaufdauer, 2))
zeitdifferenz = str(round(total_time_day, 2))
breitengrad = str(round(breitengrad, 2))


print(f"Zeitdifferenz: ~{zeitdifferenz} Tage")

print(f"R: {inp_R}")
print(f"Rho: {inp_Rho}")
print(f"h: {inp_h}")
print(f"r1: {inp_r1}")
print(f"Breitengrad: {breitengrad}°")
print(f"überschrittene Winkel(Alpha): ~{alpha}°")
print("=======================================")
print(f"Sonenrotation: ~{umlaufdauer} Tage")
print("")
#^ = Reihnfolge

with open('Res/Sonnenrotationexcel.txt', 'a') as f:
    f.write(zeitdifferenz + " Tage"+ "|" + inp_Rho +"px"+ "|" + inp_h +"px"+ "|" + inp_r1 + "px"+"|"+ inp_r2 + "px"+"|" + breitengrad + "°"+ "|" + alpha + "°"+ "|" + umlaufdauer +" Tage"+"\n")
with open('Res/Sonnenrotation.txt', 'a') as f:
    f.write(zeitdifferenz + "|" + inp_Rho + "|" + inp_h + "|" + inp_r1 +"|"+ inp_r2 + "|" + breitengrad +"|" + alpha +"|" + umlaufdauer+"\n")
os.remove("Res/Ram.txt")


#--------------------------- Excel Tabelle ---------------------------



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
