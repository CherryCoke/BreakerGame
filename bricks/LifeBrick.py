from bricks import Brick
from shared import GameConstants

class LifeBrick(Brick):

	def __init__(self, position, sprite, game):
		super(LifeBrick, self).__init__(position, sprite, game)

	def hit(self):

		game = self.getGame()
		game.increaseLives()

		super(LifeBrick, self).hit()
		
	def getHitSound(self):
		return GameConstants.SOUND_HIT_BRICK_LIFE
