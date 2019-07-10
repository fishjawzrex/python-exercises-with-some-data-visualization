class Parent(object):
	
	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	
	def override(self):
		print "CHILD override()"
		
	def altered(self):
	#override
		print "CHILD, BEFORE PARENT altered()" 
	#calling the parent method with super()
		super(Child, self).altered()
	#second override protocol
		print "CHILD, AFTER PARENT altered()"
	
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()