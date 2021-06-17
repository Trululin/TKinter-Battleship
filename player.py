
class Player:

	def __init__(self, Game):
		self.game = Game
		self.statistics = Game.game_statistic

		self.counter()

	def current_location(self, pos_x, pos_y):
		self.location = (pos_x, pos_y)

	def counter(self):
		steps = int(self.statistics.steps)
		score = int(self.statistics.score)

		steps += 1
		score = score - 4*(steps-1)

		if steps == 25 :
			score = 0
			
		self.step = steps
		self.real_score = score