import pygame

#function to draw rect
def drawRect(color1, color2, x, y, width, height):
    pygame.draw.rect(screen, color1, [x, y, width, height])
    pygame.draw.rect(screen, color2, [x, y - height, width, height])

#Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


#Screen settings
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Samuel's Game")

#loop untill user clicks close button
done = False

#screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    screen.fill(WHITE)

    drawRect(BLACK, BLUE, 100, 100, 200, 10)
    drawRect(GREEN, RED, 200, 200, 300, 50)
    drawRect(BLUE, RED, 300, 300, 200, 10)  

    pygame.display.flip()
    clock.tick(60)    
    