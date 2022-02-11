class GameStats:
	""" Track statistics for Alien Invasion."""

	def __init__(self, ai_game):

		# High score should nebver be reset.
		self.high_score = 0

		#Start Alien Invasion in active status
		self.game_active = True

		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start game in an inactive state
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1