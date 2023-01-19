import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Einstellungen")
FONT = pygame.font.Font(None, 32)

# def func_impressum():

    # font_impressum_menu = pygame.font.Font(None, 45)

    # screen.fill((102, 179, 255))

    # text_impressum_menu = font_impressum_menu.render


#def func_input():

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
                inp_rows = [int(text_rows)]
                print(inp_rows)
                inp_columns = [int(text_columns)]
                print(inp_columns)
                inp_price = [float(text_price)]
                print(inp_price)
                inp_velocity = [float(text_velocity)]
                print(inp_velocity)

            elif button_stop.collidepoint(event.pos):  # Startknopft leuchtet, bis Simulation beendet wird
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
                    inp_rows = [int(text_rows)] # Speichert die Eingabe
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
                    inp_columns = [int(text_columns)]
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
                    inp_price = [float(text_price)]
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
                    inp_velocity = [float(text_velocity)]
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