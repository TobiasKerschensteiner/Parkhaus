# Maindatei für Parkhaus

import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

#Ansichtsfenster
HEIGHT = 1000
WIDTH = 1700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parkplatz Simulation.")

#Farben
GRAY = (130, 130, 130)
GREENSPACE = (51, 112, 32)
MENUBAR = (123, 137, 229)
MENUBARX = (37, 57, 187)
WHITE = (255, 255, 255)
GO = (0, 255, 0)
STOP = (255, 0, 0)

Car_gray = pygame.image.load("bilder/Auto/Auto grau.png")
Car_green = pygame.image.load("bilder/Auto/Auto grün.png")
Car_red = pygame.image.load("bilder/Auto/Auto rot.png")
Car_pink = pygame.image.load("bilder/Auto/Auto Pink .png")
Car_blue = pygame.image.load("bilder/Auto/Auto blau.png")

#Bild Ampel einfügen
GOO = pygame.image.load("bilder/Ampel Gruen.png")
GOO_rect = GOO.get_rect()
GOO_rect.center = (60, 310)
STOOP = pygame.image.load("bilder/Ampel Rot.png")
STOOP_rect = STOOP.get_rect()
STOOP_rect.center = (60,310)


# Einfahrt
x1 = 0
y1 = 85
h1 = 80
b1 = 100
entrace = pygame.Rect(x1, y1, b1, h1)

# Ausfahrt
x2 = 0
y2 = 905
exit = pygame.Rect(x2, y2, b1, h1)

#schranke
barrier = pygame.Rect(25, 170, 5, 5)
barrier_r = pygame.Rect(25, 80, 5, 95)

#Menüleiste (platzhalter)
x4 = 0
y4 = 0
h4 = 70
b4 = 1700
menubar = pygame.Rect(x4, y4, b4, h4 )
x5 = 0
y5 = 70
h5 = 5
b5 = 1700
menubar1 = pygame.Rect(x5, y5, b5, h5)
x6 = 421
y6 = 0
h6 = 70
b6 = 5
menubar2 = pygame.Rect(x6, y6, b6, h6)
menubar3 = pygame.Rect(x6+421, y6, b6, h6)
menubar4 = pygame.Rect(x6+842, y6, b6, h6)


#Asphalt
x0 = 50
y0 = 85
h0 = 900
b0 = 1640
asphalt = pygame.Rect(x0, y0, b0, h0)

#Parkplatz
l = 150
o = 100
ANZX = 25         #Anzahl x koordinate -> bekomme die einstell info von felix
ANZY = 4           #Anzahl y koordinate  -> bekomme die einstell info von felix
DISTANCEX = -2
DISTANCEY = 100
DISTANCEY1 = -2
ANZPAR = ANZY * ANZX #parplatz gesamt

#Tobias Definitionen
carnr = 0
pcount = ANZX*ANZY                              #Parkplatzanzahl
timeh = 0                                       #aktuelle h
timem = 0                                       #aktuelle min
timed = 0                                       #aktueller Tag
inp_velocity = 10                               #Zeitbeschleunigungsfaktor
maxpark = 300                                   #maximale Parkzeit
minpark = 30                                     #minimale Parkzeit
global lpark
lpark = []                                      #leere Parkplaetze(global)
global cars
cars = []                                       #aktuelle Autos(global)
hparked = 0
dhm = [0, 0, 0]

#Celine Definitionen
parklot = Rect(0, 0, 0, 0)
font = pygame.font.SysFont(None, 50)
drawText = False

#Felix Definitionen
inp_price = 2
sumo = 10

def createcar (dhm,lpark,carnr):
    pplace = 0

    timed = dhm [0]
    timeh = dhm [1]
    timem = dhm [2]

    pplace = lpark[random.randrange(0, len(lpark), 1)]  # Parkplatznummer wird festgelegt
    lpark.remove(pplace)

    ptime = random.randrange(minpark, maxpark, 1)  # Parkdauer wird festgelegt

    # random auslosung der farbe
    carrand = [Car_green,Car_red,Car_pink,Car_blue,Car_gray]
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

def ptimecd_remvcar(inp_price,sumo):
    q = 0                               # Variable zum durcharbeiten von cars
    codw = 0                            # Hilfsvariable zum herunterzaehlen der restlichen Parkzeit
    hparked = 0                         # Stunden geparket in Stunden aufgerundet
    if cars !=[]:
        for q in range (len(cars)):     # Parkdauer wird runtergezählt (für jedes Auto in liste cars)
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
                    sumo = sumo + (hparked*inp_price)     #Umsatz wird hier berechnet
                    hparked = 0

                codw = 0

        o = 0                                           #Variable zum drucharbeiten von cars
        while o < len(cars):
            if cars[o] == [0]:
                cars.remove(cars[o])
                o = 0-1
            o = o+1
        o = 0
    return sumo

def Asphalt():
    asphalt = []
    w, h = Parkinglot()
    if ANZY == 1:
        for n in range(ANZY):
            y = o + n + (h + DISTANCEY) + 235
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX) + 150
                r = Rect(x, y, w, h)
                r.center = (x, y)
                asphalt.append(r)

    if ANZY == 2:
        for n in range(ANZY):
            y = o + n * (h + DISTANCEY) + 295
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX) + 150
                r = Rect(x, y, w, h)
                r.center = (x, y)
                asphalt.append(r)
    if ANZY == 4 or ANZY == 3:
        for n in range(ANZY):
            y = o + n * (h + DISTANCEY) + 135
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX) + 150
                r = Rect(x, y, w, h)
                r.center = (x, y)
                asphalt.append(r)

    return asphalt

def Parkinglot():  # Parkplatz größe
    w = 50
    h = 100
    return w, h

