from sys import exit


def dead(why):
	''' THIS "dead" FUNCTION IS USED TO BREAK OUT
	OF THE GAME LOOP WITH THE EXIT METHOD IMPORTED
	FROM THE "sys" MODULE'''
	print why, "Better luck next time!"
	exit(0)

	
def start():
	''' YOU CAN THINK OF THIS AS THE INITIALIZATION
	FUNCTION. IT'S THE SPARK PLUG THAT GETS THE 
	WHOLE ADVENTURE GAME RUNNING.'''
	print "You are a weary traveller and you are stranded in a desert..."
	print "You look ahead of you and you see a great Sphinx!"
	print "The Sphinx asks you a riddle: \n\'what goes up and never comes down?\'"
	res = raw_input(">> ")
	if res == "age": #explore how you can make this accept multiple queries.
		front_gate()
	else:
		dead("Wrong response, you got eaten by the Sphinx :(")
		
		
def front_gate():
	''' THIS GIVES YOU A CHOICE BETWEEN TWO DIFFERENT
	COLORED FLASKS'''
	print "Congratulations! You have been teleported to the front of\na great door with two flasks..."
	print "A red flask and a blue flask."
	resp = raw_input(">> ")
	if "take" and "blue" in resp:
		atrium()
	elif "take" and "red" in resp:
		dead("It's a trap you got blown up!")
	else:
		print "Sorry, I don't understand that input."
		front_gate()

def atrium():
	''' ATRIUM IS THE MEAT OF THE GAME PROGRAM, 
	IT USES ALL OF THE TOOLS FORM EX.35 AND 
	I EVEN BORROWED THE CTHULHU_ROOM() CODE;
	ON SECOND THOUGHT, I COULD HAVE JUST IMPORTED
	THE MODULE, SINCE THEY BOTH STORED IN THE SAME
	FOLDER OR DIRECTORY!'''
	sword_taken = False
	print "You are now in an Atrium with three doors..."
	print "door #1, #2, and #3..."
	while True:
		door = raw_input("Choose a door>> ")
		if door == "1":
			cthulhu_room()
		elif door == "2" and not sword_taken:
			print "There's an aggressive Troll guarding that door\nyou can't go through."
		elif door == "2" and sword_taken:
			action = raw_input("How are you going to get rid of this Troll?\n>> ")
			if "sword" in action:
				print "Filthy Troll is slain!\nYou proceed to enter into the room..."
				print "You find a hot chick with a million dollars in a brief case."
				print "You bang her brains out... The money is yours,\nshe is your gf, Congratulations!!!"
				exit(0)
			else:
				dead("Angry Troll bites your head off and rips your limb from limb.")
		elif door == "3" and not sword_taken:
			print "You see a great Ulbrecht Sword sitting in the corner"
			action = raw_input(">> ")
			print "You have retrieved the great Ulbrecht!"
			sword_taken = True
		else: 
			print "wtf bro!"
			
def cthulhu_room():
	''' BORROWED CODE FROM LPTHW'S EX.35'''
	print "Here you see the great evil Cthulhu."
	print "He, it , whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

start()