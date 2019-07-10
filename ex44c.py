class Parent(object):

	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	
	def altered(self):
	#override
		print "CHILD, BEFORE PARENT altered()" 
	#calling the parent method with super()
		super(Child, self).altered()
	#second override protocol
		print "CHILD, AFTER PARENT altered()"
	
dad = Parent()
son = Child()

dad.altered()
son.altered()