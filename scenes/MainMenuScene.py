from scenes.Scene import Scene
import pygame
from shared import * #@UnusedWildImport

class MainMenuScene(Scene):

	def __init__(self, game):
		super(MainMenuScene, self).__init__(game)
		
		self.addText("1- Start Game", x = 300, y = 200, size = 30)
		self.addText("2- High Scores", x = 300, y = 240, size = 30)
		self.addText("ESC- Quit", x = 300, y = 260, size = 30)
		
		self.__menuSprite = pygame.image.load(GameConstants.SPRITE_MENU)
		
	def render(self):
		self.getGame().screen.blit(self.__menuSprite, (50,50))
		
		super(MainMenuScene, self).render()
		
	def handleEvents(self, events):
		super(MainMenuScene, self).handleEvents(events) #@UndefinedVariable
		
		for event in events: #@UndefinedVariable
			if event.type == pygame.QUIT:
				exit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit()
				
				if event.key == pygame.K_1:
					self.getGame().changeScene(GameConstants.PLAYING_SCENE)
				
				if event.key == pygame.K_2:
					self.getGame().changeScene(GameConstants.HIGHSCORE_SCENE)
					