import pygame
import random
pygame.init()

velocity = 5
bounces = 0
info = pygame.display.Info()
sx = info.current_w
sy = info.current_h
screen = pygame.display.set_mode((0, 0))
running = True
logo1 = pygame.image.load("logo.png")
logo100 = pygame.image.load("logo100.png")
logo1000 = pygame.image.load("logo1000.png")
logo10000 = pygame.image.load("logo10000.png")
logo100000 = pygame.image.load("logo100000.png")
logo = logo1
lw, lh = logo.get_size()
x = random.randint(1, sx - lw)
y = random.randint(1, sy - lh)
xv = velocity
yv = velocity

bounces = 0
corners = 0
font = pygame.font.Font(None, size=40)
clock = pygame.time.Clock()

while running:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
                running = False

        speed = 1000 if keys[pygame.K_s] else 5
        
        steps = abs(speed)
        
        xv = speed if xv > 0 else -speed
        yv = speed if yv > 0 else -speed
        xv = xv / speed
        yv = yv / speed
    
    for i in range(steps):
        x += xv
        y += yv
        
        if x >= sx - lw:
            x = sx -lw
            xv = -xv
            bounces += 1
        
        if y >= sy -lh:
            y = sy - lh
            yv = -yv
            bounces += 1
            
        if x <= 0:
            xv = -xv
            bounces += 1
            
        if y <= 0:
            yv = -yv
            bounces += 1
            
        if x >= sx - lw:
            if y >= sy -lh:
                corners += 1
                
        if x >= sx - lw:
            if y <= 0:
                corners += 1
        
        if x <= 0:
            if y >= sy -lh:
                corners += 1
                
        if x <= 0:
            if y <= 0:
                corners += 1
                
        if bounces == 100:
            logo = logo100
        
        if bounces == 1000:
            logo = logo1000
        
        if bounces == 10000:
            logo = logo10000
        
        if bounces == 100000:
            logo = logo100000
    
    text1  = font.render("Corners:" + str(corners), True, (255,255,255))
    text2 = font.render("Bounces:" + str(bounces), True, (255, 255, 255))
    
    screen.fill((0,0,0))
    screen.blit(logo, (x,y))
    screen.blit(text1, (sx / 2.4,sy / 2))
    screen.blit(text2, (sx / 1.85, sy / 2))
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()