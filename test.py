class StateSpace():
	def __init__(self):
		# the state space is a 3D matrix with X, Y and theta
		self.X = 3
		self.Y = 4
		# keep the intervals of 10 degrees in the grid
		self.theta = 50 
		self.pinit = 3 * 4 * 50 
		self.space = [[[0.0 for y in range(self.Y)] for x in range(self.X)] for t in range(5)]

	def rotation(self):
		for i in the range()


s = StateSpace()
print(s.initial_prior())
