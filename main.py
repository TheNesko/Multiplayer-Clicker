from random import randint
import pygame as pg
import sys

pg.init()

#-------Preferences--------    
display_x = 700
display_y = 500
game_title = "CLICKER MP"
#-------------------------


win = pg.display.set_mode((display_x, display_y))
pg.display.set_caption(game_title)

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
            pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()