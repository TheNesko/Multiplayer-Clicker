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