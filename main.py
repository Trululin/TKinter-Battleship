import tkinter as tk
import sys
from tkinter import messagebox as msg

from config import Config
from game_statistic import Game_Statistic
from ship import Ship
from player import Player
from board import Board
from loginPage import LoginPage
from checkAgain import CheckAgain
from addPlayer import AddPlayer
from leaderboard import LeaderBoard

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.appname)
		self.geometry(self.config.screen)

		self.create_container()
		self.create_menus()

		self.pages = {}

		self.create_loginPage()
		#self.create_board()
		#self.create_leaderboard()
		
		self.config.load_player(self.config.user_path)

	def change_page(self, page):
		pages=self.pages[page]
		pages.tkraise()

	def check_login(self):
		self.username = self.pages['loginPage'].var_username.get()
		self.password = self.pages['loginPage'].var_password.get()

		granted = self.config.login(self.username, self.password)
		if granted :
			self.create_board()
			self.change_page('board')

		else :
			self.create_checkAgain()
			self.change_page('checkAgain')

	def clicked_add_player(self):

		confirm = msg.askyesno('Battleship Player', 'Are you sure you want to add this Player ? ')

		if confirm :
			self.add_username = self.pages['addPlayer'].var_add_username.get()
			self.add_password = self.pages['addPlayer'].var_add_password.get()

			data = {
				"password" : self.add_password
			}

			self.config.player[self.add_username] = data

			self.config.save_player()

		self.change_page('loginPage')

	def create_menus(self):
		self.menuBar = tk.Menu(self)
		self.configure(menu=self.menuBar)

		self.fileMenu = tk.Menu(self.menuBar, tearoff = 0)
		self.fileMenu.add_command(label = "Exit", command=self.exit)
		self.fileMenu.add_command(label = "Add Player", command=self.new_player)
		self.fileMenu.add_command(label = "Play Again", command=self.play_again)

		self.helpMenu = tk.Menu(self.menuBar, tearoff = 0)
		self.helpMenu.add_command(label = "About", command=self.show_about_info)

		self.menuBar.add_cascade(label = "File", menu=self.fileMenu)
		self.menuBar.add_cascade(label = "Help", menu=self.helpMenu)

	def create_container(self):

		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):

		self.pages['board'] = Board(self.container, self.game)

	def create_loginPage(self):

		self.pages['loginPage'] = LoginPage(self.container, self)

	def create_checkAgain(self):

		self.pages['checkAgain'] = CheckAgain(self.container, self)

	def create_addPlayer(self):

		self.pages['addPlayer'] = AddPlayer(self.container, self)

	def create_leaderboard(self):

		self.pages['leaderboard'] = LeaderBoard(self.container, self)

	def show_about_info(self):

		msg.showinfo(" About Battleship App", "This app was created for project by lin \n\nCopyright 2021")

	def exit(self):
		respon = msg.askyesno("Exit Program", "Are you sure to close the program ?")
		if respon : 
			sys.exit()

	def new_player(self):
		respon = msg.askyesno("New Player", "Are you sure you want to add new Player? This page will be closed.")
		if respon :
			self.create_addPlayer()
			self.change_page('addPlayer')

	def play_again(self):
		respon = msg.askyesno("Play Again", "Are you sure to play again ?")
		if respon : 
			self.create_loginPage()
			self.change_page('loginPage')
			self.game.ship.setup_location()
			print(self.game.ship.location)

class Battleship : 

	def __init__(self):
		self.config = Config()
		self.game_statistic = Game_Statistic()
		self.ship = Ship(self)
		self.player = Player(self)
		self.window = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location

		if ship == player :
			return True
		return False

	def button_clicked(self, pos_x, pos_y):
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages['board'].change_img_button(pos_x, pos_y, win)

		self.username = self.window.pages['loginPage'].var_username.get()
		self.game_statistic.counter += 1
		counter = self.game_statistic.counter

		step = counter
		score = 100 - (step-1)*4

		stats = {
			self.username : {
				'steps' : step, 
				'score' : score
			}
		}

		if win:
			#sys.exit()
			respon = msg.askyesno('Save Data', 'Do you want to save data to leaderboard?')

			if respon :
				self.config.data.append(stats)

				self.config.save_leaderboard()

				self.window.create_leaderboard()
				self.window.change_page('leaderboard')

				self.game_statistic.steps = 0
				self.game_statistic.counter = 0

			else :
				msg.showinfo('Exit Game', 'To exit game, click File->Exit')



	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()