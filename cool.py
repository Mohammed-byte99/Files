"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
class Block(pygame.sprite.Sprite):
   
    def __init__(self, color, width, height):
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
class Player(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self, x, y):
      
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
    
        self.change_x += x
        self.change_y += y
 
    def update(self):
        
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

screen.fill(WHITE)
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
    
    all_sprites_list.update()
    
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
