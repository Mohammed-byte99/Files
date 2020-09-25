"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
def draw_cloud(screen, x, y):
    pygame.draw.ellipse(screen, WHITE,  [20 + x, 0 + y, 90, 50], 0)
    pygame.draw.ellipse(screen, WHITE,  [80 + x, 20 + y, 50, 40], 0)
    pygame.draw.ellipse(screen, WHITE,  [20 + x, 30 + y, 90, 50], 0)
    pygame.draw.ellipse(screen, WHITE,  [0 + x, 20 + y, 50, 40], 0)

def draw_cloud2 (screen, z, w):
    pygame.draw.ellipse(screen, WHITE,  [20 + z, 0 + w, 90, 50], 0)
    pygame.draw.ellipse(screen, WHITE,  [80 + z, 20 + w, 50, 40], 0)
    pygame.draw.ellipse(screen, WHITE,  [20 + z, 30 + w, 90, 50], 0)
    pygame.draw.ellipse(screen, WHITE,  [0 + z, 20 + w, 50, 40], 0)
 
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10

 
# -------- Main Program Loop (KEYBOARD) -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

        pos = pygame.mouse.get_pos()
        z = pos[0]
        w = pos[1]
                      
    
        
    # --- Game Logic
 
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
 
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
 
    draw_cloud(screen, x_coord, y_coord)
    draw_cloud2(screen, z, w)    

 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
