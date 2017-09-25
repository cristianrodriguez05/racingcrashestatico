import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Carro(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.vida = 1
		self.imagenes = [util.cargar_imagen('imagenes/coche.png'),
						util.cargar_imagen('imagenes/carroestre.png')]
                self.arrancon = pygame.mixer.Sound('sonidos/acelerar2.wav')
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(150, 265)
		self.puntos = 0
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:
			if teclas[K_UP] and self.rect.y>=115:
				self.rect.y -= 10
				self.image = self.imagenes[0]
			elif teclas[K_DOWN] and self.rect.y<=465-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[0]

	
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
