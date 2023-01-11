import pygame as pg


pg.init()
screen = pg.display.set_mode((400, 600))
COLOR_INACTIVE = pg.Color('white')
COLOR_ACTIVE = pg.Color('green')
FONT = pg.font.Font(None, 32)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Ändert die akutelle Farbe des Eingabefeldes.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        #Verändert die Größe des Rechtecks, wenn der Text zu lang wird.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

def main():
    clock = pg.time.Clock()
    inputrows = InputBox(100, 100, 140, 32)
    inputcolumns = InputBox(100, 200, 140, 32)
    inputprice = InputBox(100, 300, 140, 32)
    inputvelocity = InputBox(100, 400, 140, 32)
    input_boxes = [inputrows, inputcolumns, inputprice, inputvelocity]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        # Text über den Textfeldern
        FONT_1 = pg.font.Font(None, 26)
        text_rows = FONT_1.render("Anzahl der Reihen:", True, (255, 255, 255))
        screen.blit(text_rows, (100, 75))
        text_columns = FONT_1.render("Anzahl der Spalten:", True, (255, 255, 255))
        screen.blit(text_columns, (100, 175))
        text_price = FONT_1.render("Preis pro Stunde:", True, (255, 255, 255))
        screen.blit(text_price, (100, 275))
        text_velocity = FONT_1.render("Geschwindigkeit der Simulation:", True, (255, 255, 255))
        screen.blit(text_velocity, (100, 375))

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()