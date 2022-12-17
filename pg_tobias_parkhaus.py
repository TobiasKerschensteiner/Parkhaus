import random
import time


pcount = 10                                     #Parkplatzanzahl
timeh = 0                                       #aktuelle h
timem = 0                                       #aktuelle min
timed = 1                                       #aktueller Tag
timefactor = 1                                  #Zeitbeschleunigungsfaktor
lpark = []

                                                #Parkdauer wird festgelegt
ptime = random.randrange(0,30,1)
print(ptime)


lcar = [ptime,0,0,0,0]                          #Liste mit Autodaten wird erstellt



pplace = random.randrange(0,pcount,1)           #Parkplatznummer wird festgelegt

for u in range (pcount):
        lpark.append(pcount-u-1)
        #lpark.reverse()
print(lpark)


for i in range (60):                          #Uhrzeit
        time.sleep(timefactor)
        timem += 1
        if timem == 60:
                timeh += 1
                timem = 0
        print(timem)

        if timeh == 24:
                timeh = 0
                timem = 0
                timed += 1

print(f"d:{timed} h:{timeh}")