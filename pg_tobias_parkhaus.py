import random
import time
carnr = 0

pcount = 10                                    #Parkplatzanzahl
timeh = 0                                       #aktuelle h
timem = 0                                       #aktuelle min
timed = 0                                       #aktueller Tag
inp_velocity = 1000                             #Zeitbeschleunigungsfaktor
maxpark = 30                                    #maximale Parkzeit
minpark = 1                                     #minimale Parkzeit
global lpark
lpark = []                                      #leere Parkplaetze
global cars
cars = []                                       #aktuelle Autos(global)
hparked = 0
dhm = [0, 0, 0]

def createcar (dhm,lpark,carnr):
    pplace = 0

    timed = dhm [0]
    timeh = dhm [1]
    timem = dhm [2]

    pplace = lpark[random.randrange(0, len(lpark), 1)]  # Parkplatznummer wird festgelegt
    lpark.remove(pplace)

    ptime = random.randrange(minpark, maxpark, 1)  # Parkdauer wird festgelegt

    # random auslosung der farbe
    carrand = ["Car_green","Car_red","Car_pink","Car_blue","Car_gray"]
    carco = random.choice(carrand)

    car = [carnr, pplace, timem, timem + ptime,ptime,carco]  # [Autonr. , parplatzNr. , Parkzeit Start, Parkzeit Ende, Dauer Parken Rest, Autofarbe]
    cars.append(car)


    return lpark

def clock (inp_velocity,dhm):

    timed = dhm [0]
    timeh = dhm [1]
    timem = dhm [2]

    time.sleep(1/inp_velocity)
    timem += 1
    if timem%60 == 0:
        timeh += 1

    if timem % 1440 == 0:
        timeh = 0
        timed += 1

    dhm = [timed,timeh,timem]
    return(dhm)

def ptimecd_remvcar():
    q = 0                               # Variable zum durcharbeiten von cars
    codw = 0                            # Hilfsvariable zum herunterzaehlen der restlichen Parkzeit
    hparked = 0                         # Stunden geparket in Stunden aufgerundet
    if cars !=[]:
        for q in range (len(cars)):  # Parkdauer wird runtergezählt (für jedes Auto in liste cars)
            if cars[q] != [0]:
                codw = cars[q][4]
                codw = codw - 1
                cars[q][4] = codw
                if codw == 0:                           # Autos (Listen) in cars werden auf abgelaufene Parkzeiten überprüft
                                                        # und wenn 0 dann aus cars entfernt und Parkplatznr. wird wieder in leere Parkplätze zurückgegeben.
                    hparked = cars[q][3] - cars[q][2]
                    hparked = hparked/60
                    hparked = int(hparked)+1
                    lpark.append(cars[q][1])            #gibt Parkplatznr als leer an Liste lpark zurück
                    cars[q] = [0]
                    print(f"hparked {hparked}")
                                                        #Umsatz wird hier berechnet
                codw = 0

        o = 0                                       #Variable zum drucharbeiten von cars
        while o < len(cars):
            if cars[o] == [0]:
                cars.remove(cars[o])
            o = o+1
        o = 0





for o in range (pcount):    #Liste mit leeren Parkplätzen wird erstellt
    lpark.append(pcount-o)
lpark.reverse()


for c in range (2000):
    dhm = clock(inp_velocity,dhm)


    if len(lpark) != 0:
        probcar = random.randint(0, 100)                              # Ob Auto erstellt wird, wird ausgewürfelt
        carnr = carnr+1                                                 # AutoNr. wird hochgezählt
        #if carnr >= 9999:                                            maybe max Autonumr.
        #    carnr = 0

        if 0 == probcar%2 and 6 < timeh < 10:                         # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Vormittag)
           lpark = createcar(dhm,lpark,carnr)

        if 0 == probcar%2 and timeh < 6 or timeh > 10:                # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Rest der Zeit)
            lpark = createcar(dhm,lpark,carnr)


    ptimecd_remvcar()



    timed = dhm [0]
    timeh = dhm [1]
    timem = dhm [2]
    print("--------------------------------------------------------")
    print(f"d:{timed} h:{timeh} m:{timem}")
    print(cars)
    print(lpark)
    print(f"lencars: {len(cars)}")
    print(f"lpark: {len(lpark)}")
    print("--------------------------------------------------------")

