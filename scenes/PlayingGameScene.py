import pygame
from scenes.Scene import Scene


class PlayingGameScene(Scene):

	def __init__(self, game):
		super(PlayingGameScene, self).__init__(game)

	def render(self):
		super(PlayingGameScene, self).render()

		game = self.getGame()

		for ball in game.getBalls():
			ball.updatePosition()

			game.screen.blit(ball.getSprite(), ball.getPosition())

		for bricks in game.getLevel().getBricks():
			game.screen.blit(bricks.getSprite(), bricks.getPosition())

	def handleEvents(self, events):
		super(PlayingGameScene, self).handleEvents(events)

		for event in events:
			if event.type == pygame.QUIT:
				exit()
