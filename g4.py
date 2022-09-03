import pygame
import random
import math

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

background = pygame.image.load("spacebg.jpg")

pygame.display.set_caption("Space Invander")

icon = pygame.image.load('spaceship.png')

pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_enemies = 5

for i in range(num_enemies):
    enemyimg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(45)

#bullet
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = -5
bullet_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10


over_font = pygame.font.Font("freesansbold.ttf",64)


def show_score(x,y):
    score = font.render("Score: %s"%score_value,True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text,(200,250))
    
def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x,y+10))

def isCollision(x1,y1,x2,y2): 
    distance = math.sqrt((math.pow(x1-x2,2))+(math.pow(y1-y2,2)))
    if distance < 27:
        return True
    else:
        return False
                                                                                          

#Game Loop
running = True
while running:
    
    #RGB - Red,Green,Blue
    screen.fill((0,0,0))
    #background image
    screen.blit(background, (-300,-200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

        
    for i in range(num_enemies):
        if enemyY[i]>440:
            for j in range(num_enemies):
                enemyY[j] = 2000 
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 736 or enemyX[i] <= 0:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
            
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 10
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)
    
    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY += bulletY_change

        
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()





















    
