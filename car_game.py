import pygame
import random
import time
from pygame import mixer
import math




# size of window
x = 600
y = 650

#creat window and modifie it
pygame.init()
mother_windo = pygame.display.set_mode((x, y))
pygame.display.set_caption("game")
image = pygame.image.load("icon.png")
background1 = pygame.image.load("real.png")
background = pygame.transform.scale(background1, (x, y))
barrier = []
pygame.display.set_icon(image)

# add image car
playerimg = pygame.image.load("car1.png")

#cordonne
playerX = 275
playerY = 500
barX = []
barY = []
barrier_list = ["Car0.png", "Audi0.png", "Mini_van0.png", "Mini_truck0.png", "Police0.png"]
height = [119, 110, 117, 118, 110]
width = [30, 25, 30, 30, 25]
change_Y = []
bgX = 0
barrier_choises = []
bgY = 0
bar_stat = True
number_of_bariers = 4
font = pygame.font.Font('freesansbold.ttf', 64)
start_time = time.time()

#adding backgound music
bg_music = pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
for i in range(number_of_bariers):
    barrier_choises.append(random.choice(barrier_list))

for i in range(number_of_bariers) :
    barrier.append(pygame.image.load(barrier_choises[i]))
    barX.append(random.randint(85, 380))
    barY.append(random.randint(0, 380))
    change_Y.append(1) 

# fonction to move car and scrool background image
def player(x, y, bar_stat, barX, barY):
    bg_Y = bgY % background.get_rect().width 
    mother_windo.blit(background, (bgX, bg_Y))
    if bg_Y <= 650 :
        mother_windo.blit(background, (0, bg_Y - background.get_rect().width))
    playerY = y - 8
    mother_windo.blit(playerimg,(playerX, playerY))
    for i in range(number_of_bariers):
        result = position(barX, barY, i)
        for k in range(199):
            if result == True:
                barriers(barX[i], barY[i], barrier[i])
                break
            else:
                result = position(barX, barY, i)
    return bg_Y

def position(barX, barY, i):
          if i == 0 :
              return True
          elif i == 1 :
              dist_X = abs(barX[i] - barX[0])
              dist_Y = abs(barY[i] - barY[0])
              c1 = math.sqrt(dist_X**2 + dist_Y**2)
              if c1 < 100 :
                  return False
              else:
                  return True
          elif i == 2 :
              dist_X = abs(barX[i] - barX[1])
              dist_Y = abs(barY[i] - barY[1])
              dist_X1 = abs(barX[i] - barX[0])
              dist_Y1 = abs(barY[i] - barY[0])
              c1 = math.sqrt(dist_X**2 + dist_Y**2)
              c2 = math.sqrt(dist_X1**2 + dist_Y1**2)
              if c1 < 100 or c2 < 100 :
                   return False
              else :
                  return True
          elif i == 3 :
             dist_X = abs(barX[i] - barX[2])
             dist_Y = abs(barY[i] - barY[2])
             dist_X1 = abs(barX[i] - barX[1])
             dist_Y1 = abs(barY[i] - barY[1])
             dist_X2 = abs(barX[i] - barX[0])
             dist_Y2 = abs(barY[i] - barY[0])
             c1 = math.sqrt(dist_X**2 + dist_Y**2)
             c2 = math.sqrt(dist_X1**2 + dist_Y1**2)
             c3 = math.sqrt(dist_X2**2 + dist_Y2**2)
             if c1 < 100 or c2 < 100 or c3 < 100 :
                   return False
             else :
                  return True
              

# barriers 
def barriers(barX, barY, barrier) :           
        mother_windo.blit(barrier,(barX, barY))

def loss(bg_Y):
        text = font.render('GAME OVER', True, (255, 255, 255))
        mother_windo.blit(text, (100, 100))
        for i in range(number_of_bariers):
            barY[i] = 2000
        return False

def win(bg_Y):
    text = font.render('YOU WIN', True, (255, 255, 255))
    mother_windo.blit(text, (150, 100))
    for i in range(number_of_bariers):
        barY[i] = 2000

st = False
status = True
sor = sorted(barrier_list) 
condition = []
condition_OX = []
fr = True

while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    mother_windo.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    if fr == True:
        if keys[pygame.K_RIGHT] :
            if playerX >= 385 :
                pass
            else:
                playerX = playerX + 4
        if keys[pygame.K_LEFT] :
            if playerX <= 85 :
                pass
            else:
                playerX = playerX - 4
    bg_Y = player(playerX, playerY, bar_stat, barX, barY)
    for i in range(number_of_bariers):
        barY[i] = barY[i] + change_Y[i]
        if barY[i] > 650 :
            barY[i] = barY[i] - 850
            barX[i] = random.randint(80, 380)

    for i in range(len(barrier)):
        if fr == False :
            break
        for ele in barrier_choises :
            condition.append(height[sor.index(ele) - 1])
            condition_OX.append(width[sor.index(ele) - 1])
        try:
            disX = abs(playerX - barX[i])
            disY = abs(playerY - (barY[i] ))
            disX1 = abs(playerX - barX[2] )
            disY1 = abs(playerY - (barY[2] ))
            disX2 = abs(playerX - barX[1])
            disY2 = abs(playerY - (barY[1] ))
            disX3 = abs(playerX - barX[0])
            disY3 = abs(playerY - (barY[0] ))
            c = math.sqrt(disX**2 + disY**2)
            c1 = math.sqrt(disX1**2 + disY1**2)
            c2 = math.sqrt(disX2**2 + disY2**2)
            c3 = math.sqrt(disX3**2 + disY3**2)
            if c1 <= condition_OX[1] or c2 <= condition_OX[2]  or c <= condition_OX[0]  or c3 <= condition_OX[3]  :
                print("here0")
                fr = False
                loss_sound = mixer.Sound("explosion.wav")
                loss_sound.play()
                pygame.mixer.music.stop()
                break
            if condition[0] >= disY > disX < condition_OX[0]  or condition[1] >= disY1 > disX1 < condition_OX[1] or condition[2] >= disY2 >disX2 < condition_OX[2] or condition[3] >= disY3 > disX3 < condition_OX[3]:
                print("here1")
                fr = False
                loss_sound = mixer.Sound("explosion.wav")
                loss_sound.play()
                pygame.mixer.music.stop()

                break
            else:
                fr = True
        except:
          pass
    if  False == fr :
        loss(bg_Y)
        bgY = bgY - 5
    font_time = pygame.font.SysFont(None, 64)
    dure = round(time.time() - start_time, 2)
    if dure >= 90 and fr == True:
        pygame.mixer.music.stop() 
        win(bg_Y)
    else:
        if fr == True:
            text = font_time.render(f"time: {dure} s", True, (255, 255, 255))
            mother_windo.blit(text, (30, 18))
        bgY = bgY + 5 
    pygame.display.update()
    