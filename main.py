from random import randint
import pygame as pg
import sys

pg.init()

#-------Preferences--------    
display_x = 700
display_y = 500
game_title = "CLICKER Multiplayer SEX SEX SEX SEX SEX SEX SEX SEX SEX SEX SEX SEX SEX SEX"
icon = pg.image.load("Multiplayer-Clicker/images/icon.jpg") # Ikonę będę przerabiał tylko musze jakiegoś gimpa czy jaki chuj pobrac
background_color = (119, 226, 252) # Potem bedzie zmieniane zależne od tematyki gry
#-------------------------


win = pg.display.set_mode((display_x, display_y))
pg.display.set_caption(game_title)
pg.display.set_icon(icon)


class Code:
    def generate(length):
        """
            Przykład użycia:
            print(Code.generate(10)) - zwróci kod o długości 10
        """
        characters = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%&"
        code = ""
        for _ in range(length):
            random_number = randint(0, len(characters)-1)
            code += characters[random_number]
        return code


print(Code.generate(10))


class Game:
    def __init__(self):
        pass

    def run(self):
        """
            Zamykanie okna
            
        """
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            win.fill(background_color)
            pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()