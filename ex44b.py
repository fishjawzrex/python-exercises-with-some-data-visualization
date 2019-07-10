class Parent(object):

	def override(self):
		print "PARENT override()"
		
class Child(Parent):
	def override(self):
		print "CHILD override()"
		print "You can override the parent class..."
		print "by giving the subclass's function the same name!"
	
dad = Parent()
son = Child()

dad.override()
son.override()