import pygame
import sys
from pygame.locals import *

pygame.init()
HEIGHT = 950
WIDTH = 1500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rechtecke zeichnen.")
GRAY = (130, 130, 130)
GREENSPACE = (51, 112, 32)
MENUBAR = (132, 195, 190)
TRAFFICLIGHT = (155, 17, 30)
WHITE = (255, 255, 255)
GO = (0, 255, 0)
STOOP = (255, 0, 0)



# Einfahrt
x1 = 0
y1 = 250
h1 = 120
b1 = 500
entrace = pygame.Rect(x1, y1, b1, h1)

# Ausfahrt
x2 = 0
y2 = 650
exit = pygame.Rect(x2, y2, b1, h1)

# Ampel (Platzhalter)
x3 = 70
y3 = 220
h3 = 30
b3 = 20
trafficlight = pygame.Rect(x3, y3, b3, h3)
#Menüleiste (platzhalter)
x4 = 0
y4 = 0
h4 = 70
b4 = 1500
menubar = pygame.Rect(x4, y4, b4, h4 )

#Asphalt
x0 = 90
y0 = 85
h0 = 850
b0 = 1400
asphalt = pygame.Rect(x0, y0, b0, h0)

#Parkfläche
def Asphalt():
    asphalt = []
    w, h = Parkinglot()
    for n in range(ANZY):
        y = o + n * (h + DISTANCEY) # unterre reihe + 700
        for m in range(ANZX):
            x = l + m * (w + DISTANCEX) + 100
            r = Rect(x, y, w, h)
            asphalt.append(r)
    return asphalt

#Parkplatz 1 oben
l = 150
o = 100
ANZX = 20           #Anzahl x koordinate
ANZY = 1           #Anzahl y koordinate
DISTANCEX = -2
DISTANCEY = 75
def Parkinglot():
    w = ((b0 - l * 2) // ANZX) - DISTANCEX
    h = ((h0 - 325 * 2) // ANZY) - DISTANCEY
    return w, h

def Parkingnr():
    w, textsize = Parkinglot()
    return textsize

aph = Asphalt()
print(aph)
#color = (0, 0, 0)
parklot = Rect(0, 0, 0, 0)
textsize = Parkingnr()
font = pygame.font.SysFont(None, textsize)


drawText = False
while True:
    screen.fill(GREENSPACE)
    pygame.draw.rect(screen, GRAY, asphalt)
    pygame.draw.rect(screen, GRAY, entrace)
    pygame.draw.rect(screen, GRAY, exit)
    pygame.draw.rect(screen, TRAFFICLIGHT, trafficlight)
    pygame.draw.rect(screen, MENUBAR, menubar)

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
                    nrText = font.render(f"{num}", True, (0, 0, 0))
                    textRect = nrText.get_rect()
                    textRect.center = r.center

                    drawText = True

    pygame.draw.rect(screen, GO, parklot)
    if drawText:
        screen.blit(nrText, textRect)


    pygame.display.update()

