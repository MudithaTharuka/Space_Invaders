import pygame
import random

# Initializing the pygame
pygame.init()

# Creating the game screen
screen = pygame.display.set_mode((1400,760))

# Title and the logo of the game window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("space-invaders.png")
playerX = 668
playerY = 620
playerXchange = 0

# Enemy
enemyImage = pygame.image.load("main_enemy.png")
enemyX = random.randint(0, 1336)
enemyY = random.randint(50, 200)
enemyXchange = 0

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

# Game loop [Infinite loop]
running = True
while running:
    
    # All the events [keybord or mouse] are detected and looped inside in this for loop
    for event in pygame.event.get():

        # Check whether the close button has pressed
        if event.type == pygame.QUIT:
            running = False
        
        # Check whether the an moving key is pressing
        if event.type == pygame.KEYDOWN:
            # Left movement of the ship
            if event.key == pygame.K_a:
                playerXchange = -0.8
            # Right movement of the ship
            if event.key == pygame.K_d:
                playerXchange = 0.8      

        # Check whether the an moving key is relesing
        if event.type == pygame.KEYUP:
            # Stop movement of the ship
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerXchange = 0


    # player moves
    playerX += playerXchange # Is there any movement
    # Define the bounderies and control the movement of spaceship out of them
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1336:
        playerX = 1336
    # player
    player(playerX, playerY)

    # Enemy
    enemy(enemyX, enemyY)

    # Updating everything inside the game window
    pygame.display.update()