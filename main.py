from random import randint
import pygame as pg
import pygame_menu as pg_menu  # Jeżeli tutaj wyskoczy błąd zainstaluj ten moduł: pip install pygame_menu ||<- do skopiowania
import socket


#-------Preferences--------    
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
GAME_TITLE = "CLICKER Multiplayer"
GAME_ICON = pg.image.load("images/icon.jpg") # Ikonę będę przerabiał tylko musze jakiegoś gimpa czy jaki chuj pobrac
BACKGROUND_COLOR = (119, 226, 252) # Potem bedzie zmieniane zależne od tematyki gry
# BACKGROUND_IMG = comming soon..


#-------------------------
#---------MENU(Wszystkie grafiki przycisków)------------
START_GAME = 'images/menu_elements/START GAME.jpg'
START_GAME_hover = 'images/menu_elements/hover/START GAME hover.png'
 
OPTIONS = 'images/menu_elements/OPTIONS.png' 
OPTIONS_hover = 'images/menu_elements/hover/OPTIONS hover.png'

QUIT = 'images/menu_elements/QUIT.png' 
QUIT_hover = 'images/menu_elements/hover/QUIT hover.png'




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

class Fonts:
    def __init__(self, 
                 font_size, 
                 font_family, 
                 font_color,
                 text,
                 set_bold,
                 set_italic):
        """
            Tworzenie tekstu
            Cechy tekstu wpisane dość czytelnie
            
            
            
        """
        self.font_size = font_size
        self.font_family = font_family
        self.font_color = font_color
        self.text = text
        self.font = pg.font.SysFont(font_family, font_size)
        """
            Jeżeli chcesz pogróbić albo pokrzywić tekst przy tworzeniu 
            należy wpisać wartość True, a jeżeli nie chcesz któryś z opcji należy wpisać wartość False
            
            Przykład:
            Fonts((...), True, False ) - Tylko pobrubiona
            Fonts((...), True, False ) - Tylko pokrzywiona
            Fonts((...), True, True ) - to i to
            Fonts((...), False, False ) - zwykły tekst
            
        """
        self.font.set_bold(set_bold)
        self.font.set_italic(set_italic)
        self.label = self.font.render(self.text, 1, self.font_color)
         
        
    
    def createLabel(self, win, x, y):
        self.win = win
        self.win.blit(self.label, (x, y))
  

 
class Button():
    def __init__(self,
                 win,
                 button_x,
                 button_y,
                 button_width, 
                 button_height, 
                 background_color, 
                 ):
        
        """
            Tworzenie przycisków
            Polega na podaniu wartości jakie widać powyżej ^^^
            
            i teraz tak:
            jeżeli chcemy użyć obrazka jako przycisk musimy wykonać kod w ten sposób:
            > Button(self.window, button_x, button_y, button_width, button_height, (kolor)).img(self.window, img_x, img_y, *Ścieżka do grafiki*)
                                                                                                            (Pozycja obrazka(najlepiej taka sama co przycisku))
            
            a jeżeli chcemy bez obrazka i sam kwadrat to:
            > Button(self.window, button_x, button_y, button_width, button_height, (kolor)).createButton()
        """
        self.win = win
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.button_height = button_height
        self.button_color = background_color
        

        
       
    
    
    def createButton(self):
        pg.draw.rect(self.win, self.button_color, 
                     (self.button_x, self.button_y, self.button_width, self.button_height))
    
    def img(self, win, image_x, image_y, image_path): 
        self.win = win  
        self.img_x = image_x 
        self.img_y = image_y 
        self.img_path = image_path
        self.image = pg.image.load(self.img_path)
        self.win.blit(self.image, (self.img_x, self.img_y))
        
        
class Game:
    def __init__(self):
        self.is_running = True

        """
        Inicjalizacja pygame
        tworzenie okna
        """
        pg.init()
        pg.display.set_icon(GAME_ICON)
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
        #testowt tekst
        
    
                
        
        """
            Fonts(rozmiar, 
                    czcionka, 
                    kolor,
                    tekst,
                    bold (domyślna wartość false),
                    italic (domyślna wartość false)).crateLabel(okno, współrzędne tego tekstu)
        """
        
        
        # Fonts(20, 'Arial',(0,0,0), 'Testowy Tekst',True , False).createLabel(self.window, 200, 200)
        
        # Test przycisku
        
        
        
        Button(self.window, 500, 200, 350, 100, (0,0,0)).img(self.window, 0, 0, START_GAME)
        Button(self.window, 500, 200, 350, 100, (0,0,0)).createButton()
        
        
        
        
        # test
        # Rect = pg.Rect(DISPLAY_WIDTH/2,
        #                DISPLAY_HEIGHT/2,
        #                50,
        #                50)
        # pg.draw.rect(self.window, (250,20,30), Rect)
        #----

        pg.display.update()
        
        self.window.fill(BACKGROUND_COLOR)

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