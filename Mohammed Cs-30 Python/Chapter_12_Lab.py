"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
import random
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rectangle():

    def __init__(self):

        self.x = random.randrange(700)
        self.y = random.randrange(500)

        self.h = random.randrange(20,70)
        self.w = random.randrange(20,70)

        self.change_x = random.randrange(-3,3)
        self.change_y = random.randrange(-3,3)

        self.color = [225, 155, 5]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.h, self.w], 0)

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

class Ellipse(Rectangle):
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.h, self.w], 0)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []
for x in range(100):
    my_list.append(Rectangle())
    R = random.randrange(0, 256)
    B = random.randrange(0, 256)
    G = random.randrange(0, 256)
    self.color = (R, B, G)
for x in range(100):
    my_list.append(Ellipse())


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
          
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for rect in my_list:
        rect.draw(screen)
        rect.move()
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
