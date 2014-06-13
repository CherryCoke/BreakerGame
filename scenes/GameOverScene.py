from scenes.Scene import Scene
from shared import GameConstants
import pygame

class GameOverScene(Scene):

	def __init__(self, game):
		super(GameOverScene, self).__init__(game)
	
	def render(self):
		super(GameOverScene, self).render()
		
		self.clearText()
		self.addText("Press Mouse to restart", 400, 400, size=30)
		
	def handleEvents(self, events):
		super(GameOverScene, self).handleEvents(events)
		
		for event in events:
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					self.getGame().reset()
					self.getGame().changeScene(GameConstants.PLAYING_SCENE)
