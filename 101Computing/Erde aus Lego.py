radius = 6371 #km
width = 16 #mm
length = 16 #mm
height = 10 #mm

radius = radius * 1000000

print("Die Erde hat ein Radius von: " + str(radius)+ "mm")

planetEarth = 4*3.14*(radius*radius*radius)/3

print("Die Erde hat ein Volumen von: " + str(planetEarth)+ "mm")

legobrick = width*height*length

print("Ein Legostein hat ein Volumen von: " + str(legobrick)+ "mm")

numbersofbricks = planetEarth/legobrick

print("Es werden folgende Anzahl an Legosteinen benötigt um die Erde aus Legosteinen zu bauen: " + str(numbersofbricks))