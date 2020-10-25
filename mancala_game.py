import mancala_front as front
import pygame
import sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (225, 25, 25)
BLUE = (25, 25, 225)
GREY = (235, 235, 235)

pygame.init()
screen = pygame.display.set_mode((1185, 500))
pygame.display.set_caption('Mancala')
screen.fill(GREY)

player_1 = []
player_2 = []

def drawBoard():
    front.setPlayerPosition(screen, player_1, 1100, 375, BLUE)
    front.setPlayerPosition(screen, player_2, 85, 125, RED)
    front.drawPlayer(player_1)
    front.drawPlayer(player_2)

def movePieces():
    nPieces = 0
    for obj in player_1:
        test = front.Square(screen, obj.centerPosition)
        if test.checkButtonClickOnSquare() == True:
            nPieces = obj.numberOfPieces
            obj.numberOfPieces = 0
            print("deu bom")

        if nPieces != 0:
            obj.numberOfPieces += 1
            nPieces -= 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    drawBoard()

    if event.type == pygame.MOUSEBUTTONDOWN:
        movePieces()
        
    pygame.display.update()

pygame.quit()