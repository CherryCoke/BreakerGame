import os #@UnusedImport
import fileinput
import pygame
import random
from bricks import * #@UnusedWildImport 
from shared import * #@UnusedWildImport

class Level():

	def __init__(self, game):
		self.__game = game
		self.__bricks = []
		self.__amountOfBricksLeft = 0
		self.__currentLevel = 0

	def getBricks(self):
		return self.__bricks

	def getAmountOfBricksLeft(self):
		return self.__amountOfBricksLeft

	def brickHit(self):
		self.__amountOfBricksLeft -= 1

	def loadNextLevel(self):
		self.__currentLevel += 1
		fileName = os.path.join("Assets", "levels", "level" + str(self.__currentLevel) + ".dat")
		
		if not os.path.exists(fileName):
			self.loadRandom()
			
		else:
			self.load(self.__currentLevel)
		
	def loadRandom(self):
		
		self.__bricks = []

		x, y = 0, 0 #Setting x, y coordinates to find bricks
		
		maxBricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0])
		rows = random.randint(2, 8)
		amountOfSuperBricks = 0
		
		for row in range(0, rows): #@UnusedVariable
			for brick in range(0, maxBricks):
				brickType = random.randint(0, 3)
				
				if brickType == 1 or amountOfSuperBricks >= 3:
					brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
					self.__bricks.append(brick)
					self.__amountOfBricksLeft += 1
					
				elif brickType == 2:
					brick = SpeedBrick([x, y], pygame.image.load\
						(GameConstants.SPRITE_SPEEDBRICK), self.__game)
					self.__bricks.append(brick)
					amountOfSuperBricks += 1
					
				elif brickType == 3:
					brick = LifeBrick([x, y], pygame.image.load\
						(GameConstants.SPRITE_LIFEBRICK), self.__game)
					self.__bricks.append(brick)
					amountOfSuperBricks = 1

				x += GameConstants.BRICK_SIZE[0]
			x = 0
			y += GameConstants.BRICK_SIZE[1]

	def load(self, level):
		self.__currentLevel = level
		self.__bricks = []

		x, y = 0, 0 #Setting x, y coordinates to find bricks

		for line in fileinput.input(os.path.join\
			("Assets", "levels", "level" + str(level) + ".dat")):
			for currentBrick in line:
				if currentBrick == "1":
					brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
					self.__bricks.append(brick)
					self.__amountOfBricksLeft += 1
				elif currentBrick == "2":
					brick = SpeedBrick([x, y], pygame.image.load\
						(GameConstants.SPRITE_SPEEDBRICK), self.__game)
					self.__bricks.append(brick)
					self.__amountOfBricksLeft += 1
				elif currentBrick == "3":
					brick = LifeBrick([x, y], pygame.image.load\
						(GameConstants.SPRITE_LIFEBRICK), self.__game)
					self.__bricks.append(brick)
					self.__amountOfBricksLeft += 1

				x += GameConstants.BRICK_SIZE[0]
			x = 0
			y += GameConstants.BRICK_SIZE[1]
