import tkinter as tk
from PIL import Image, ImageTk

class Board(tk.Frame):

	def __init__(self, parent, Game):

		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_mainframe()
		self.update_board()

	def create_mainframe(self):
		self.mainframe = tk.Frame(self, height=self.config.side, width=self.config.side, bg="black")
		self.mainframe.pack(expand=True)

	def create_board(self):
		self.frame_rows = []
		color = 756867

		n_row, n_column = self.config.row, self.config.column
		row_height, row_width = self.config.side//n_row, self.config.side

		for i in range(n_row):
			row_color = f"#{color}"
			frame = tk.Frame(self.mainframe, height=row_height, width=row_width, bg=row_color)
			self.frame_rows.append(frame)
			color += 500

	def show_board(self):
		for frame in self.frame_rows:
			frame.pack()

	def put_and_resize_photo(self, oriImg, scale):
		n_column = self.config.column
		button_width = self.config.side//n_column

		image = Image.open(oriImg)
		image_w, image_h = image.size
		ratio = image_w/button_width
		image = image.resize((int(image_w//ratio//scale), int(image_h//ratio//scale)))
		return ImageTk.PhotoImage(image)

	def change_img_button(self, pos_x, pos_y, win):
		if win:
			img = self.win_img_btn
		else : 
			img = self.final_img_btn
		self.button_board[pos_x][pos_y].configure(image=img)

	def create_button_board(self):
		self.button_board = []
		n_row, n_column = self.config.row, self.config.column
		button_height, button_width = self.config.side//n_row, self.config.side//n_column

		self.init_img_btn = self.put_and_resize_photo(oriImg=self.config.init_img_btn, scale=1)

		self.final_img_btn = self.put_and_resize_photo(oriImg=self.config.final_img_btn, scale=1)

		self.win_img_btn = self.put_and_resize_photo(oriImg=self.config.win_img_btn, scale=1)


		for i in range(n_row):
			row = []
			for j in range(n_column):
				button = tk.Button(self.frame_rows[i], bg="grey", image=self.init_img_btn, compound="c", height=button_height, width=button_width, command=lambda x=i, y=j:self.game.button_clicked(x, y))
				row.append(button)
			self.button_board.append(row)

	def show_button_board(self):
		n_row, n_column = self.config.row, self.config.column
		for i in range(n_row):
			for j in range(n_column):
				self.button_board[i][j].pack(side="left")

	def update_board(self):
		self.create_board()
		self.show_board()
		self.create_button_board()
		self.show_button_board()
		