from scenes.Scene import Scene
from HighScore import Highscore
from shared import GameConstants
import pygame

class HighscoreScene(Scene):

	def __init__(self, game):
		super(HighscoreScene, self).__init__(game)
		self.__highscoreSprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE) #@UndefinedVariable
		
	def render(self):
		self.getGame().screen.blit(self.__highscoreSprite,(50,50))
		
		self.clearText()
		
		highscore = Highscore()
		x = 350
		y = 100
		
		for score in highscore.getScores():
			self.addText(score[0], x, y, size= 30)
			self.addText(str(score[1]), x + 200, y, size=30)
			y +=30
			
		self.addText("Press mouse to start a new game", x, y +60, size = 30)
		
		super(HighscoreScene, self).render()
		
		
	def handleEvents(self, events):
		super(HighscoreScene, self).handleEvents(events)
		
		for event in events:
			if event.type == pygame.QUIT:
				exit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					self.getGame().reset()
					self.getGame().changeScene(GameConstants.MAINMENU_SCENE) #@UndefinedVariable
		