parking = Parkinglot()

def Parkingnr():
    w, textsize = Parkinglot()
    return textsize

#GAS GAS GAS -------------------------------------------------------------------------------------------

for o in range(pcount):  # Liste mit leeren Parkplätzen wird erstellt
    lpark.append(pcount - o)
lpark.reverse()

koordinate = {}
aph = Asphalt()
for c in range(len(aph)):
    for cd in range(1):
        xy = [aph[c][0], aph[c][1]]
        c = c+1
        koordinate [c]=xy

print(koordinate) #x und y koordinaten als dic mit parkplatznummer

textsize = Parkingnr()

while True:
    dhm = clock(inp_velocity, dhm)

    if len(lpark) != 0:
        probcar = random.randint(0, 100)  # Ob Auto erstellt wird, wird ausgewürfelt
        carnr = carnr + 1  # AutoNr. wird hochgezählt

        if 0 == probcar % 2 and 6 < timeh < 10:  # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Vormittag)
            lpark = createcar(dhm, lpark, carnr)

        if 0 == probcar % 2 and timeh < 6 or timeh > 10:  # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Rest der Zeit)
            lpark = createcar(dhm, lpark, carnr)

    sumo = ptimecd_remvcar(inp_price,sumo)


#Ausgabe Ausgabe Ausgabe Ausgabe Ausgabe Ausgabe Ausgabe

    screen.fill(GREENSPACE)
    pygame.draw.rect(screen, GRAY, asphalt)
    pygame.draw.rect(screen, GRAY, entrace)
    pygame.draw.rect(screen, GRAY, exit)
    pygame.draw.rect(screen, MENUBAR, menubar)
    pygame.draw.rect(screen, MENUBARX, menubar1)
    pygame.draw.rect(screen, MENUBARX, menubar2)
    pygame.draw.rect(screen, MENUBARX, menubar3)
    pygame.draw.rect(screen, MENUBARX, menubar4)




    pygame.draw.rect(screen, GO, parklot) #parkplatz wird grün

    for ue in range(len(cars)):
        parkplatz2 = cars[ue][1]
        cor = koordinate[parkplatz2]
        # xx = cor[0]
        # yy = cor[1]
        kord = [koordinate[parkplatz2][0], koordinate[parkplatz2][1]]

        # Bild Auto einfügen
        Car_blue_rect = Car_blue.get_rect()
        Car_blue_rect.center = (koordinate[parkplatz2][0] + 25, koordinate[parkplatz2][1] + 50)
        Car_pink_rect = Car_pink.get_rect()
        Car_pink_rect.center = (koordinate[parkplatz2][0] + 25, koordinate[parkplatz2][1] + 50)
        Car_red_rect = Car_red.get_rect()
        Car_red_rect.center = (koordinate[parkplatz2][0] + 25, koordinate[parkplatz2][1] + 50)
        Car_green_rect = Car_green.get_rect()
        Car_green_rect.center = (koordinate[parkplatz2][0] + 25, koordinate[parkplatz2][1] + 50)
        Car_gray_rect = Car_gray.get_rect()
        Car_gray_rect.center = (koordinate[parkplatz2][0] + 25, koordinate[parkplatz2][1] + 50)
        # random auslosung der farbe

        carrand = [Car_green, Car_red, Car_pink, Car_blue, Car_gray]
        car_rect_rand = [Car_gray_rect, Car_green_rect, Car_red_rect, Car_pink_rect, Car_blue_rect]

        car = random.choice(carrand)
        car_rect = random.choice(car_rect_rand)


        screen.blit(cars[ue][5], car_rect)
        print(koordinate[parkplatz2][0], koordinate[parkplatz2][1])



#Ampel
    if len(lpark) == 0:
        screen.blit(STOOP, STOOP_rect)
    else:
        screen.blit(GOO, GOO_rect)
#Schranke
    if len(lpark) == 0:
        pygame.draw.rect(screen, STOP, barrier_r)
    else:
        pygame.draw.rect(screen, STOP, barrier)

#Zeichnen Parkplätze
    for ele in aph:
        pygame.draw.rect(screen, WHITE, ele, 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        elif event.type == MOUSEMOTION:
            for p in aph:
                if p.collidepoint(event.pos):
                    if parklot != p:
                        parklot = p
                        drawText = False
                    break

# Anzeigen der Parkplatznummer
            for num, p in enumerate(aph):
                if p.collidepoint(event.pos):
                    nrText = font.render(f"{num + 1}", True, (0, 0, 0))
                    textRect = nrText.get_rect()
                    textRect.center = p.center
                    drawText = True

    font_output = pygame.font.Font(None, 32)

    # Anzeige für Tag und Uhrzeit
    day = dhm[0]
    hour = dhm[1]
    minute = dhm[2]

    text_day = font_output.render(f"Tag: {day}", True, (255, 255, 255))
    screen.blit(text_day, (10, 10))
    text_time = font_output.render(f"Uhrzeit: {hour}:{minute}", True, (255, 255, 255))
    screen.blit(text_time, (10, 40))

    # Anzeige für die belegten Parkplätze

    text_occupied = font_output.render(f"Belegte Parkplätze: {len(cars)}", True, (255, 255, 255))
    screen.blit(text_occupied, (435, 25))

    # Anzeige für die freien Parkplätze

    text_l_park = font_output.render(f"Freie Parkplätze: {len(lpark)}", True, (255, 255, 255))
    screen.blit(text_l_park, (855, 25))

    # Anzeige des Umsatzes

    text_turnover = font_output.render(f"Umsatz: {sumo}€", True, (255, 255, 255))
    screen.blit(text_turnover, (1275, 25))

    if drawText:
        screen.blit(nrText, textRect)

    pygame.display.update()

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