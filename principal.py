import sys, pygame, util
from pygame.locals import *
from carro import *
from obs import *
from random import *

SCREEN_WIDTH = 1324
SCREEN_HEIGHT = 558
ICON_SIZE = 32

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "La Carretera" )
    background_image = util.cargar_imagen('imagenes/carreteraverdedf.png');
    pierde_vida = util.cargar_sonido('sonidos/choque.wav')
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    carro = Carro()
    obs = [Obs((1500,337),randint(1,10)),
           Obs((1500,115),randint(1,10)),
           Obs((1500,202),randint(1,10)),
           Obs((1500,290),randint(1,10))]
    
    while True:
        for n in obs:
            n.update()
            n.renovar()
            
        fuente = pygame.font.Font(None,50)
        texto_puntos = fuente.render("Puntos: "+str(n.puntaje),1,(255,255,255))
        texto_vida = fuente.render("Vida: "+str(carro.vida),1,(255,255,255))
        
        carro.update()
                
        for n in obs:
            if carro.rect.colliderect(n.rect):
                carro.image = carro.imagenes[1]
                pierde_vida.play()
                if carro.vida > 0:
                    carro.vida=carro.vida-1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(carro.image, carro.rect)
        screen.blit(texto_vida,(400,500))
        screen.blit(texto_puntos,(100,500))
        for n in obs:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)
        

      
if __name__ == '__main__':
      game()

