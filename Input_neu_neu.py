import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))
FONT = pygame.font.Font(None, 32)

# Leere Textfelder
text_rows = ""
text_columns = ""
text_price = ""
text_velocity = ""

# Variablen für Farbe
color_text = (255, 255, 255)

color_active_r = pygame.Color("lightskyblue3")
color_inactive_r = ("white")
color_r = color_inactive_r

color_active_c = pygame.Color("lightskyblue3")
color_inactive_c = ("white")
color_c = color_inactive_c

color_active_p = pygame.Color("lightskyblue3")
color_inactive_p = ("white")
color_p = color_inactive_p

color_active_v = pygame.Color("lightskyblue3")
color_inactive_v = ("white")
color_v = color_inactive_v

# Variablen zum Aktivieren der einzelnen Textfelder
active_rows = False
active_columns = False
active_price = False
active_velocity = False

# Koordinaten der Eingabefelder
input_rows = pygame.Rect(100, 100, 140, 32)
input_columns = pygame.Rect(100, 200, 140, 32)
input_price = pygame.Rect(100, 300, 140, 32)
input_velocity = pygame.Rect(100, 400, 140, 32)

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

        # Tastaturerkennung und Texteingabe
        if event.type == pygame.KEYDOWN:
            if active_rows == True:
                if event.key == pygame.K_BACKSPACE:
                    text_rows = text_rows[:-1]
                elif event.key is not pygame.K_RETURN: # Erkennt alle Tasten außer "Enter"
                    text_rows += event.unicode

                if event.key == pygame.K_RETURN:
                    print(text_rows)
                    inp_rows = text_rows # Speichert die Eingabe
                    #text_rows = "" (löscht das Textfeld)

        if event.type == pygame.KEYDOWN:
            if active_columns == True:
                if event.key == pygame.K_BACKSPACE:
                    text_columns = text_columns[:-1]
                elif event.key is not pygame.K_RETURN:
                    text_columns += event.unicode

                if event.key == pygame.K_RETURN:
                    print(text_columns)
                    inp_columns = text_columns
                    #text_columns = ""

        if event.type == pygame.KEYDOWN:
            if active_price == True:
                if event.key == pygame.K_BACKSPACE:
                    text_price = text_price[:-1]
                elif event.key is not pygame.K_RETURN:
                    text_price += event.unicode

                if event.key == pygame.K_RETURN:
                    print(text_price)
                    inp_price = text_price
                    #text_price = ""

        if event.type == pygame.KEYDOWN:
            if active_velocity == True:
                if event.key == pygame.K_BACKSPACE:
                    text_velocity = text_velocity[:-1]
                elif event.key is not pygame.K_RETURN:
                    text_velocity += event.unicode

                if event.key == pygame.K_RETURN:
                    print(text_velocity)
                    inp_velocity = text_velocity
                    #text_velocity = ""

    screen.fill((102, 179, 255))

    # Wechselt die Farbe des Eingabefeldes bei Berührung
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

    # Zeichnen der Eingabefelder
    pygame.draw.rect(screen, color_r, input_rows, 2)
    pygame.draw.rect(screen, color_c, input_columns, 2)
    pygame.draw.rect(screen, color_p, input_price, 2)
    pygame.draw.rect(screen, color_v, input_velocity, 2)

    # Text wird "gerendert"
    text_surface_r = FONT.render(text_rows, True, color_text)
    text_surface_c = FONT.render(text_columns, True, color_text)
    text_surface_p = FONT.render(text_price, True, color_text)
    text_surface_v = FONT.render(text_velocity, True, color_text)

    screen.blit(text_surface_r, (input_rows.x+5, input_rows.y+5))
    screen.blit(text_surface_c, (input_columns.x + 5, input_columns.y + 5))
    screen.blit(text_surface_p, (input_price.x + 5, input_price.y + 5))
    screen.blit(text_surface_v, (input_velocity.x + 5, input_velocity.y + 5))

    # Anpassung der Weite der Textfelder
    input_rows.w = max(150, text_surface_r.get_width() + 10)
    input_columns.w = max(150, text_surface_c.get_width() + 10)
    input_price.w = max(150, text_surface_p.get_width() + 10)
    input_velocity.w = max(150, text_surface_v.get_width() + 10)

    # Text über den Textfeldern
    FONT_1 = pygame.font.Font(None, 26)

    text_rows_cap = FONT_1.render("Anzahl der Reihen:", True, color_text)
    screen.blit(text_rows_cap, (100, 75))
    text_columns_cap = FONT_1.render("Anzahl der Spalten:", True, color_text)
    screen.blit(text_columns_cap, (100, 175))
    text_price_cap = FONT_1.render("Preis pro Stunde in €:", True, color_text)
    screen.blit(text_price_cap, (100, 275))
    text_velocity_cap = FONT_1.render("Geschwindigkeit der Simulation:", True, color_text)
    screen.blit(text_velocity_cap, (100, 375))

    # Programm wird aktualisiert
    pygame.display.flip()
    clock.tick(30)
