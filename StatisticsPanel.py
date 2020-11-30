
import pygame as p
import math
import random as r
import dice
from dice import countsOfSix


WIDTH = 300
HEIGHT = 600
X = 600
Y = 0
countsOfSix = [0, 0, 0, 0, 0, 0]

BACKGROUND = p.Color("light gray")


def draw(screen):
    panel = p.Rect(X, Y, WIDTH, HEIGHT)
    p.draw.rect(screen, BACKGROUND, 
                p.Rect(X, Y, WIDTH, HEIGHT))
    font = p.font.SysFont("Arial", 20)
    

    text = ["Total Rolls:" + str(dice.NUM_OF_ROLLS),
            "",
            "Side 6 count: " + str(dice.countsOfSix[5]),
            "",
            "Side 5 count: " + str(dice.countsOfSix[4]),
            "",
            "Side 4 count: " + str(dice.countsOfSix[3]),
            "",
            "Side 3 count: " + str(dice.countsOfSix[2]),
            "",
            "Side 2 count: " + str(dice.countsOfSix[1]),
            "",
            "Side 1 count: " + str(dice.countsOfSix[0]),
            "",
            "Mode: " + str(mode(dice.countsOfSix)),
            "", "", "", "",   
            "Press space to start/stop", 
            " and 'r' to reset."] 
    
    for i in range(len(text)):
        textObject = font.render(text[i], 0, p.Color("black"))
        textLocation = panel.move(5, 20 * i)
        screen.blit(textObject, textLocation)


def mode(countsOfSix):
    max = 0
    for i in range(len(countsOfSix)):
        if countsOfSix[max] < countsOfSix[i]:
            max = i
    return max + 1

