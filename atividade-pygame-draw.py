import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

points = []
square = []
retangle = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
     keys = pygame.key.get_pressed()


    if keys[pygame.K_c]: 
        if event.type == MOUSEBUTTONDOWN:
            
            square
            points.append(event.pos)

    screen.fill((255, 255, 255))



    for point in points:
        pygame.draw.circle(screen, (39, 39, 255), point, 39)
    pygame.display.update()