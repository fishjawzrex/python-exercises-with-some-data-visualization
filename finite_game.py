from sys import exit

class Scene(object):
	'''	
	def enter(self):
		print "I don't know what he meant by" 
		print "subclass this shit."
		exit(1)
	'''


class First_Scene(Scene):
	def enter(self):
		print "This is the first scene and stuff of the"
		print "game, it is also the opening scene..."
		print "Do you want to advance to the next scene?"
		print "Hit ENTER to continue or ctrl + c to exit"
		raw_input(">> ")
		return 'scene_2'

class Second_Scene(Scene):
	def enter(self):
		print "yup, this is the second scene"
		print "advance?"
		raw_input(">> ")
		return 'scene_3'

class Final_Scene(Scene):
	def enter(self):
		print "this is the final scene..."
		print "congratulations!"
		exit(1)
		
class Map(object):
	cache = {'starting_scene':First_Scene(),
				'scene_2':Second_Scene(),
				'scene_3':Final_Scene()}
				
	def __init__(self, scene_name):
		self.scene_name = scene_name
				
	def next_scene(self, scene):
		return Map.cache.get(scene)
	def opening_scene(self):
		return self.next_scene(self.scene_name)
		
		
class Engine(object):
	def __init__(self, map_scene):
		self.map_scene = map_scene
	
	def play(self):
		current_scene = self.map_scene.opening_scene()
		
		while True:
			next_scene_loader = current_scene.enter()
			current_scene = self.map_scene.next_scene(next_scene_loader)

game_file = Map('starting_scene')
player = Engine(game_file)
player.play()