import pygame

HOEHE = 950
BREITE = 1500

GRAU = (211, 211, 211)
GRUENFLAECHE = (51, 112, 32)
MENUELEISTE = (132, 195, 190)
AMPEL = (155, 17, 30)
screen = pygame.display.set_mode((BREITE, HOEHE))

#Parkfläche
x = 90
y = 80
h = 860
b = 1400
asphalt = pygame.Rect(x, y, b, h)

# Einfahrt
x1 = 0
y1 = 200
h1 = 120
b1 = 500
einfahrt = pygame.Rect(x1, y1, b1, h1)

# Ausfahrt
x2 = 0
y2 = 700
ausfahrt = pygame.Rect(x2, y2, b1, h1)

# Ampel (Platzhalter)
x3 = 70
y3 = 170
h3 = 30
b3 = 20
ampel = pygame.Rect(x3, y3, b3, h3)
#Menüleiste (platzhalter)
x4 = 0
y4 = 0
h4 = 70
b4 = 1500
menueleiste = pygame.Rect(x4, y4, b4, h4 )





screen.fill(GRAU)

running = True

while running:
    screen.fill(GRUENFLAECHE)
    pygame.draw.rect(screen, GRAU, asphalt )
    pygame.draw.rect(screen,GRAU, einfahrt)
    pygame.draw.rect(screen, GRAU, ausfahrt)
    pygame.draw.rect(screen, AMPEL, ampel)
    pygame.draw.rect(screen, MENUELEISTE, menueleiste)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
