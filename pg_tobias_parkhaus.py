import random
import time
x = 0
q = 0
pcount = 10                                     #Parkplatzanzahl
timeh = 0                                       #aktuelle h
timem = 0                                       #aktuelle min
timed = 0                                       #aktueller Tag
timefactor = 0.01                               #Zeitbeschleunigungsfaktor
maxpark = 30                                    #maximale Parkzeit
minpark = 1                                     #minimale Parkzeit
lpark = []                                      #leere Parkplätze
cars = []                                       #Autos



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

    if timem % 1440 == 0:
        timeh = 0
        timed += 1

    print(f"d:{timed} h:{timeh} m:{timem}")




    y = random.randint(0,100)                                   #Ob Auto erstellt wird, wird ausgewürfelt

    if len(lpark) != 0:
        if 0 == y%2 and 6 < timeh < 10:                         # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Vormittag)
            x = x + 1
            pplace = lpark[random.randrange(0, len(lpark), 1)]  # Parkplatznummer wird festgelegt
            lpark.remove(pplace)

            ptime = random.randrange(minpark, maxpark, 1)       # Parkdauer wird festgelegt

            cars.append([x, pplace, timem, timem + ptime, ptime]) # [Autonr. , parplatzNr. , Parkzeit Start, Parkzeit Ende, Dauer Parken]

        if 0 == y%2 and timeh < 6 or timeh > 10:                                            # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Rest der Zeit)
            x = x + 1
            pplace = lpark[random.randrange(0, len(lpark), 1)]  # Parkplatznummer wird festgelegt
            lpark.remove(pplace)

            ptime = random.randrange(minpark, maxpark, 1)  # Parkdauer wird festgelegt

            cars.append([x, pplace, timem, timem + ptime, ptime]) # [Autonr. , parplatzNr. , Parkzeit Start, Parkzeit Ende, Dauer Parken]




    while q < len(cars) and cars !=[]:  # Parkdauer wird runtergezählt (für jedes Auto in liste cars)
        codw = cars[q][4]
        codw = codw - 1
        cars[q][4] = codw
        if codw == 0:                           # Autos (Listen) in cars werden auf abgelaufene Parkzeiten überprüft
                                                # und wenn 0 dann aus cars entfernt und Parkplatznr. wird wieder in leere Parkplätze zurückgegeben.
            lpark.append(cars[q][1])
            cars.remove(cars[q])
        q = q+1
        codw = 0
    q = 0



    print(cars)
    print(lpark)
    print(f"lencars: {len(cars)}")
    print(f"lpark: {len(lpark)}")