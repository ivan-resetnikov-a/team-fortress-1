import pygame as pg
pg.mixer.init()
pg.font.init()
pg.init()

import core

font = pg.font.Font('assets/fonts/pixeloid.ttf', 9)



class TF1 :
	def __init__ (self) :
		# config
		self.windowSize = (1920, 1080)
		self.renderSize = (480, 270)
		self.title = 'Team Fortress 1'

		self.fps = 60

		# initialise window
		self.window = pg.display.set_mode(self.windowSize, pg.FULLSCREEN)
		self.frame  = pg.Surface(self.renderSize)
		self.clock  = pg.time.Clock()


	def run (self) :
		self.onStart()
		self.runnning = True

		while self.runnning :
			for event in pg.event.get() :
				if event.type == pg.QUIT :
					self.runnning = False

			self.update()
			self.render()

		pg.mixer.quit()
		pg.font.quit()
		pg.quit()


	def update (self) :
		pass


	def render (self) :
		# update screen
		self.frame.fill((0, 0, 0))

		# render
		[player.render(self.frame) for player in self.players]

		self.frame.blit(font.render(str(round(self.clock.get_fps())), 0, (255, 255, 255)), (0, 0))

		# apply buffer
		self.window.blit(pg.transform.scale(self.frame, self.windowSize), (0, 0))
		self.clock.tick(self.fps)
		pg.display.flip()


	def onStart (self) :
		self.players = []

		self.players.append(core.Player('solider', 'red'))



TF1().run()