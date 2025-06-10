STARTING_OPEN_SQUARE_NUMBER = 15
from Square import *
import random

class Game():
    START_LEFT = 35
    START_TOP = 35

    def __init__(self, window):
        self.window = window

        LEGAL_MOVES_DICT = {
            0:(1, 4),
            1:(0, 2, 5),
            2:(1, 3, 6),
            3:(2, 7),
            4:(0, 5, 8),
            5:(1, 4, 6, 9),
            6:(2, 5, 7, 10),
            7:(3, 6, 11),
            8:(4, 9, 12),
            9:(5, 8, 10, 13),
            10:(6, 9, 11, 14),
            11:(7, 10, 15),
            12:(8, 13, 16),
            13:(9, 12, 14),
            14:(10, 13, 15),
            15:(11, 14)
        }

        yPos = Game.START_TOP
        self.squareList = []

        for row in range (0, 4):
            xPos = Game.START_LEFT
            for col in range(0,4):
                squareNumber = (row * 4 ) + col
                legalMovesTuple = LEGAL_MOVES_DICT[squareNumber]
                oSquare = Square(self.window, xPos, yPos, squareNumber, legalMovesTuple)
                self.squareList.append(oSquare)
                xPos = xPos + SQUARE_WIDTH
            yPos = yPos + SQUARE_HEIGHT

        self.soundTick = pygame.mixer.Sound('sounds/tick.wav')
        self.soundApplause = pygame.mixer.Sound('sounds/applause.wav')
        self.soundNope = pygame.mixer.Sound('sounds/nope.wav')

        self.playing = False
        self.startNewGame()

    def startNewGame(self):
        for oSquare in self.squareList:
            oSquare.reset()

        self.oOpenSquare = self.squareList[STARTING_OPEN_SQUARE_NUMBER]

        for i in range(0, 200):
            legalMovesForThisTile = self.oOpenSquare.getLegalMoves()
            nextMoveNumber = random.choice(legalMovesForThisTile)
            print("OpenSquare:", self.oOpenSquare.getSquareNumber())
            print("LegalMoves:", legalMovesForThisTile)
            print("Next move:", nextMoveNumber)
            print("Jumlah squareList:", len(self.squareList))
            oSquare = self.squareList[nextMoveNumber]

            self.switch(oSquare, playMoveSound=False)

        self.playing = True

    def gotClick(self, clickLoc):
            if not self.playing:
                return
            
            for oSquare in self.squareList:
                if oSquare.clickedInside(clickLoc):
                    squareNumber = oSquare.getSquareNumber()
                    legalMovesForOpenSquareTuple = self.oOpenSquare.getLegalMoves()
                    legalMove = squareNumber in legalMovesForOpenSquareTuple
                    if legalMove:
                        self.switch(oSquare, playMoveSound=True)
                    else:
                        self.soundNope.play()
                    return
            
    def switch (self, oSquareToSwitch, playMoveSound=False):
        oSquareToSwitch.switch(self.oOpenSquare)
        self.oOpenSquare = oSquareToSwitch

        if playMoveSound:
            self.soundTick.play()

    def checkForWin(self):
        if not self.playing:
            return False
        
        for oSquare in self.squareList:
            if not oSquare.isTileInProperPlace():
                return False
            
        self.playing + False
        self.soundApplause.play()
        return True
    
    def getGamePlaying(self):
        returnself.playing

    def stopPlaying(self):
        selfPlaying = False

        def draw (self):
            for oSquare in self.squarelist:
                oSquare.draw()
        
