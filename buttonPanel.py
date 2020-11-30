

import pygame as p 

WIDTH = 600
HEIGHT = 150
X = 0
Y = 600-150
BACKGROUND = p.Color('white')


def draw(screen, buttonNum):
    panel = p.Rect(X, Y, WIDTH, HEIGHT)
    p.draw.rect(screen, BACKGROUND, panel)
    button = p.Rect(0, 0, WIDTH//3, HEIGHT//2)

    if buttonNum == 1:
        startButton = button.clamp(panel).move(0, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["START"]
        textObjectGreen = font.render(text[0], 0, p.Color("black"))
        textLocation = startButton.move(50, 20)
        p.draw.rect(screen, p.Color("light green"), startButton)
        screen.blit(textObjectGreen, textLocation)

        stopButton = button.clamp(panel).move(WIDTH//3, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["STOP"]
        textObjectRed = font.render(text[0], 0, p.Color("black"))
        textLocation = stopButton.move(50, 20)
        p.draw.rect(screen, p.Color("red"), stopButton)
        screen.blit(textObjectRed, textLocation)

        resetButton = button.clamp(panel).move(2*WIDTH // 3, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["RESET"]
        textObjectBlue = font.render(text[0], 0, p.Color("black"))
        textLocation = resetButton.move(50, 20)
        p.draw.rect(screen, p.Color("DEEPSKYBLUE"), resetButton)
        screen.blit(textObjectBlue, textLocation)

    elif buttonNum == 2:
        startButton = button.clamp(panel).move(0, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["START"]
        textObjectGreen = font.render(text[0], 0, p.Color("black"))
        textLocation = startButton.move(50, 20)
        p.draw.rect(screen, p.Color("green"), startButton)
        screen.blit(textObjectGreen, textLocation)

        stopButton = button.clamp(panel).move(WIDTH//3, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["STOP"]
        textObjectRed = font.render(text[0], 0, p.Color("black"))
        textLocation = stopButton.move(50, 20)
        p.draw.rect(screen, p.Color("SALMON"), stopButton)
        screen.blit(textObjectRed, textLocation)

        
        resetButton = button.clamp(panel).move(2*WIDTH // 3, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["RESET"]
        textObjectBlue = font.render(text[0], 0, p.Color("black"))
        textLocation = resetButton.move(50, 20)
        p.draw.rect(screen, p.Color("DEEPSKYBLUE"), resetButton)
        screen.blit(textObjectBlue, textLocation)

    elif buttonNum == 3:
        startButton = button.clamp(panel).move(0, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["START"]
        textObjectGreen = font.render(text[0], 0, p.Color("black"))
        textLocation = startButton.move(50, 20)
        p.draw.rect(screen, p.Color("green"), startButton)
        screen.blit(textObjectGreen, textLocation)

        stopButton = button.clamp(panel).move(WIDTH//3, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["STOP"]
        textObjectRed = font.render(text[0], 0, p.Color("black"))
        textLocation = stopButton.move(50, 20)
        p.draw.rect(screen, p.Color("red"), stopButton)
        screen.blit(textObjectRed, textLocation)

        resetButton = button.clamp(panel).move(2*WIDTH // 3, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["RESET"]
        textObjectBlue = font.render(text[0], 0, p.Color("black"))
        textLocation = resetButton.move(50, 20)
        p.draw.rect(screen, p.Color("light blue"), resetButton)
        screen.blit(textObjectBlue, textLocation)

    else:
        startButton = button.clamp(panel).move(0, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["START"]
        textObjectGreen = font.render(text[0], 0, p.Color("black"))
        textLocation = startButton.move(50, 20)
        p.draw.rect(screen, p.Color("green"), startButton)
        screen.blit(textObjectGreen, textLocation)


        stopButton = button.clamp(panel).move(WIDTH//3, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["STOP"]
        textObjectRed = font.render(text[0], 0, p.Color("black"))
        textLocation = stopButton.move(50, 20)
        p.draw.rect(screen, p.Color("red"), stopButton)
        screen.blit(textObjectRed, textLocation)


        resetButton = button.clamp(panel).move(2*WIDTH // 3, HEIGHT//4)
        font = p.font.SysFont("Arial", 30, 1)
        text = ["RESET"]
        textObjectBlue = font.render(text[0], 0, p.Color("black"))
        textLocation = resetButton.move(50, 20)
        p.draw.rect(screen, p.Color("DEEPSKYBLUE"), resetButton)
        screen.blit(textObjectBlue, textLocation)
        
        
    return startButton, stopButton, resetButton
