import tkinter as tk

class CheckAgain(tk.Frame):

	def __init__(self, parent, Game):
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="grey")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#create main frame
		self.main_frame = tk.Frame(self, height=self.config.side, width=self.config.side, bg="blue")
		self.main_frame.pack(expand=True)

		self.text = tk.Label(self.main_frame, bg="black", text="WRONG USERNAME OR PASSWORD, PLEASE TRY AGAIN", font=("Arial", 10, "bold"), fg="white")
		self.text.pack()

		self.back = tk.Button(self, text="CLICK ME", font=("Arial", 18, "bold"), command=lambda:self.game.change_page('loginPage'))
		self.back.pack(pady=5)