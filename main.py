from random import randint as rnd
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
    def codeGen(max_len):
        """
            Wyznaczanie długości kodu dla naszych potrzeb w (max_len)
            i na dole jego generowanie :) 
        """
        characters = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%&"
        code=[]
        for i in range(max_len):
            rand_number = rnd(0,len(characters))
            for char in characters[rand_number]:
                continue
            code.append(char)
        return "Code: "+"".join(code)

   # print(codeGen(10))  <- przykładowe wyświetlanie ¯\_(ツ)_/¯




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