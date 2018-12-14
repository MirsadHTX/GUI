import pygame

pygame.init()

lydObjekt1 = pygame.mixer.Sound('lyd.wav')

minVindue = pygame.display.set_mode((500 , 600))

while True:  # main game l      oop


    for event in pygame.event.get():

        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            pygame.mixer.Sound.play(lydObjekt1)



    pygame.display.update()
