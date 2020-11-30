

import pygame as p
import dice
import buttonPanel
import StatisticsPanel


WIDTH = 900
HEIGHT = 600 
BACKGROUND_COLOR = 'white'
MAX_FPS = 5

def main():
    p.init()
    screen = p.display.set_mode([WIDTH, HEIGHT])
    p.display.set_caption('Dice Sim V. 1')
    screen.fill(p.Color(BACKGROUND_COLOR)) 
    clock = p.time.Clock()
    dice.draw(screen)
    buttons = buttonPanel.draw(screen, 0)
    rollingDice = False
    running = True
    while running:
        for event in p.event.get(): 
            if event.type == p.QUIT:
                running = False 
            if event.type == p.MOUSEBUTTONDOWN:
                for i in range(len(buttons)):
                    if buttons[i].collidepoint(event.pos):
                        if i == 0:
                            rollingDice = True
                            buttons = buttonPanel.draw(screen, 1)
                        elif i == 1:
                            rollingDice = False
                            buttons = buttonPanel.draw(screen, 2)
                        elif i == 2:
                            rollingDice = False
                            dice.countsOfSix = [0, 0, 0, 0, 0, 0]
                            dice.NUM_OF_ROLLS = 0
                            buttons = buttonPanel.draw(screen, 3)

            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    if rollingDice == True:
                        rollingDice = False
                        buttons = buttonPanel.draw(screen, 2)
                    elif rollingDice == False:
                        rollingDice = True
                        buttons = buttonPanel.draw(screen, 1)
                if event.key == p.K_r:
                    rollingDice = False
                    dice.countsOfSix = [0, 0, 0, 0, 0, 0]
                    dice.NUM_OF_ROLLS = 0
                    buttons = buttonPanel.draw(screen, 3)
                            
                            
        if rollingDice:
            dice.roll_a_dice(screen)
        StatisticsPanel.draw(screen)    
                  
                
        
        p.display.flip()
        clock.tick(MAX_FPS)
        
        
main()
