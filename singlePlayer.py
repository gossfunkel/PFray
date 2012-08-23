import pygame
from pygame.locals import *

# Welcome to the Fray

# Translation from guide:
# __init__ = initialise
# _running = running
# _display_surf = displaySurf
# _image_surf = imageSurf
# on_x = onX

class Fray:
    def initialise(self): # "__init__"
        self.running = True
        self.displaySurf = None
        self.imageSurf = None
        self.size = self.weight, self.height = 800, 1000
    
    def onInit(self):
        pygame.init()
        self.displaySurf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
        self.imageSurf = pygame.image.load(

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self.running = False
    
    def onLoop(self):
        pass
    
    def onRender(self):
        pass
    
    def onCleanup(self):
        pygame.quit()
    
    def onExecute(self):
        if self.onInit() == False:
            self.running = False
        while self.running:
            for event in pygame.event.get():
                self.onEvent(event)
            self.onLoop()
            self.onRender()
        self.onCleanup()
 
if __name__ == "__main__" :
    theFray = Fray()
    theFray.on_execute()

