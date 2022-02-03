import matplotlib.pyplot as plt


["Zeitdifferenz", "Rho", "Höhe", "Pos. von Mittelachse", "Breitengrad", "Winkel", "Sonnenrotation"]

x_breitengrad = []
y_rotation = []

with open('Res/Sonnenrotation.txt', 'r') as f:
        for line in f.readlines():
           data = line.strip()
           Zeitdifferenz, Rho, Höhe, Pos_von_Mittelachse, Breitengrad, alpha, Sonnenrotation = data.split("|")
           x_breitengrad.append(Breitengrad)
           y_rotation.append(Sonnenrotation)

for i in range(0, len(y_rotation)):
    y_rotation[i] = float(y_rotation[i])

for i in range(0, len(x_breitengrad)):
    x_breitengrad[i] = float(x_breitengrad[i])

# print(x_breitengrad)
# print(y_rotation)



plt.xlabel("Breitengrad")
plt.ylabel("Rotationsperiode in Tagen")
plt.title("Differentielle Rotation der Sonne")

plt.plot(x_breitengrad,y_rotation)         #linie chart
plt.scatter(x_breitengrad,y_rotation)      #punkte chart
plt.axis([-40, 40, 0, 30])                 #xy,xy
plt.grid(True)                             #Gitter
plt.show()
