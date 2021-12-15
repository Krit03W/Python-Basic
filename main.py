import pygame
import numpy as np

pygame.init()

display = pygame.display.set_mode((1150, 700))

clock = pygame.time.Clock()
FPS = 30

x = 0
y = 350
heading = 0
while True:
    #chek exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    dist = 5
    heading_rad = heading/180*np.pi
#chek user input
    if pygame.key.get_pressed()[pygame.K_w]:
        x = x + dist * np.cos(heading)
        y = y + dist * np.sin(heading)
    if pygame.key.get_pressed()[pygame.K_a]:
        x = x + dist * np.cos(heading-np.pi/2)
        y = y + dist * np.sin(heading-np.pi/2)
    if pygame.key.get_pressed()[pygame.K_s]:
        x = x - dist * np.cos(heading)
        y = y - dist * np.sin(heading)
    if pygame.key.get_pressed()[pygame.K_d]:
        x = x + dist * np.cos(heading+np.pi/2)
        y = y + dist * np.sin(heading+np.pi/2)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        heading = heading - 3
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        heading = heading + 3


#compute
    display.fill('black')
    pygame.draw.circle(display, 'red', (x,y), 50)

    heading_rad = heading/180*np.pi
    start_line = (x + 30*np.cos(heading_rad), y + 30*np.sin(heading_rad))
    end_line = (x + 70*np.cos(heading_rad), y + 70*np.sin(heading_rad))
    pygame.draw.line(display, 'yellow', start_line, end_line, 5)


#wait
    clock.tick(FPS)

#display to player
    pygame.display.update()
