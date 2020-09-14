"""
 Simple graphics demo
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
# Import a library of functions called 'pygame'
import pygame
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LBLUE = (22, 248, 233)
BROWN = (130, 78, 31)

 
PI = 3.141592653
 
# Set the height and width of the screen
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Professor Craven's Cool Game")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(LBLUE)
 
    # Draw a rectangle

    pygame.draw.rect(screen, GREEN, [0, 420, 500, 50], 0)
    pygame.draw.rect(screen, BROWN, [0, 450, 500, 200], 0)
    pygame.draw.rect(screen, RED,   [25, 270, 150, 150], 0)    
  
       
    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLUE, [25, 200, 150, 150], 0, PI, 50)
 
 
    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()