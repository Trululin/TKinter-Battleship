import tkinter as tk
from tkinter import messagebox as msg

class LeaderBoard(tk.Frame):

	def __init__(self, parent, Game):
		self.game = Game
		self.config = Game.config
		self.data_index = []
		self.update_mode = False
		self.current_data = self.config.data[0]
		self.last_current_data_index = 0

		super().__init__(parent)
		self.configure(bg="bisque")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, height=self.config.side, width=self.config.side, bg="bisque")
		self.main_frame.pack(expand=True)

		self.text_frame = tk.Frame(self.main_frame, height=self.config.side//4, width=self.config.side, bg="bisque")
		self.text_frame.pack(side="top", expand="True", fill="x")

		self.text = tk.Label(self.text_frame, bg="bisque", text="LeaderBoard", font=("Arial", 30, "bold"), fg="black")
		self.text.pack(expand=True, fill="y")

		self.content = tk.Frame(self.main_frame, height=3*self.config.side//4, width=self.config.side, bg="bisque")
		self.content.pack(side="top", expand=True, fill="x")

		self.leftpart = tk.Frame(self.content, height=self.config.side, width=self.config.side//3, bg="brown")
		#self.leftpart.pack(side="left", expand=True, fill="both")
		self.leftpart.grid(row=1, column=0, sticky="nsew")

		self.rightpart = tk.Frame(self.content, height=self.config.side, width=2*self.config.side//3, bg="green")
		#self.rightpart.pack(side="right", expand=True, fill="both")
		self.rightpart.grid(row=1, column=1, sticky="nsew")

		self.leftpart.grid_columnconfigure(0, weight=1)
		self.leftpart.grid_rowconfigure(1, weight=4)

		self.rightpart.grid_columnconfigure(1, weight=2)
		self.rightpart.grid_rowconfigure(1, weight=4)

		self.create_leftcontent()
		self.create_rightcontent()

	def create_leftcontent(self):
		frame_w = self.config.side//3
		frame_h = self.config.side

		self.left_content = tk.Frame(self.leftpart, width=frame_w, height=frame_h, bg="white")
		self.left_content.pack(fill="x")

		self.data_list_box = tk.Listbox(self.left_content, bg="white", fg="black", font=("Arial", 16), height=frame_h)
		self.data_list_box.pack(side="left", fill="both", expand=True)

		self.data_scroll = tk.Scrollbar(self.left_content)
		self.data_scroll.pack(side="right", fill="y")

		self.show_all_data_in_listbox()
	
		self.data_list_box.configure(yscrollcommand=self.data_scroll.set)
		self.data_scroll.configure(command=self.data_list_box.yview)

		self.data_list_box.bind("<<ListboxSelect>>", self.clicked_item_inListBox)

	def show_list_data_in_listbox(self):
		datas = self.config.data

		for index in self.data_index :
			data = datas[index]
			for name, info in data.items():
				name = name
				self.data_list_box.insert("end", name)

	def show_all_data_in_listbox(self):
		self.data_list_box.delete(0, 'end')
		datas = self.config.data
		self.data_index = []
		counter = 0
		for data in datas:
			self.data_index.append(counter)
			counter += 1
		self.show_list_data_in_listbox()

	def clicked_item_inListBox(self, event):
		if not self.update_mode:
			selection = event.widget.curselection()
			try : 
				clicked_item_index = selection[0]
			except IndexError:
				clicked_item_index = self.last_current_data_index

			index = self.data_index[clicked_item_index]
			self.last_current_data_index = index
			self.current_data = self.config.data[index]
			print(clicked_item_index, "==>", index)
			for name, info in self.current_data.items():
				username = name
				steps = info['steps']
				score = info['score']

			self.table_info[0][1].configure(text=username)
			self.table_info[1][1].configure(text=steps)
			self.table_info[2][1].configure(text=score)



	def create_rightcontent(self):
		frame_w = 2*self.config.side//3
		frame_h = self.config.side

		self.detail_content = tk.Frame(self.rightpart, width=frame_w, height=frame_h, bg="white")
		self.detail_content.pack(expand=True, fill="both")

		for name, info in self.current_data.items():
			info = [
				['Name :', name],
				['Steps :', info['steps']],
				['Score :', info['score']]
			]

		self.table_info = []
		rows, columns = len(info), len(info[0]) # 3, 2
		for row in range(rows):
			aRow = []
			for column in range(columns):
				label = tk.Label(self.detail_content, text=info[row][column], font=("Arial", 18), bg="white")
				aRow.append(label)
				if column == 0:
					sticky = "e"
				else:
					sticky = "w"
				label.grid(row=row, column=column, sticky=sticky)
			self.table_info.append(aRow)

		self.rightpart.grid_rowconfigure(0, weight=1)
		self.rightpart.grid_columnconfigure(0, weight=1)

		
