"""
 Simple graphics demo
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
# Import a library of functions called 'pygame'
import random
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
DBROWN = (130, 69, 24)
YELLOW = (248, 248, 77)
LRED = (249, 132, 108)
LPURPLE = (169, 143, 252)
PURPLE = (64, 8, 243)
PINK = (255, 0, 215)
BEIGE = (246,181,101)


PI = 3.141592653
 
# Set the height and width of the screen
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Mohammeds Beautiful Kite Painting")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
cloud_x = 100
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(LBLUE)

    # Draw Stickman
    pygame.draw.line(screen, BLACK, [300, 360], [300, 390], 5)
    pygame.draw.line(screen, BLACK, [300, 380], [330, 350], 3)
    pygame.draw.line(screen, BLACK, [300, 380], [270, 350], 3)
    pygame.draw.line(screen, BLACK, [300, 390], [310, 420], 3)
    pygame.draw.line(screen, BLACK, [300, 390], [290, 420], 3)

    # Draw Kite String
    pygame.draw.line(screen, WHITE, [330, 350], [350, 200], 3)


    # Draw rectangles 
    pygame.draw.rect(screen, GREEN, [0, 420, 500, 50], 0)
    pygame.draw.rect(screen, BROWN, [0, 450, 500, 200], 0)
    pygame.draw.rect(screen, RED,   [25, 270, 150, 150], 0)
    pygame.draw.rect(screen, BROWN, [75, 340, 50, 80], 0)
    pygame.draw.rect(screen, LRED, [120, 170, 40, 90], 0)
    pygame.draw.rect(screen, BLUE,  [35, 290, 40, 40], 0)
    pygame.draw.rect(screen, BLUE,  [125, 290, 40, 40], 0)



    # Ellispe for the door, and clouds and sun
    pygame.draw.ellipse(screen, YELLOW, [105, 370, 10, 10], 0)
    pygame.draw.ellipse(screen, YELLOW, [20, 20, 80, 80],  0)
    pygame.draw.ellipse(screen, BEIGE, [285, 330, 30, 30], 0)

    for cloud_x in range (0, 400, 200): 
        pygame.draw.ellipse(screen, WHITE,  [185+cloud_x, 40, 90, 50], 0)
        pygame.draw.ellipse(screen, WHITE,  [245+cloud_x, 60, 50, 40], 0)
        pygame.draw.ellipse(screen, WHITE,  [185+cloud_x, 70, 90, 50], 0)
        pygame.draw.ellipse(screen, WHITE,  [165+cloud_x, 60, 50, 40], 0)
    cloud_x += 5
    

    if cloud_x > 500:
    # Reset it just above the top
        y = random.randrange(-50, -10)
        cloud_x = y
   
    # This draws a triangle for roof, and for the  kite
    pygame.draw.polygon(screen, LPURPLE, ([100, 170], [25, 270], [175, 270], 0))
    pygame.draw.polygon(screen, BLUE, ([350,240], [390, 200], [310, 200], [350, 160], 0))
    
                
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()
