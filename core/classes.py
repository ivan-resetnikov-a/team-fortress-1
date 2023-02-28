import pygame as pg



class Solider :
	def __init__ (self, team) :
		self.img = pg.image.load('assets/classes/solider/body.png').convert_alpha()
		
		teamImage = pg.image.load('assets/classes/solider/team.png').convert_alpha()

		colorMask = pg.Surface((16, 16))

		if   team == 'red'  : colorMask.fill((172, 50, 50))
		elif team == 'blue' : colorMask.fill((0, 0, 255))

		teamImage.blit(colorMask, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
		self.img.blit(teamImage, (0, 0))

		self.pos = [0, 0]
		self.vel = [0, 0]


	def render (self, frame) :
		frame.blit(self.img, self.pos)


class Scout :
	pass


class Medic :
	pass


class Demoman :
	pass


class Heavy :
	pass


class Spy :
	pass


class Sniper :
	pass


class Pyro :
	pass


class Engineer :
	pass

