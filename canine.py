class Canine(object):
	'''this is the original class/ super-class; Notice the
		lower-case object in the argument field. It has methods/
		funtions, __init__ that accept self, and age as arguments...
		has getter and setter methods, and a fun growl method that  you 
		can call and it prints the "GRRRR!"'''
	def __init__(self, age):
		self.age = age
		self.name = None 
		print "I am Canidae"
	
	def growl(self):
		print "GRRRR!"
	def get_name(self):
		return self.name
	def get_age(self):
		return self.age
	def set_name(self, newname):
		self.name = newname
	def set_age(self, newage):
		self.age = newage
		
	def __str__(self):
		return "Canid:" + "name: " + str(self.name) + " age: " + str(self.age)
		
		
class Wolf(Canine):#the class itself never takes any parameters
	'''this is a class/sub-class of The super-class Canine.
		it has additional custom methods like bite, howl, and
		it accepts self, age, and color as arguments or parameters
		it also had custom str and set_color methods'''
	def __init__(self, age, color):
		super(Wolf, self).__init__(age)#setting up parent class parameters in __init__ method 
		self.color = color #Initializing the extra parameter 
		self.tricks  = []
	def bite(self):
		action = raw_input("do you want a bite? ")
		#self.action = action
		if action == "yes":
			print "CHOMP!"
		else:
			print "wolf goes away..."
	def howl(self):
		return "WOOOOOOOOOOOOOOOOOOOOOOOF!!!"
	def add_trick(self, new_trick):
		self.tricks.append(new_trick)
	# you can change the color of this wolf		
	def set_color(self, new_color):
		self.color = new_color
	# now, we're going to overide the  __str__ method for the 
	# superclass Canine
	def __str__(self):
		return "This is a " +  str(self.color) + " wolf, and it is " + str(self.age) + " years old...and it's name is %s" % self.name
	