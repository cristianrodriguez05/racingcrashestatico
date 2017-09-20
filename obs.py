import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *
from random import choice
import util

class Obs(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.imagenes = [util.cargar_imagen('imagenes/cono.png'),
                                        util.cargar_imagen('imagenes/hueco.png'),
                                        util.cargar_imagen('imagenes/aceite.png'),
                                        util.cargar_imagen('imagenes/retro.png'),
                                        util.cargar_imagen('imagenes/rocas.png')]
                self.image = self.imagenes[randint(0,4)]
		self.velocidad = randint(1,10)
		self.rect = self.image.get_rect()
		self.rect.move_ip(1500,choice([115, 202, 290, 337]))
        
	def update(self):
		self.rect.x -= self.velocidad
                
        def renovar(self):
		if self.rect.x <= 0:
                        self.image = self.imagenes[randint(0,4)]
                        self.velocidad = randint(1,10)
                        self.rect = self.image.get_rect()
                        self.rect.move_ip(1500,choice([100, 200, 300, 400]))
