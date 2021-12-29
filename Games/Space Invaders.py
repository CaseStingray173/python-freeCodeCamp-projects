import pygame
import random
import math
from pygame import mixer

# Initializing pygame
pygame.init()

# Creating the screen for the game
screen = pygame.display.set_mode((800, 600))

# Adding a background to our game screen
background = pygame.image.load("background.png")

# Adding background sound
# mixer.music.load("background.wav")
# mixer.music.play(-1)

# Adding title and icon to the game window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Adding the player ship to the window
# At the bottom center of the screen
player_img = pygame.image.load("player.png")
player_x = 370
player_y = 480
player_x_change = 0

# Adding the enemy to the window
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, 800))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

# Adding the bullet to the window
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 11
# Ready status means that the bullet is still in the ship (i.e., its not fired)
# Fire status means that it has left the ship and its now on the screen
bullet_status = "ready"

# Score

score_val = 0
# We select the font for the score on the screen
font = pygame.font.Font("freesansbold.ttf", 32)

# The coordinates for the score text
text_x = 10
text_y = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)


# This renders the score using the font we selected and will display the score
# on the screen
def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))


# This renders the game over text and displays it on the screen
def game_over_txt():
    over_text = over_font.render("WASTED", True, (255, 0, 0))
    screen.blit(over_text, (270, 250))


# This places the player ship on the screen
def player(x, y):
    screen.blit(player_img, (x, y))


# This places the enemy on the screen
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


# This places the bullet on the screen
def fire_bullet(x, y):
    global bullet_status
    bullet_status = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# This checks if the bullet collided with the enemy
def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 27:
        return True
    else:
        return False


# While loop stop the window from closing automatically
# For loop inside the while loop checks for the events
# specifically the quit event (closing the window)
running = True
while running:

    # All the things that should be running along the window belong
    # in this while loop
    # You can change the background color of the empty window
    screen.fill((0, 0, 0))

    # We draw the background here since, like all the other things
    # we want to be on as long as the game window is on
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        # This is the if condition for Quitting the game
        if event.type == pygame.QUIT:
            running = False

        # This if checks if any key has been pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_status == "ready":
                    # This adds the bullet sound effect
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # Get the current x position of the spaceship
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player movement
    player_x += player_x_change

    # This if condition makes sure the player ship doesnt go out of the window
    if player_x < 0:
        player_x = 0
    elif player_x > 736:
        player_x = 736

    # Enemy movement
    for i in range(num_of_enemies):

        # Game over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_txt()
            wasted_sound = mixer.Sound("wasted.wav")
            wasted_sound.play()
            break

        enemy_x[i] += enemy_x_change[i]
        # This if condition makes sure the enemy doesnt go out of the window
        if enemy_x[i] < 0:
            enemy_x_change[i] = 3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] > 736:
            enemy_x_change[i] = -3
            enemy_y[i] += enemy_y_change[i]

        # Checking for collision
        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_status = "ready"
            score_val += 1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)
            # This adds the explosion sound effect
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()

        # Just like player ship we need the enemy to be on the screen
        # as long as the screen is on
        # Calling the enemy function to draw it on the screen
        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    # First if condition checks when the bullet is outside the window and
    # as soon as it goes outside the window it resets is positions to the
    # previous position
    if bullet_y < 0:
        bullet_y = 480
        bullet_status = "ready"

    if bullet_status == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Since we need the player ship to be on the screen as long as
    # the screen is on we will call the player function in the loop
    # to draw it on the screen
    # And you want this player ship drawn after the screen.fill() to
    # avoid the ship being drawn under the screen.fill()
    player(player_x, player_y)

    # Called the function for displaying the score on the screen
    show_score(text_x, text_y)

    # Once you change the anything in the window you need to update it
    pygame.display.update()
