from shared import GameObject 
from shared import GameConstants

class Brick(GameObject):

	def __init__(self, position, sprite, game):
		self.__game = game
		self.__hitpoints = 100 #hitpoints bricks have
		self.__lives = 1 #lives bricks have\
		#Importing __init__ from GameObject 
		super(Brick, self).__init__(position, (GameConstants.BRICK_SIZE), sprite)

	def getGame(self):
		return self.__game

	def isDestroyed(self):
		return self.__lives <= 0

	def getHitPoints(self):
		return self.__hitpoints

	def hit(self):
		self.__lives -= 1

	def getHitSound(self):
		pass