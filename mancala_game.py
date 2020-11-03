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

player_1 = front.setPlayerPosition(screen, 1100, 375, BLUE)
player_2 = front.setPlayerPosition(screen, 85, 125, RED)
player_2[:6] = player_2[5::-1]

def drawBoard():
    front.drawPlayer(player_1)
    front.drawPlayer(player_2)

def checkSquareClicked():
    cont = 0

    for obj in player_1:
        if obj.checkButtonClickOnSquare():
            return cont
        
        cont += 1

    return -1

def movePieces(positionInList):
    nPieces = player_1[positionInList].numberOfPieces

    if nPieces == 0:
        return

    player_1[positionInList].numberOfPieces = 0
    positionInList += 1

    while nPieces != 0:
        if positionInList <= 6:
            player_1[positionInList].numberOfPieces += 1
            nPieces -= 1
            positionInList += 1
        else:
            break

    if nPieces != 0:
        positionInList = 0

        while nPieces != 0:
            player_2[positionInList].numberOfPieces += 1
            nPieces -= 1
            positionInList += 1

    capturePieces(positionInList)

def capturePieces(positionInList):
    positionInList -= 1
    if positionInList <= 6 and player_1[positionInList].numberOfPieces == 1:
        player_1[6].numberOfPieces += player_2[5-positionInList].numberOfPieces
        player_1[6].numberOfPieces += player_1[positionInList].numberOfPieces
        player_1[positionInList].numberOfPieces = 0
        player_2[5-positionInList].numberOfPieces = 0

def checkWinner():
    summation = 0
    for obj in player_1:
        if obj.numberOfPieces != 0:
            summation += 1

    if summation == 1:
        if player_1[6].numberOfPieces > player_2[6].numberOfPieces:
            return "Parabéns, você venceu!"

        else:
            return "Que pena, você perdeu"

    return -1

def startGame():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    squareClicked = checkSquareClicked()

                    if squareClicked != -1:
                        movePieces(squareClicked)

        message = checkWinner()
        if isinstance(message, str): 
            print(message)

        drawBoard()
        pygame.display.update()

    pygame.quit()