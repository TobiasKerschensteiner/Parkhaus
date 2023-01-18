import pygame
import sys
from pygame.locals import *
import random

pygame.init()

#Ansichtsfenster
HEIGHT = 1000
WIDTH = 1700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parkplatz symulation.")

#Farben
GRAY = (130, 130, 130)
GREENSPACE = (51, 112, 32)
MENUBAR = (123, 137, 229)
MENUBARX = (37, 57, 187)
WHITE = (255, 255, 255)
GO = (0, 255, 0)
STOP = (255, 0, 0)

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
ANZX = 30         #Anzahl x koordinate -> bekomme die einstell info von felix
ANZY = 4           #Anzahl y koordinate  -> bekomme die einstell info von felix
DISTANCEX = -2
DISTANCEY = 100
DISTANCEY1 = -2
ANZPAR = ANZY * ANZX #parplatz gesamt


carnr = 27  # lückenfüller für die schaltung bekomme variable von Tobi max anzahl an autos




#positionirung der Parkplätze
def Asphalt():
    asphalt = []
    w, h = Parkinglot()
    if ANZY == 1:
        for n in range(ANZY):
            y = o + n + (h + DISTANCEY) + 235
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX) + 25
                r = Rect(x, y, w, h)
                r.center = (x, y)
                asphalt.append(r)

    if ANZY == 2:
        for n in range(ANZY):
            y = o + n * (h + DISTANCEY) + 295
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX) +25
                r = Rect(x, y, w, h)
                r.center = (x , y)
                asphalt.append(r)
    if ANZY == 4 or ANZY == 3:
        for n in range(ANZY):
            y = o + n * (h + DISTANCEY) + 135
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX) + 25
                r = Rect(x, y, w, h)
                r.center = (x,y)
                asphalt.append(r)


    return asphalt



def Parkinglot(): #Parkplatz größe
    w = 50
    h = 100
    return w, h
parking = Parkinglot()


def Parkingnr():
    w, textsize = Parkinglot()
    return textsize




koordinate = {}
aph = Asphalt()
for c in range(len(aph)):
    for cd in range(1):
        xy = [aph[c][0], aph[c][1]]
        c = c+1
        koordinate [c]=xy

print(koordinate) #x und y koordinaten als dic mit parkplatznummer



park = [1, 5]
for ue in range(len(park)):
    parkplatz2 = park[ue]
    cor = koordinate[parkplatz2]
    # xx = cor[0]
    # yy = cor[1]
    kord = [koordinate[parkplatz2][0], koordinate[parkplatz2][1]]
    print(koordinate[parkplatz2][0], koordinate[parkplatz2][1])


#Bild Auto einfügen
Car_blue = pygame.image.load("bilder/Auto/Auto blau.png")
Car_blue_rect = Car_blue.get_rect()
Car_blue_rect.center = (koordinate[parkplatz2][0]+25 , koordinate[parkplatz2][1]+50)
Car_pink = pygame.image.load("bilder/Auto/Auto Pink .png")
Car_pink_rect = Car_pink.get_rect()
Car_pink_rect.center = (koordinate[parkplatz2][0]+25 , koordinate[parkplatz2][1]+50)
Car_red = pygame.image.load("bilder/Auto/Auto rot.png")
Car_red_rect = Car_red.get_rect()
Car_red_rect.center = (koordinate[parkplatz2][0]+25 , koordinate[parkplatz2][1]+50)
Car_green = pygame.image.load("bilder/Auto/Auto grün.png")
Car_green_rect = Car_green.get_rect()
Car_green_rect.center = (koordinate[parkplatz2][0]+25 , koordinate[parkplatz2][1]+50)
Car_gray = pygame.image.load("bilder/Auto/Auto grau.png")
Car_gray_rect = Car_gray.get_rect()
Car_gray_rect.center = (koordinate[parkplatz2][0]+25 , koordinate[parkplatz2][1]+50)
#random auslosung der farbe
carrand = [Car_green, Car_red, Car_pink, Car_blue, Car_gray]
car_rect_rand = [Car_gray_rect, Car_green_rect, Car_red_rect, Car_pink_rect, Car_blue_rect]
car = random.choice(carrand)
car_rect = random.choice(car_rect_rand)




#print("Parkplatz 1 =",aph[0][0],",",aph[0][1])   # x und y koordinaten der prakplätze für tobi (links oben) für mitte/mitte x+25 y+50
parklot = Rect(0, 0, 0, 0)
textsize = Parkingnr()
font = pygame.font.SysFont(None, 50)

drawText = False
#aph = pygame.Rect(0,0,0,0)
#aph.center = (500, 500)

while True:
#einfügen der grafiken
    screen.fill(GREENSPACE)
    pygame.draw.rect(screen, GRAY, asphalt)
    pygame.draw.rect(screen, GRAY, entrace)
    pygame.draw.rect(screen, GRAY, exit)
    pygame.draw.rect(screen, MENUBAR, menubar)
    pygame.draw.rect(screen, MENUBARX, menubar1)
    pygame.draw.rect(screen, MENUBARX, menubar2)
    pygame.draw.rect(screen, MENUBARX, menubar3)
    pygame.draw.rect(screen, MENUBARX, menubar4)

    screen.blit(car, car_rect)




#Ampel
    if carnr > ANZPAR - 1:
        screen.blit(STOOP, STOOP_rect)
    else:
        screen.blit(GOO, GOO_rect)
#Schranke
    if carnr > ANZPAR - 1:
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
        elif event.type == MOUSEBUTTONUP:
            for num, p in enumerate(aph):
                if p.collidepoint(event.pos):
                    nrText = font.render(f"{num+1}", True, (0, 0, 0))
                    textRect = nrText.get_rect()
                    textRect.center = p.center


                    drawText = True

    #pygame.draw.rect(screen, GO, parklot) #parkplatz wird grün
    if drawText:
        screen.blit(nrText, textRect)




    pygame.display.update()