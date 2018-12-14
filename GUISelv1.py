import pygame, sys
import pygame.locals


breddePaaVinduet = 1000
hoejdePaaVinduet = 500
roedBaggrund = 0
groenBaggrund = 255
blaaBaggrund = 0


pygame.init()
minVindue = pygame.display.set_mode((breddePaaVinduet, hoejdePaaVinduet))
minVindue.fill((roedBaggrund , groenBaggrund , blaaBaggrund))

GUIErIgang = True

while (GUIErIgang):



    pygame.draw.rect(minVindue,(255,0,0),(20,50,50,100),0)

    for event in pygame.event.get():

         if event.type == pygame.locals.QUIT:

             pygame.quit()

             sys.exit()


    pygame.display.update()