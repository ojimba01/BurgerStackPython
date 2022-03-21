#Olayinka Jimba
##############
import sys
#import pygame
import random
#Allows for random numbers to be generated 
#Just importing pygames library
#import media
#Just importing media library
import pgzrun
#Just importing pygame zeros library
#import characters
global enemies
global game_status
global game
BURGER = "burger.png"
#TITLESCREEN = Actor("titlescreen.png")
#Defining the burger variable attached to the burger file name on the computer
WIDTH = 550
#Declaring the Width of screen
HEIGHT = 600
#Declaring the Height of screen
#Below are just miscelanious or unused variables (these can be deleted)
RED = 200, 0, 0
#WHITE = 255, 255, 255
SKY = 135, 206, 235
BOX = Rect((0, 20), (100, 10))
#hitbox = rect(BOX, RED)
#POS = (100,100)
#TT = Actor("title")
#CIRC = filled_circle((0,20),100,(0,0,0))
#draw.filled_circle(pos, radius, (r, g, b))
#invisible = Rect(WIDTH//2,HEIGHT - 30, 50, 25)
START = Actor("start")
BURGER = Actor('fullburger')
#hitbox.y = HEIGHT - 30
#hitbox.x = WIDTH//2
actors=[]
PLATE = Actor("plate2")
PLATE.y = HEIGHT - 30
PLATE.x = WIDTH//2
game = Actor('titlescreen')
#main = screen.fill((135, 206, 235))
#main1= Actor(main)
game.state = ['titlescreen', 'main', 'youwon']
game_status = game.state[0]
#start.pos = 700,750

#quitgame = Actor("title")
#quitgame.pos = 600, 750

#gameover = False
#score = 0
#gamemode = 1
#actors =[]
start = Actor("start")
topbun = Actor("topbun")
middle = Actor("middle")
bottombun = Actor("bottombunmain")
topbun.x = random.randint(40,WIDTH-40)
topbun.y = -100
enemies = [topbun,middle,bottombun]

enemies.append(Actor("topbun"))
enemies.append(Actor("middle"))
enemies.append(Actor("bottombunmain"))

gamestart=1
#This function is just updating the game for everytime there is a user input
# and or event.

run_once = 0
#def win():
    #screen.blit('youwon',(0,0))
def draw_time():
    screen.draw.text(str(game_timer),(500,30), color="black")
def draw_intruct():
    screen.draw.text(str("Complete the burger in 30 seconds using the arrow keys to win!"),(30,500), color="black")
def draw_credit():
    screen.draw.text(str("Game Developed by Olayinka"),(30,500), color="black")
def draw_game_over():
    screen.fill((0,0,0))
    screen.blit('game-over', (200, 200))
    screen.blit('press-enter2', (300, 400))
def draw_game_won():
    #clock.schedule(win, 3.0)
    screen.blit('youwon',(0,0))
    
##
            
# Draw the main menu Screen
def draw_main_menu():
    if game_status == game.state[0]:
        screen.blit('titlescreen', (0,0))
        #game.draw()
def main_loop():
    global game_status
    if game_status == game.state[1]:
        draw_game()
        if keyboard.rshift or keyboard.lshift:
            sys.exit()
        if keyboard.left:
            PLATE.x -=5
        elif keyboard.right:
            PLATE.x +=5
        for enemy in enemies:
            x=1
            enemy.y += 5
            if enemy.y > HEIGHT + 60:
                enemy.y = -100
                enemy.x = random.randint(100, WIDTH-60)
            if PLATE.image == "plate2":
                if PLATE.contains(bottombun):
                    sounds.startgameclicksound.play()
                    Run(run_once)
                    PLATE.image = "level1"
            if PLATE.image == "level1":
                if PLATE.contains(middle):
                    sounds.startgameclicksound.play()
                    Run2(run_once)
                    PLATE.image = "level2"
            if PLATE.image == "level2":
                if PLATE.contains(topbun):
                    sounds.startgameclicksound.play()
                    Run3(run_once)
                    PLATE.image = "level3"
            if PLATE.image == "level3":
                sounds.startgameclicksound.play()
                game_status = game.state[2]
            #if PLATE.image == "level3":
                #game_status == game.state[2]
                
    
# Draw the game over Screen
#def draw_background 
def draw_game():
    #while game_status == game.state[0]:
    screen.fill((135, 206, 235))
   

def lev1(actor, containment):
    if actor.contains(containment):
        actor.image = "level1"
    return actor
def lev2(actor, containment):
    if actor.contains(containment):
        actor.image = "level2"
    #while actor == Actor("level2"):
    return actor
def lev3(actor, containment):
    if actor.contains(containment):
        actor.image = "level3"
    #while actor == Actor("level2"):
    return actor

def Run(run):
    run=0
    while run==0:
            if run_once == 0:
                lev1(PLATE, bottombun)
                run+= 1
                
def Run2(run):
    run=0
    while run==0:
            if run_once == 0:
                lev2(PLATE, middle)
                run+= 1
                
def Run3(run):
    run=0
    while run==0:
            if run_once == 0:
                lev3(PLATE, topbun)
                run+= 1
                
            
#Background Music is here
game_timer = 30
game_timer_start = 30
timer_decrement = 0.2

#if gamestart ==1:
#    music.set_volume(1)
  #  music.play("dinerdash")
  #  print(music.is_playing("dinerdash"))
 #   if game_timer <= 0:
    #    sounds.stop("dinerdash")
        
    
def on_key_down():
    global game_status
# We only care are certain keys if we are in the title or

#   gameover states (namely the return key)

    if game_status == game.state[0]:
        if keyboard.RETURN:
            # Change the state to be "game"
            game_status = game.state[1]
    if game_status == game.state[2]:
        if keyboard.rshift or keyboard.lshift:
            sys.exit()
            # Change the state to be "game"
            game_status = game.state[0]
            

            

    # Exit the program

        #sys.exit()
def draw_entities():
    BURGER.draw()
    PLATE.draw()
    for enemy in enemies:
        enemy.draw()
def update():
    global game_timer
    
    if game_status == game.state[1]:
        if (game_timer <= 0):
            return
        else:
            game_timer -= 0.017
        main_loop()
    if game_status == game.state[2]:
        draw_game_won()
#    global score, gamestart

#dont worry about this its for the main mu later
    #if gamestart == 1:
    #    screen.fill((135, 206, 235))

        
    ###########
        #Example below is that the function is updating the plates movement by -5
        #pixels everytime the left arrow key is pressed.
    #if PLATE.Rect.collidelist(enemies):
     #   PLATE = Actor('level1')
    if game_status == game.state[0]:
        draw_main_menu()
        on_key_down()
    #if game_status == game.state[2]:
        
        
    

def draw():
    #this is the game drawing out all of the updates that are being made to the game.
    #the screen.clear is simply clearing out any after images of the objects moving in game.
    #screen.fill is just adding the background colors
    #gamestart=1
    #if gamestart == 1:
        #TITLESCREEN.draw()
    #if keyboard.RETURN:
    #TITLESCREEN.draw()
    screen.clear()
    if game_status == game.state[0]:
        draw_main_menu()
    if game_status == game.state[1]:
        #draw_main_menu()
        draw_game()
        draw_intruct()
        on_key_down()
        draw_time()
        draw_entities()
    if game_status == game.state[2]:
        draw_game_won()
        draw_credit()
        on_key_down()
    #if game_status == game.state[2]:
     #   on_key_down()
        
    #gamestart +=1
    #screen.draw.rect(BOX, RED)
            
pgzrun.go()

 ### IGNORE THIS AND BELOW Setup pygame/window ---------------------------------------- #


