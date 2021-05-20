import pygame
import random

# Initializing the pygame
pygame.init()

# Creating the game screen
screen = pygame.display.set_mode((1400,760))

# Background
background = pygame.image.load("2303148.jpg")

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
enemyXchange = 1
enemyYchange = 40

# Bullet
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 620
#bulletXchange = 0
bulletYchange = 3
bulletState = "ready"

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))

# Game loop [Infinite loop]
running = True
while running:
    
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background 
    screen.blit(background, (0, 0))

    # All the events [keybord or mouse] are detected and looped inside in this for loop
    for event in pygame.event.get():

        # Check whether the close button has pressed
        if event.type == pygame.QUIT:
            running = False
        
        # Check whether the a key is pressing
        if event.type == pygame.KEYDOWN:
            # Left movement of the ship
            if event.key == pygame.K_a:
                playerXchange = -1.1
            # Right movement of the ship
            if event.key == pygame.K_d:
                playerXchange = 1.1     
            # Bullet moving
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

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

    # Enemy moves
    enemyX += enemyXchange 
    # Define the bounderies and control the movement of enemy 
    if enemyX <= 0:
        enemyXchange = 1
        enemyY += enemyYchange 
    elif enemyX >= 1336:
        enemyXchange = -1
        enemyY += enemyYchange 

    # Bullet movement
    # Bullet reading
    if bulletY <= 0: 
        bulletY = 620
        bulletState = "ready"
    
    # Bullet firing
    if bulletState is "fire": 
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYchange


    # player
    player(playerX, playerY)

    # Enemy
    enemy(enemyX, enemyY)

    # Updating everything inside the game window
    pygame.display.update()