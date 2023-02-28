import pygame as pg

from .classes import Solider, Scout, Medic, Demoman, Heavy, Spy, Sniper, Pyro, Engineer

classes = {
	'solider'  : Solider,
	'scout'    : Scout,
	'medic'    : Medic,
	'demoman'  : Demoman,
	'heavy'    : Heavy,
	'spy'      : Spy,
	'sniper'   : Sniper,
	'pyro'     : Pyro,
	'engineer' : Engineer
}



class Player (Solider, Scout, Medic, Demoman, Heavy, Spy, Sniper, Pyro, Engineer) :
	def __init__ (self, name, team) :
		classes[name].__init__(self, team)


	def stringify (self) :
		return json.dumps({
			'pos' : self.pos
		})
