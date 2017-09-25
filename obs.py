import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *
from random import choice
import util

class Obs(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.imagenes = [util.cargar_imagen('imagenes/cono.png'),
                                        util.cargar_imagen('imagenes/hueco.png'),
                                        util.cargar_imagen('imagenes/aceite.png'),
                                        util.cargar_imagen('imagenes/retro.png'),
                                        util.cargar_imagen('imagenes/rocas.png')]
		self.arrancon = pygame.mixer.Sound('sonidos/acelerar2.wav')
                self.image = self.imagenes[randint(0,4)]
		self.velocidad = randint(7,10)
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[1])
		self.cont = 0
        
	def update(self):
                self.rect.x -= self.velocidad
                teclas = pygame.key.get_pressed()
                if teclas[K_SPACE]:
                        self.acelerar()
                else:
                        self.arrancon.stop()
                
        def renovar(self):
		if self.rect.x <= 0:
                        self.image = self.imagenes[randint(0,4)]
                        self.velocidad = randint(1,10)
                        self.rect.x = 1500
                        self.cont = 0

        def acelerar(self):
                self.arrancon.play()
                self.rect.x -= 15
