import random
import time
q = 0
x = 0
pcount = 10                                     #Parkplatzanzahl
timeh = 0                                       #aktuelle h
timem = 0                                       #aktuelle min
timed = 0                                       #aktueller Tag
timefactor = 0.001                              #Zeitbeschleunigungsfaktor
lpark = []                                      #leere Parkplätze
cars = []



for o in range (pcount):    #Liste mit leeren Parkplätzen wird erstellt
    lpark.append(pcount-o)
lpark.reverse()
print(lpark)

for c in range (2000):
    time.sleep(timefactor)
    timem += 1
    if timem%60 == 0:
        timeh += 1

    print(timem)

    if timem == 1440:
        timeh = 0
        timed += 1

    print(f"d:{timed} h:{timeh} m:{timem}")




    y = random.randint(0,10) #Ob Auto erstellt wird, wird ausgewürfelt

    if 0 == y%2 and lpark != []:
            x = x + 1
            pplace = lpark[random.randrange(0, len(lpark), 1)]  # Parkplatznummer wird festgelegt
            lpark.remove(pplace)

            ptime = random.randrange(1, 30, 1)  # Parkdauer wird festgelegt

            cars.append([x, pplace, timem, timem + ptime, ptime]) # [Autonr. , parplatzNr. , Parkzeit Start, Parkzeit Ende, Dauer Parken]

    if cars != []:
        z = len(cars)-1
        while q <= z:  # Parkdauer wird runtergezählt (für jedes Auto in liste cars)
            q = q +1
            print(f"q: {q}")
            print(f"lencars: {len(cars)-1}")
            codw = cars[q][4]
            codw = codw - 1
            cars[q][4] = codw
            if codw == 0:
                lpark.append(cars[q][1])
                cars.remove(cars[q])
                z = len(cars)-1

            codw = 0
        q = 0





#for i in cars
#   cars[]
    print(cars)
    print(lpark)
