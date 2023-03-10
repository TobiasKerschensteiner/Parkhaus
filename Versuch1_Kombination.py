# Maindatei für Parkhaus

import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

import pygame
import sys

from pygame import Rect

pygame.init()

global cars
cars = []  # aktuelle Autos(global)

def Settings():

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1700, 1000))
    pygame.display.set_caption("Einstellungen")
    FONT = pygame.font.Font(None, 32)

    # Leere Textfelder
    text_rows = "4"
    text_columns = "5"
    text_price = "1.5"
    text_velocity = "0.5"
    text_start = "    Start    "
    text_stop = "Beenden"
    text_impressum = "Impressum"

    # Variablen für Farbe
    color_text = (255, 255, 255)
    color_text_s = (0, 255, 0)
    color_text_sp = (255, 0, 0)
    color_active = pygame.Color("white")
    color_inactive = pygame.Color("lightskyblue3")

    color_active_r = color_active
    color_inactive_r = color_inactive
    #color_r = color_inactive_r

    color_active_c = color_active
    color_inactive_c = color_inactive
    #color_c = color_inactive_c

    color_active_p = color_active
    color_inactive_p = color_inactive
    #color_p = color_inactive_p

    color_active_v = color_active
    color_inactive_v = color_inactive
    #color_v = color_inactive_v

    color_active_s = color_text_s
    color_inactive_s = color_inactive
    #color_s = color_inactive_s

    color_active_sp = color_text_sp
    color_inactive_sp = color_inactive
    #color_sp = color_inactive_sp

    color_active_i = color_active
    color_inactive_i = color_inactive
    #color_i = color_inactive_i

    # Variablen zum Aktivieren der einzelnen Textfelder
    active_rows = False
    active_columns = False
    active_price = False
    active_velocity = False
    active_start = False
    active_stop = False
    active_impressum = False

    # Koordinaten der Eingabefelder
    input_rows = pygame.Rect(100, 100, 140, 32)
    input_columns = pygame.Rect(100, 200, 140, 32)
    input_price = pygame.Rect(100, 300, 140, 32)
    input_velocity = pygame.Rect(100, 400, 140, 32)
    button_start = pygame.Rect(100, 475, 60, 32)
    button_stop = pygame.Rect(240, 475, 60, 32)
    button_impressum = pygame.Rect(100, 550, 60, 32)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mauserkennung der einzelnen Felder
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rows.collidepoint(event.pos):
                    active_rows = True
                else:
                    active_rows = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_columns.collidepoint(event.pos):
                    active_columns = True
                else:
                    active_columns = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_price.collidepoint(event.pos):
                    active_price = True
                else:
                    active_price = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_velocity.collidepoint(event.pos):
                    active_velocity = True
                else:
                    active_velocity = False

            # Mauserkennung der Knöpfe
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos):
                    active_start = True
                    # Wenn Start gedrückt wird, werden alle Werte eingegeben
                    inp_rows = int(text_rows)
                    print(inp_rows)
                    inp_columns = int(text_columns)
                    print(inp_columns)
                    inp_price = float(text_price)
                    print(inp_price)
                    inp_velocity = float(text_velocity)
                    print(inp_velocity)
                    global settings
                    settings = [inp_rows, inp_columns, inp_price, inp_velocity]
                    Simulation(settings)
                    return settings


                elif button_stop.collidepoint(event.pos):  # Startknopf leuchtet, bis Simulation beendet wird
                    active_start = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_stop.collidepoint(event.pos):
                    active_stop = True
                else:
                    active_stop = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_impressum.collidepoint(event.pos):
                    active_impressum = True
                else:
                    active_impressum = False

            # Tastaturerkennung und Texteingabe
            if event.type == pygame.KEYDOWN:
                if active_rows == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_rows = text_rows[:-1]
                    elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                       pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        text_rows += event.unicode  # Es können nur zahlen eingegeben werden

                    if event.key == pygame.K_RETURN:
                        inp_rows = int(text_rows) # Speichert die Eingabe
                        print(inp_rows)
                        # text_rows = "" (löscht das Textfeld)

            if event.type == pygame.KEYDOWN:
                if active_columns == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_columns = text_columns[:-1]
                    elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                       pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        text_columns += event.unicode

                    if event.key == pygame.K_RETURN:
                        inp_columns = int(text_columns)
                        print(inp_columns)
                        # text_columns = ""

            if event.type == pygame.KEYDOWN:
                if active_price == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_price = text_price[:-1]
                    elif event.key in [pygame.K_PERIOD, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                       pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        text_price += event.unicode  # Es können nur Zahlen und Punkte eingegeben werden

                    if event.key == pygame.K_RETURN:
                        inp_price = float(text_price)
                        print(inp_price)
                        # text_price = ""

            if event.type == pygame.KEYDOWN:
                if active_velocity == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_velocity = text_velocity[:-1]
                    elif event.key in [pygame.K_PERIOD, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                       pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        text_velocity += event.unicode

                    if event.key == pygame.K_RETURN:
                        inp_velocity = float(text_velocity)
                        print(inp_velocity)
                        # text_velocity = ""

        # Farbe des Hintergrunds
        screen.fill((102, 179, 255))

        # Wechselt die Farbe des Eingabefeldes bei Aktivierung
        if active_rows:
            color_r = color_active_r
        else:
            color_r = color_inactive_r

        if active_columns:
            color_c = color_active_c
        else:
            color_c = color_inactive_c

        if active_price:
            color_p = color_active_p
        else:
            color_p = color_inactive_p

        if active_velocity:
            color_v = color_active_v
        else:
            color_v = color_inactive_v

        if active_start:
            color_s = color_active_s
        else:
            color_s = color_inactive_s

        if active_stop:
            color_sp = color_active_sp
        else:
            color_sp = color_inactive_sp

        if active_impressum:
            color_i = color_active_i
        else:
            color_i = color_inactive_i

        # Zeichnen der Eingabefelder
        pygame.draw.rect(screen, color_r, input_rows, 2)
        pygame.draw.rect(screen, color_c, input_columns, 2)
        pygame.draw.rect(screen, color_p, input_price, 2)
        pygame.draw.rect(screen, color_v, input_velocity, 2)
        pygame.draw.rect(screen, color_s, button_start, 2)
        pygame.draw.rect(screen, color_sp, button_stop, 2)
        pygame.draw.rect(screen, color_i, button_impressum, 2)

        # Text wird "gerendert"
        text_surface_r = FONT.render(text_rows, True, color_text)
        text_surface_c = FONT.render(text_columns, True, color_text)
        text_surface_p = FONT.render(text_price, True, color_text)
        text_surface_v = FONT.render(text_velocity, True, color_text)
        text_surface_s = FONT.render(text_start, True, color_text_s)
        text_surface_sp = FONT.render(text_stop, True, color_text_sp)
        text_surface_i = FONT.render(text_impressum, True, color_text)

        # Anpassung des Textes an das Textfeld
        screen.blit(text_surface_r, (input_rows.x + 5, input_rows.y + 5))
        screen.blit(text_surface_c, (input_columns.x + 5, input_columns.y + 5))
        screen.blit(text_surface_p, (input_price.x + 5, input_price.y + 5))
        screen.blit(text_surface_v, (input_velocity.x + 5, input_velocity.y + 5))
        screen.blit(text_surface_s, (button_start.x + 5, button_start.y + 5))
        screen.blit(text_surface_sp, (button_stop.x + 5, button_stop.y + 5))
        screen.blit(text_surface_i, (button_impressum.x + 5, button_impressum.y + 5))

        # Anpassung der Weite der Textfelder
        input_rows.w = max(150, text_surface_r.get_width() + 10)
        input_columns.w = max(150, text_surface_c.get_width() + 10)
        input_price.w = max(150, text_surface_p.get_width() + 10)
        input_velocity.w = max(150, text_surface_v.get_width() + 10)
        button_start.w = max(60, text_surface_s.get_width() + 10)
        button_stop.w = max(60, text_surface_sp.get_width() + 10)
        button_impressum.w = max(60, text_surface_i.get_width() + 10)

        # Text über den Textfeldern
        FONT_cap = pygame.font.Font(None, 26)

        text_rows_cap = FONT_cap.render("Anzahl der Reihen:", True, color_text)
        screen.blit(text_rows_cap, (100, 75))
        text_columns_cap = FONT_cap.render("Anzahl der Spalten:", True, color_text)
        screen.blit(text_columns_cap, (100, 175))
        text_price_cap = FONT_cap.render("Preis pro Stunde in €:", True, color_text)
        screen.blit(text_price_cap, (100, 275))
        text_velocity_cap = FONT_cap.render("Geschwindigkeit der Simulation:", True, color_text)
        screen.blit(text_velocity_cap, (100, 375))

        # Programm wird aktualisiert
        pygame.display.flip()
        clock.tick(30)

def Simulation(settings,):

    inp_velocity = settings[3]
    lpark = []  # leere Parkplaetze

    # Ansichtsfenster
    HEIGHT = 1000
    WIDTH = 1700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Parkplatz Simulation.")

    # Farben
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

    # Bild Ampel einfügen
    GOO = pygame.image.load("bilder/Ampel Gruen.png")
    GOO_rect = GOO.get_rect()
    GOO_rect.center = (60, 310)
    STOOP = pygame.image.load("bilder/Ampel Rot.png")
    STOOP_rect = STOOP.get_rect()
    STOOP_rect.center = (60, 310)

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

    # schranke
    barrier = pygame.Rect(25, 170, 5, 5)
    barrier_r = pygame.Rect(25, 80, 5, 95)

    # Menüleiste (platzhalter)
    x4 = 0
    y4 = 0
    h4 = 70
    b4 = 1700
    menubar = pygame.Rect(x4, y4, b4, h4)
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
    menubar3 = pygame.Rect(x6 + 421, y6, b6, h6)
    menubar4 = pygame.Rect(x6 + 842, y6, b6, h6)

    # Asphalt
    x0 = 50
    y0 = 85
    h0 = 900
    b0 = 1640
    asphalt = pygame.Rect(x0, y0, b0, h0)

    # Parkplatz
    ANZX = settings[1]  # Anzahl x koordinate
    ANZY = settings[0]  # Anzahl y koordinate
    DISTANCEY1 = -2
    ANZPAR = ANZY * ANZX  # parkplatz gesamt

    # Tobias Definitionen
    carnr = 0
    pcount = ANZX * ANZY  # Parkplatzanzahl
    timeh = 0  # aktuelle h
    timem = 0  # aktuelle min
    timed = 0  # aktueller Tag
    hparked = 0
    dhm = [0, 0, 0, 0]

    # Celine Definitionen
    parklot = Rect(0, 0, 0, 0)
    font = pygame.font.SysFont(None, 50)
    drawText = False

    # Felix Definitionen
    sumo = 0

    for o in range(pcount):  # Liste mit leeren Parkplätzen wird erstellt
        lpark.append(pcount - o)

    koordinate = {}
    aph = Asphalt(settings)
    for c in range(len(aph)):
        for cd in range(1):
            xy = [aph[c][0], aph[c][1]]
            c = c+1
            koordinate [c]=xy

    print(koordinate) #x und y koordinaten als dic mit parkplatznummer

    textsize = Parkingnr()

    while True:
        dhm = clock(inp_velocity,dhm)

        if len(lpark) != 0:
            probcar = random.randint(0, 100)  # Ob Auto erstellt wird, wird ausgewürfelt
            carnr = carnr + 1  # AutoNr. wird hochgezählt

            if 0 == probcar % 2 and 6 < timeh < 10:  # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Vormittag)
                lpark = createcar(dhm, lpark, carnr)

            if 0 == probcar % 2 and timeh < 6 or timeh > 10:  # Zeit und Wahrscheinlichkeit für erstellen eines Autos wird bestimmt (Rest der Zeit)
                lpark = createcar(dhm, lpark, carnr)



        sumo, lpark = ptimecd_remvcar(settings[2],sumo,lpark)


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



        text_day = font_output.render(f"Tag: {day}", True, (255, 255, 255))
        screen.blit(text_day, (10, 10))
        text_time = font_output.render(f"Stunden: {hour}", True, (255, 255, 255))
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
        print(f"lencars: {len(cars)}")
        print(f"lpark: {len(lpark)}")
        print("--------------------------------------------------------")

def createcar (dhm,lpark,carnr,):
    maxpark = 300  # maximale Parkzeit
    minpark = 30  # minimale Parkzeit
    #pplace = 0
    Car_gray = pygame.image.load("bilder/Auto/Auto grau.png")
    Car_green = pygame.image.load("bilder/Auto/Auto grün.png")
    Car_red = pygame.image.load("bilder/Auto/Auto rot.png")
    Car_pink = pygame.image.load("bilder/Auto/Auto Pink .png")
    Car_blue = pygame.image.load("bilder/Auto/Auto blau.png")

    timem = dhm [2]

    pplace = lpark[random.randrange(0, len(lpark), 1)]  # Parkplatznummer wird festgelegt
    lpark.remove(pplace)

    ptime = random.randrange(minpark, maxpark, 1)  # Parkdauer wird festgelegt

    # random auslosung der farbe
    carrand = [Car_green,Car_red,Car_pink,Car_blue,Car_gray]
    carco = random.choice(carrand)

    car = [carnr, pplace, timem, timem + ptime,ptime,carco]  # [Autonr. , parplatzNr. , Parkzeit Start, Parkzeit Ende, Dauer Parken Rest, Autofarbe]
    cars.append(car)

def clock (settings,dhm):

    timed = dhm [0]
    timeh = dhm [1]
    timem = dhm [2]
    inp_velocity = settings


    time.sleep(1/inp_velocity)
    timem += 1

    if timem%60 == 0:
        timeh += 1

    if timem % 1440 == 0:
        timeh = 0
        timed += 1

    dhm = [timed,timeh,timem]
    return(dhm)

def ptimecd_remvcar(inp_price,sumo,lpark):
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
    return sumo, lpark

def Asphalt(settings):
    l = 150
    o = 100
    DISTANCEX = -2
    DISTANCEY = 100
    ANZX = settings[1]
    ANZY = settings[0]
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

#def main():

Settings()

Simulation(settings)

#---------------------------------------------------------------------------------------------------------------

#main()