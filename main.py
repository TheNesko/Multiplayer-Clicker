from random import randint
import pygame as pg
import socket


#-------Preferences--------    
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500
GAME_TITLE = "CLICKER MP"
#--------------------------


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


class Server:
    def __init__(self):
        """
        Ta klasa jest odpowiedzialna za logike multiplayer
        host jest to kod generowany przez klase Code
        """
        self.server = socket.socket()
        self.host = Code.generate(8)
        self.port = 69420


class Game:
    def __init__(self):
        self.is_running = True

        """
        Inicjalizacja pygame
        tworzenie okna
        """
        pg.init()
        pg.display.set_caption(GAME_TITLE)
        self.window = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def update(self):
        """
        logika gry
        """
        pass

    def render(self):
        """
        funkcje wyświetlające na ekranie
        logika interfejsu
        """
        
        #test
        Rect = pg.Rect(DISPLAY_WIDTH/2,
                       DISPLAY_HEIGHT/2,
                       50,
                       50)
        pg.draw.rect(self.window, (250,20,30), Rect)
        #----

        pg.display.update()
        self.window.fill((30, 30, 30))

    def run(self):
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
            self.update()
            self.render()
            

if __name__ == "__main__":
    game = Game()
    game.run()