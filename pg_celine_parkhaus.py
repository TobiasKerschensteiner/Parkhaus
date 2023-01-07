import pygame
import sys
from pygame.locals import *

pygame.init()
HEIGHT = 1000
WIDTH = 1700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parkplatz zeichnen.")
GRAY = (130, 130, 130)
GREENSPACE = (51, 112, 32)
MENUBAR = (123, 137, 229)
MENUBARX = (37, 57, 187)
TRAFFICLIGHT = (155, 17, 30)
WHITE = (255, 255, 255)
GO = (0, 255, 0)
STOP = (255, 0, 0)



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

# Ampel (Platzhalter)
x3 = 25
y3 = 172
h3 = 30
b3 = 20
trafficlight = pygame.Rect(x3, y3, b3, h3)

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
menubarx = pygame.Rect(x5, y5, b5, h5)
x6 = 421
y6 = 0
h6 = 70
b6 = 5
menubar2 = pygame.Rect(x6, y6, b6, h6)
menubar3 = pygame.Rect(x6+421, y6, b6, h6)
menubar4 = pygame.Rect(x6+842, y6, b6, h6)
#men = pygame.Rect(0, 500, b5, h5 )




#Asphalt
x0 = 50
y0 = 85
h0 = 900
b0 = 1640
asphalt = pygame.Rect(x0, y0, b0, h0)

#positionirung der Parkplätze
def Asphalt():
    asphalt = []
    w, h = Parkinglot()
    if ANZY == 1:
        for  n1 in range(ANZY):
            y = o + n1 + (h + DISTANCEY1) + 235
            for m1 in range(ANZX):
                x = l + m1 * (w + DISTANCEX)
                r = Rect(x, y, w, h)
                asphalt.append(r)
    if ANZY == 2:
        for n in range(ANZY):
            y = o + n * (h + DISTANCEY1) + 295
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX)
                r = Rect(x, y, w, h)
                asphalt.append(r)
    if ANZY == 4 or ANZY == 3:
        for n in range(ANZY):
            y = o + n * (h + DISTANCEY) + 110
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX)
                r = Rect(x, y, w, h)
                asphalt.append(r)


    return asphalt




#Parkplatz
l = 150
o = 100
ANZX = 30          #Anzahl x koordinate -> bekomme die einstell info von felix
ANZY = 2           #Anzahl y koordinate  -> bekomme die einstell info von felix
DISTANCEX = -2
DISTANCEY = 75
DISTANCEY1 = -2
def Parkinglot(): #Parkplatz größe
    w = 50
    h = 110
    return w, h

def Parkingnr():
    w, textsize = Parkinglot()
    return textsize




aph = Asphalt()
print(aph)
#color = (0, 0, 0)
parklot = Rect(0, 0, 0, 0)
textsize = Parkingnr()
font = pygame.font.SysFont(None, 50)


drawText = False
while True:
    screen.fill(GREENSPACE)
    pygame.draw.rect(screen, GRAY, asphalt)
    pygame.draw.rect(screen, GRAY, entrace)
    pygame.draw.rect(screen, GRAY, exit)
    pygame.draw.rect(screen, TRAFFICLIGHT, trafficlight)
    pygame.draw.rect(screen, MENUBAR, menubar)
    pygame.draw.rect(screen, MENUBARX, menubarx)
    pygame.draw.rect(screen, MENUBARX, menubar2)
    pygame.draw.rect(screen, MENUBARX, menubar3)
    pygame.draw.rect(screen, MENUBARX, menubar4)
    #pygame.draw.rect(screen,MENUBARX, men)


    for ele in aph:
        pygame.draw.rect(screen, WHITE, ele, 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEMOTION:
            for r in aph:
                if r.collidepoint(event.pos):
                    if parklot != r:
                        parklot = r
                        drawText = False
                    break

        elif event.type == MOUSEBUTTONUP:
            for num, r in enumerate(aph):
                if r.collidepoint(event.pos):
                    nrText = font.render(f"{num+1}", True, (0, 0, 0))
                    textRect = nrText.get_rect()
                    textRect.center = r.center

                    drawText = True

    pygame.draw.rect(screen, GO, parklot)
    if drawText:
        screen.blit(nrText, textRect)


    pygame.display.update()