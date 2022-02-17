import matplotlib.pyplot as plt
from numpy import average


# ["Zeitdifferenz", "Rho", "Höhe", "Pos. von Mittelachse", "Breitengrad", "Winkel", "Sonnenrotation"]

# x_breitengrad = []
# y_rotation = []

# with open('Res/Sonnenrotation.txt', 'r') as f:
#         for line in f.readlines():
#            data = line.strip()
#            Zeitdifferenz, Rho, Höhe, r1, r2, Breitengrad, alpha, Sonnenrotation = data.split("|")
#            x_breitengrad.append(Breitengrad)
#            y_rotation.append(Sonnenrotation)

# for i in range(0, len(y_rotation)):
#     y_rotation[i] = float(y_rotation[i])

# for i in range(0, len(x_breitengrad)):
#     x_breitengrad[i] = float(x_breitengrad[i])

# x_breitengrad = sorted(x_breitengrad)
# y_rotation = sorted(y_rotation)


# plt.xlabel("Breitengrad")
# plt.ylabel("Rotationsperiode in Tagen")
# plt.title("Differentielle Rotation der Sonne")

# plt.plot(x_breitengrad,y_rotation)         #linie chart
# plt.scatter(x_breitengrad,y_rotation)      #punkte chart
# plt.axis([-40, 40, 24, 36])                 #xy,xy
# plt.grid(True)                             #Gitter
# plt.show()



#--------------------------------------------------------
try:
    x_breitengrad = []
    y_rotation = []
    dateipfad = 'Res/Sonnenrotation.txt'
    with open(dateipfad, 'r') as f:
            for line in f.readlines():
                data = line.strip()
                Zeitdifferenz, Rho, Höhe, r1, r2, Breitengrad, alpha, Sonnenrotation = data.split("|")
                x_breitengrad.append(Breitengrad)
                y_rotation.append(Sonnenrotation)

    for i in range(0, len(y_rotation)):
        y_rotation[i] = float(y_rotation[i])

    for i in range(0, len(x_breitengrad)):
        x_breitengrad[i] = abs(float(x_breitengrad[i]))

    x_breitengrad = sorted(x_breitengrad)
    y_rotation = sorted(y_rotation)
    länge = len(x_breitengrad)
    durchschnitt = round(average(y_rotation), 1)

    plt.xlabel("Breitengrad")
    plt.ylabel("Rotationsperiode in Tagen")

    plt.title(  "Differentielle Rotation der Sonne"
                +"\n"+"\n" +
                f"Insgesamt: {länge} Sonnenflecken | Durchschnitt: {durchschnitt} Tage")

    plt.plot(x_breitengrad,y_rotation)         #l| inie chart
    plt.scatter(x_breitengrad,y_rotation)      #punkte chart
    plt.axis([0, 90, 24, 36])                  #xy,xy
    plt.grid(True)                             #Gitter
    plt.show()

except FileNotFoundError:
    print("\n"+f"Keine Detei gefunden mit dem Dateipfad: {dateipfad}")
