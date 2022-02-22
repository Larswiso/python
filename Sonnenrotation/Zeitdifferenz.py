inp_t1 = input("t1: ")
inp_t2 = input("t2: ")

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

print(f"Zeitdifferenz: ~{total_time_day} Tage")
