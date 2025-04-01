import pygame
import random

pygame.init()

width,height = 800,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Car Game")

playercar = pygame.image.load("car.png")
playercar = pygame.transform.scale(playercar,(80,120))

aicar = pygame.image.load("car2.png")
aicar = pygame.transform.scale(aicar,(80,120))

playerx,playery = width//2-40,height-150
aix,aiy = random.randint(100,width-100),-120

clock = pygame.time.Clock()
running  = True

while running:
    screen.fill((0,0,0))

    for i in range(0,height,40):
        pygame.draw.rect(screen,(255,255,255),(width//2-5,i,10,20))

    for event in pygame.event.get():
        if(event.type==quit):
            running=False

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] and playerx>100):
        playerx-=5
    elif(keys[pygame.K_RIGHT] and playerx<width-120):
        playerx+=5

    aiy+=5
    if(aiy>height):
        aiy = -120
        aix = random.randint(100,width-180)

    screen.blit(playercar,(playerx,playery))
    screen.blit(aicar,(aix,aiy))

    pygame.display.update()
    clock.tick(60)

pygame.quit()


# import pygame
# import sys

# pygame.init()

# width,height = 400,300
# screen = pygame.display.set_mode((width,height))
# clock = pygame.time.Clock()

# ballcolor = (255,255,255)
# ballr = 10
# ballx,bally = 100,80
# velocityx,velocityy = 30,30

# running = True
# while running:
#     screen.fill((0,0,0))

#     for event in pygame.event.get():
#         if(event==pygame.QUIT):
#             running = False

#     ballx+=velocityx
#     bally+=velocityy

#     if(ballx-ballr<=0 or ballx+ballr>=width):
#         velocityx=-velocityx
#     if(bally-ballr<=0 or bally+ballr>=height):
#         velocityy=-velocityy

#     pygame.draw.circle(screen,ballcolor,(ballx,bally),ballr)

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
# sys.quit()
