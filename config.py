from json import load, dump

class Config : 

	def __init__(self):
		self.appname = "BattleShip"

		self.row = 5
		self.column = 5

		base = 150
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+200+0"

		self.login_pic = "img/login.jpg"
		self.init_img_btn = "img/init_img.jpeg"
		self.final_img_btn = "img/final_img.jpg"
		self.win_img_btn = "img/win_img.jpg"

		self.user_path = "json/player.json"
		self.data_path = "json/leaderboard.json"

		self.load_leaderboard()

	def load_player(self, path):
		with open(path, "r") as json_data:
			self.player = load(json_data)
		return self.player

	def save_player(self):
		with open("json/player.json", "w") as json_data:
			dump(self.player, json_data)

	def login(self, username, password):
		users = self.load_player(self.user_path)

		if username in users:
			if password == users[username]["password"]:
				return True
			else : 
				return False
		else : 
			return False

	def load_leaderboard(self):
		with open(self.data_path, "r") as file_json:
			self.data = load(file_json)

	def save_leaderboard(self):
		with open(self.data_path, "w") as file_json:
			dump(self.data, file_json)