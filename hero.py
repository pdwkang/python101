class Hero(object):
	def __init__(self):
		self.name = "Paul"

	def cheer_hero(self):
		print "Fight hard, " + self.name

def cheer_hero(hero):
		print "Global"
