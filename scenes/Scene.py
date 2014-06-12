

class Scene:

	def __init__(self, game):
		self.__game = game
		self.__texts = []

	def render(self):
		pass

	def getGame(self):
		return self.__game

	def handleEvents(self, events):
		pass

	def clearText(self):
		self.__text = []

	def addText(self):
		pass	