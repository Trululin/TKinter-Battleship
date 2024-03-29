import tkinter as tk
from tkinter import messagebox as msg

class AddPlayer(tk.Frame) :

	def __init__(self, parent, Game):
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="bisque")
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, height=self.config.side, width=self.config.side, bg="bisque")
		self.main_frame.pack(expand=True)

		self.label_add_username = tk.Label(self.main_frame, text="username", font=("Arial", 18, "bold"), bg="bisque", fg="black")
		self.label_add_username.pack(pady=5)

		self.var_add_username = tk.StringVar()
		self.entry_add_username = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), textvariable = self.var_add_username)
		self.entry_add_username.pack(pady=5)

		self.label_add_password = tk.Label(self.main_frame, text="password", font=("Arial", 18, "bold"), bg="bisque", fg="black")
		self.label_add_password.pack(pady=5)

		self.var_add_password = tk.StringVar()
		self.entry_add_password = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), textvariable = self.var_add_password)
		self.entry_add_password.pack(pady=5)

		self.btn_login = tk.Button(self.main_frame, text="Add", font=("Arial", 18, "bold"), command=lambda:self.game.clicked_add_player())
		self.btn_login.pack(pady=5)

