import os

class GameConstants:
	BALL_SIZE = [16, 16]
	BRICK_SIZE = [100, 30]
	PAD_SIZE = [139, 13]
	SCREEN_SIZE = [800, 600]

	SPRITE_BALL = os.path.join("Assets", "ball.png")
	SPRITE_BRICK = os.path.join("Assets", "standard.png")
	SPRITE_SPEEDBRICK = os.path.join("Assets", "speed.png")
	SPRITE_LIFEBRICK = os.path.join("Assets", "life.png")
	SPRITE_PAD = os.path.join("Assets", "pad.png")
	
	PLAYING_SCENE = 0
	GAMEOVER_SCENE = 1
	HIGHSCORE_SCENE = 2
	MAINMENU_SCENE = 3