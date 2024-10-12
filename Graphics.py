import pygame
from Side import *
import pygame.event

pygame.init()

width = 1000
height = 1000

screen = pygame.display.set_mode((width, height))

s1 = pygame.Rect(100, 100, 100, 100)
s2 = pygame.Rect(210, 100, 100, 100)
s3 = pygame.Rect(320, 100, 100, 100)
s4 = pygame.Rect(100, 210, 100, 100)
s5 = pygame.Rect(210, 210, 100, 100)
s6 = pygame.Rect(320, 210, 100, 100)
s7 = pygame.Rect(100, 320, 100, 100)
s8 = pygame.Rect(210, 320, 100, 100)
s9 = pygame.Rect(320, 320, 100, 100)

face = [[s1, s2, s3],
        [s4, s5, s6],
        [s7, s8, s9]]
self = input("what side do you want to be looking at? ")

while True:
    pygame.draw.rect(screen, self, s1)
    pygame.draw.rect(screen, self, s2)
    pygame.draw.rect(screen, self, s3)
    pygame.draw.rect(screen, self, s4)
    pygame.draw.rect(screen, self, s5)
    pygame.draw.rect(screen, self, s6)
    pygame.draw.rect(screen, self, s7)
    pygame.draw.rect(screen, self, s8)
    pygame.draw.rect(screen, self, s9)
    pygame.display.update()
    for EVENT in pygame.event:
        if EVENT == pygame.QUIT:
            pygame.quit()
            sys.exit()