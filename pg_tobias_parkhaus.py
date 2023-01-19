import random
import time
carnr = 0
q = 0
pcount = 10                                     #Parkplatzanzahl
timeh = 0                                       #aktuelle h
timem = 0                                       #aktuelle min
timed = 0                                       #aktueller Tag
inp_velocity = 1000                             #Zeitbeschleunigungsfaktor
maxpark = 30                                    #maximale Parkzeit
minpark = 1                                     #minimale Parkzeit
lpark = []                                      #leere Parkplätze
cars = []                                       #Autos
pplace = 0
dhm = [0,0,0]
hparked = 0

def createcar (dhm,lpark,cars,carnr):

    timed = dhm [0]
    timeh = dhm [1]
    timem = dhm [2]

    pplace = lpark[random.randrange(0, len(lpark), 1)]  # Parkplatznummer wird festgelegt
    lpark.remove(pplace)

    ptime = random.randrange(minpark, maxpark, 1)  # Parkdauer wird festgelegt

    # random auslosung der farbe
    carrand = ["Car_green","Car_red","Car_pink","Car_blue","Car_gray"]
    carco = random.choice(carrand)

    car = [carnr, pplace, timem, timem + ptime,ptime,carco]  # [Autonr. , parplatzNr. , Parkzeit Start, Parkzeit Ende, Dauer Parken]
    cars.append(car)


    return cars,lpark

def clock (timefactor,dhm):

    timed = dhm [0]
    timeh = dhm [1]
    timem = dhm [2]

    time.sleep(1/inp_velocity)
    timem += 1
    if timem%60 == 0:
        timeh += 1

    print(timem)

    if timem % 1440 == 0:
        timeh = 0
        timed += 1

    dhm = [timed,timeh,timem]
    return(dhm)




for o in range (pcount):    #Liste mit leeren Parkplätzen wird erstellt
    lpark.append(pcount-o)
lpark.reverse()
print(lpark)

for c in range (2000):
    dhm = clock(inp_velocity,dhm)



    if len(lpark) != 0:

        probcar = random.randint(0, 100)                              # Ob Auto erstellt wird, wird ausgewürfelt
        carnr = carnr+1                                                 # AutoNr. wird hochgezählt
        if carnr >= 500:
            carnr = 0

        if 0 == probcar%2 and 6 < timeh < 10:                         # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Vormittag)
           cars, lpark = createcar(dhm,lpark,cars,carnr)

        if 0 == probcar%2 and timeh < 6 or timeh > 10:                # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Rest der Zeit)
            cars, lpark = createcar(dhm,lpark,cars,carnr)






    while q < len(cars) and cars !=[]:  # Parkdauer wird runtergezählt (für jedes Auto in liste cars)
        codw = cars[q][4]
        codw = codw - 1
        cars[q][4] = codw
        if codw == 0:                           # Autos (Listen) in cars werden auf abgelaufene Parkzeiten überprüft
                                                # und wenn 0 dann aus cars entfernt und Parkplatznr. wird wieder in leere Parkplätze zurückgegeben.
            hparked = cars[q][3] - cars[q][2]
            hparked = hparked/60
            hparked = int(hparked)+1
            lpark.append(cars[q][1])
            cars.remove(cars[q])
            print(f"hparked {hparked}")
                                                #Umsatz wird hier berechnet
        q = q+1
        codw = 0
    q = 0


    print(cars)
    print(lpark)
    print(f"lencars: {len(cars)}")
    print(f"lpark: {len(lpark)}")

    timed = dhm [0]
    timeh = dhm [1]
    timem = dhm [2]
    print(f"d:{timed} h:{timeh} m:{timem}")