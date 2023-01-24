# Anzeigen der Ausgangsvariablen
font_output = pygame.font.Font(None, 32)

# Anzeige für Tag und Uhrzeit
dhm = [15, 12, 30]
day = dhm[0]
hour = dhm[1]
minute = dhm[2]

text_day = font_output.render(f"Tag: {day}", True, (255, 255, 255))
screen.blit(text_day, (10, 10))
text_time = font_output.render(f"Uhrzeit: {hour}:{minute}", True, (255, 255, 255))
screen.blit(text_time, (10, 40))

# Anzeige für die belegten Parkplätze
Carnr = [20]
car_nr = Carnr[0]

text_occupied = font_output.render(f"Belegte Parkplätze: {car_nr}", True, (255, 255, 255))
screen.blit(text_occupied, (435, 10))

# Anzeige für die freien Parkplätze
lpark = [50]
l_park = lpark[0]

text_l_park = font_output.render(f"Freie Parkplätze: {l_park}", True, (255, 255, 255))
screen.blit(text_l_park, (855, 10))

# Einstellungsfenster
text_settings = font_output.render("Einstellungen", True, (255, 255, 255))
screen.blit(text_settings, (1275, 10))