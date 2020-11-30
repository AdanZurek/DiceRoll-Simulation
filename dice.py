'''
Created on Mar 3, 2019

@author: Adan
'''

import pygame as p 
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300
X = 0
Y = 0
DICE_NUMBER = 2
FIRST_DICE = 0
SECOND_DICE = 0
NUM_OF_ROLLS = 0 
countsOfSix = [0, 0, 0, 0, 0, 0]

dice6_one = p.image.load("D6-1.png")
dice6_two = p.image.load("D6-2.png")
dice6_three = p.image.load("D6-3.png")
dice6_four = p.image.load("D6-4.png")
dice6_five = p.image.load("D6-5.png")
dice6_six = p.image.load("D6-6.png")


already_rolled = False

def draw(screen):
    p.draw.rect(screen, p.Color('white'), p.Rect(X, Y, SCREEN_WIDTH, SCREEN_HEIGHT))
    
def roll_a_dice(screen):
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    global NUM_OF_ROLLS
    NUM_OF_ROLLS += 2
    display_dice(screen, dice1, dice2)

    
def display_dice(screen, first, second):
    display_first(screen, first)
    display_second(screen, second)

def display_first(screen, first):
    if (first == 1):
        screen.blit(dice6_one, ((SCREEN_WIDTH/2) - 100, SCREEN_HEIGHT/2))
        countsOfSix[0] += 1  
        return 1  
    elif (first == 2):
        screen.blit(dice6_two,((SCREEN_WIDTH/2) - 100,SCREEN_HEIGHT/2))
        countsOfSix[1] += 1
        return 2
    elif (first== 3):
        screen.blit(dice6_three,((SCREEN_WIDTH/2) - 100, SCREEN_HEIGHT/2))
        countsOfSix[2] += 1
        return 3
    elif (first == 4):
        screen.blit(dice6_four, ((SCREEN_WIDTH/2) - 100, SCREEN_HEIGHT/2))
        countsOfSix[3] += 1
        return 4
    elif (first == 5):
        screen.blit(dice6_five, ((SCREEN_WIDTH/2) - 100, SCREEN_HEIGHT/2))
        countsOfSix[4] += 1
        return 5
    elif (first == 6):
        screen.blit(dice6_six, ((SCREEN_WIDTH/2) - 100, SCREEN_HEIGHT/2))
        countsOfSix[5] += 1
        return 6
    
def display_second(screen, second):
    if (second == 1):
        screen.blit(dice6_one, ((SCREEN_WIDTH/2) + 100, SCREEN_HEIGHT/2))  
        countsOfSix[0] += 1
        return 1  
    elif (second == 2):
        screen.blit(dice6_two,((SCREEN_WIDTH/2) + 100, SCREEN_HEIGHT/2))
        countsOfSix[1] += 1
        return 2
    elif (second == 3):
        screen.blit(dice6_three,((SCREEN_WIDTH/2) + 100,SCREEN_HEIGHT/2))
        countsOfSix[2] += 1
        return 3
    elif (second == 4):
        screen.blit(dice6_four, ((SCREEN_WIDTH/2) + 100, SCREEN_HEIGHT/2))
        countsOfSix[3] += 1
        return 4
    elif (second == 5):
        screen.blit(dice6_five, ((SCREEN_WIDTH/2) + 100, SCREEN_HEIGHT/2))
        countsOfSix[4] += 1
        return 5
    elif (second == 6):
        screen.blit(dice6_six, ((SCREEN_WIDTH/2) + 100, SCREEN_HEIGHT/2))
        countsOfSix[5] += 1
        return 6

