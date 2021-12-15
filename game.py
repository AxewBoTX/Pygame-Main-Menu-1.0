#Module Imports
import pygame,os,time
from Data.menu import*

class Game():
	def __init__(self):
		#Main Window
		pygame.mixer.pre_init(44100, -16, 2,512)
		pygame.init()
		pygame.mixer.init()
		pygame.font.init()
		self.main_width = 1200
		self.main_height = 700
		self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		pygame.display.set_caption("Window")

		#State Control Structure
		self.running = True
		self.starting = True
		self.playing = False
		self.lost = False

		#Game Assets
		self.FPS = 240
		self.last_time = time.time()
		self.main_clock = pygame.time.Clock()
		self.myfont = pygame.font.Font(
			os.path.join("Assets","font.ttf"),50)
		self.menu = Menu(
			self.window,self.FPS,self.main_clock,self.myfont,
			self.main_width,self.main_height)
		self.Game_Window_Text = self.myfont.render("GAME WINDOW",False,'black')
		self.LOST_Window_Text = self.myfont.render("LOST WINDOW",False,'black')

	#Starting Window
	def starting_window(self):
		#Close Event Control
		if self.menu.running == True:
			self.running = True
		elif self.menu.running == False:
			self.running = False
		if self.menu.change == True:
			self.starting = False
			self.playing = True
			self.lost = False
		self.menu.main_menu()

	#Game Window
	def game_window(self):
		#Delta Time
		dt = self.last_time - time.time()
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		self.window.blit(self.Game_Window_Text,(420,200))

		#Events
		for event in pygame.event.get():
			#Quit Event
			if event.type == pygame.QUIT:
				self.running = False
			#State Change Event
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				self.starting = False
				self.playing = False
				self.lost = True
			#FullScreen Events
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
				pygame.display.set_mode((0,0),pygame.FULLSCREEN)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F9:
				pygame.display.set_mode((self.main_width,self.main_height))

		#Updating the Display and Ticking the FPS
		pygame.display.update()
		self.main_clock.tick(self.FPS)

	#Lost Window
	def lost_window(self):
		#Delta Time
		dt = self.last_time - time.time()
		dt *= 240
		self.last_time = time.time()

		#Window Structure
		self.window.fill('white')
		self.window.blit(self.LOST_Window_Text,(420,200))

		#Events
		for event in pygame.event.get():
			#Quit Event
			if event.type == pygame.QUIT:
				self.running = False
			#State Chnage Event
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				self.starting = True
				self.playing = False
				self.lost = False
			#FullScreen Events
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
				pygame.display.set_mode((0,0),pygame.FULLSCREEN)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F9:
				pygame.display.set_mode((self.main_width,self.main_height))

		#Updating the Display and Ticking the FPS
		pygame.display.update()
		self.main_clock.tick(self.FPS)