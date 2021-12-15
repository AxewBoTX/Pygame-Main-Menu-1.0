from game import*

#Creating the Game Object
game = Game()

#Main Loop
while game.running == True:
	#Checking if the User is Starting the Game
	if game.starting == True:
		if game.playing == False:
			if game.lost == False:
				game.starting_window()
	#Checking if the User is Playing the Game
	if game.starting == False:
		if game.playing == True:
			if game.lost == False:
				game.game_window()
	#Checking if the User Lost the Game
	if game.starting == False:
		if game.playing == False:
			if game.lost == True:
				game.lost_window()