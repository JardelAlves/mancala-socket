import pygame
import sys
from pygame.locals import *

WHITE = (255, 255, 255)

class Square:
    def __init__(self, screen, centerPosition, color = WHITE, numberOfPieces = 0):
        self.centerPosition = centerPosition
        self.color = color
        self.numberOfPieces = numberOfPieces
        self.screen = screen
        self.font = pygame.font.SysFont('Corbel', 100)

    def drawSquare(self):
        pygame.draw.circle(self.screen, self.color, self.centerPosition, 60)
        pygame.draw.rect(self.screen, self.color, (self.centerPosition[0] - 40, self.centerPosition[1] - 40, 80, 80))

    def drawKallah(self):
        pygame.draw.circle(self.screen, self.color, self.centerPosition, 60)
        pygame.draw.circle(self.screen, self.color, (self.centerPosition[0], self.centerPosition[1] + 250), 60)
        pygame.draw.rect(self.screen, self.color, (self.centerPosition[0] - 60, self.centerPosition[1], 120, 250))

    def displayNumberOfPieces(self):
        text = self.font.render(str(self.numberOfPieces), True, WHITE)
        textRect = text.get_rect(center = self.centerPosition)
        self.screen.blit(text, textRect)

    def displayNumberOfPiecesOnKallah(self):
        text = self.font.render(str(self.numberOfPieces), True, WHITE)
        textRect = text.get_rect(center = (self.centerPosition[0], self.centerPosition[1] + 125))
        self.screen.blit(text, textRect)

    def checkButtonClickOnSquare(self):
        mouse = pygame.mouse.get_pos()
        
        if self.centerPosition[0] - 40 <= mouse[0] <= self.centerPosition[0] + 40 and self.centerPosition[1] - 40 <= mouse[1] <= self.centerPosition[1] + 40: 
            return True

        else:
            return False

def setPlayerPosition(screen, player, positionKallah, positionY, color):
    positionX = 85
    for cont in range(6):
        player.append(Square(screen, (positionX + 145, positionY), color, 4))
        positionX += 145

    player.append(Square(screen, (positionKallah, 125), color))

def drawPlayer(player):
    for cont in range(6):
        player[cont].drawSquare()
        player[cont].displayNumberOfPieces()
        
    player[6].drawKallah()
    player[6].displayNumberOfPiecesOnKallah()