import pygame,os,time

class Menu():
	def __init__(self,master,FPS,main_clock,font_,w,h):
		#Main Code
		self.window = master
		self.running = True
		self.FPS = FPS
		self.last_time = time.time()
		self.main_clock = main_clock
		self.font = font_
		self.main_width = w
		self.main_height = h
		self.pop_sound = pygame.mixer.Sound(
			os.path.join("Assets","POP.mp3"))

		#Menu Option Control Structure
		self.on_start = True
		self.on_about = False
		self.on_exit = False
		self.change = False

		#Menu Assets
		self.cursor = self.font.render("@",False,'black')
		self.start_text = self.font.render("START",False,'black')
		self.about_text = self.font.render("ABOUT",False,'black')
		self.exit_text = self.font.render("EXIT",False,'black')
		self.Main_Menu_text = self.font.render("Main Menu",False,'black')

	#Start Option
	def start(self):
		#Delta Time
		dt = time.time() - self.last_time
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		self.window.blit(self.cursor,(480,350))
		self.window.blit(self.start_text,(540,350))
		self.window.blit(self.about_text,(540,420))
		self.window.blit(self.exit_text,(540,490))
		self.window.blit(self.Main_Menu_text,(470,200))
		self.change = False

		#Events
		for event in pygame.event.get():
			#Quit Event
			if event.type == pygame.QUIT:
				self.running = False
			#State Chnage To About Option
			if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				self.on_start = False
				self.on_about = True
				self.on_exit = False
				self.pop_sound.play(0)
			#State Chnage To Exit Option
			if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				self.on_start = False
				self.on_about = False
				self.on_exit = True
				self.pop_sound.play(0)
			#Option Selection Event
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				self.change = True
			#FullScreen Events
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
				pygame.display.set_mode((0,0),pygame.FULLSCREEN)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F9:
				pygame.display.set_mode((self.main_width,self.main_height))

		#Updating the Display and Ticking the FPS
		pygame.display.update()
		self.main_clock.tick(self.FPS)

	#About Option
	def about(self):
		#Delta Time
		dt = time.time() - self.last_time
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		self.window.blit(self.cursor,(480,420))
		self.window.blit(self.start_text,(540,350))
		self.window.blit(self.about_text,(540,420))
		self.window.blit(self.exit_text,(540,490))
		self.window.blit(self.Main_Menu_text,(470,200))

		#Events
		for event in pygame.event.get():
			#Quit Event
			if event.type == pygame.QUIT:
				self.running = False
			#State Change To Exit Option
			if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				self.on_start = False
				self.on_about = False
				self.on_exit = True
				self.pop_sound.play(0)
			#State Change To Start Option
			if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				self.on_start = True
				self.on_about = False
				self.on_exit = False
				self.pop_sound.play(0)
			#Option Selection Event
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				pygame.display.set_mode((self.main_width,self.main_height))
				os.system("Data\\ABOUT.txt")
			#FullScreen Events
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
				pygame.display.set_mode((0,0),pygame.FULLSCREEN)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F9:
				pygame.display.set_mode((self.main_width,self.main_height))

		#Updating the Display and Ticking the FPS
		pygame.display.update()
		self.main_clock.tick(self.FPS)

	#Exit Option
	def exit(self):
		#Delta Time
		dt = time.time() - self.last_time
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		self.window.blit(self.cursor,(480,490))
		self.window.blit(self.start_text,(540,350))
		self.window.blit(self.about_text,(540,420))
		self.window.blit(self.exit_text,(540,490))
		self.window.blit(self.Main_Menu_text,(470,200))

		#Events
		for event in pygame.event.get():
			#Quit Event
			if event.type == pygame.QUIT:
				self.running = False
			#State Change To Start
			if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				self.on_start = True
				self.on_about = False
				self.on_exit = False
				self.pop_sound.play(0)
			#State Chnage To About
			if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				self.on_start = False
				self.on_about = True
				self.on_exit = False
				self.pop_sound.play(0)
			#Option Selection Event
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				self.running = False
			#FullScreen Events
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
				pygame.display.set_mode((0,0),pygame.FULLSCREEN)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F9:
				pygame.display.set_mode((self.main_width,self.main_height))

		#Updating the Display and Ticking the FPS
		pygame.display.update()
		self.main_clock.tick(self.FPS)

	#Menu Option Control Function
	def main_menu(self):
		#On Start Option
		if self.on_start == True:
			if self.on_about == False:
				if self.on_exit == False:
					self.start()
		#On About Option
		if self.on_start == False:
			if self.on_about == True:
				if self.on_exit == False:
					self.about()
		#On Exit Option
		if self.on_start == False:
			if self.on_about == False:
				if self.on_exit == True:
					self.exit()