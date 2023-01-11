import pygame
import sys
from pygame.locals import *

pygame.init()

#Ansichtsfenster
HEIGHT = 1000
WIDTH = 1700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parkplatz zeichnen.")

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

#positionirung der Parkplätze
def Asphalt():
    asphalt = []
    w, h = Parkinglot()
    if ANZY == 1:
        for  n1 in range(ANZY):
            y = o + n1 + (h + DISTANCEY) + 235
            for m1 in range(ANZX):
                x = l + m1 * (w + DISTANCEX)
                r = Rect(x, y, w, h)
                asphalt.append(r)
    if ANZY == 2:
        for n in range(ANZY):
            y = o + n * (h + DISTANCEY) + 295
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX)
                r = Rect(x, y, w, h)
                asphalt.append(r)
    if ANZY == 4 or ANZY == 3:
        for n in range(ANZY):
            y = o + n * (h + DISTANCEY) + 80
            for m in range(ANZX):
                x = l + m * (w + DISTANCEX)
                r = Rect(x, y, w, h)
                asphalt.append(r)


    return asphalt