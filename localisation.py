import math
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np 

class StateSpace():
	def __init__(self):
		# the state space is a 3D matrix with X, Y and theta
		self.X = 18*4
		self.Y = 18*8
		# keep the intervals of 10 degrees in the grid
		self.theta =360
		# p- intial is contributed by only X and Theta.
		self.pinit = 1/(self.X * self.Y * self.theta)
		self.data = []

	def intial(self):
		self.space = [[[self.pinit for y in range(self.Y)] for x in range(self.X)] for t in range(self.theta)]

	def sense(self, z):
		print('Range-value: {}'.format(z))
		sum = 0
		for t in range(self.theta):
			for x in range(self.X):
				for y in range(self.Y):
					self.space[t][x][y] = self.space[t][x][y] * self.beam(z, t, x/4)
					sum += self.space[t][x][y]

		for t in range(self.theta):
			for x in range(self.X):
				for y in range(self.Y):
					self.space[t][x][y] = self.space[t][x][y]/sum

	def beam(self, z, t, x):
		sigma = 0.25
		actual = x / (math.cos(self.deg2rad(t)))
		return self.gaussian(actual, sigma, z)


	def deg2rad(self, t):
		return (t * (math.pi / 180))

	def gaussian(self, a, sigma, z):
		gauss = (1 / (math.sqrt(2 * math.pi * (sigma ** 2))))* math.exp(-0.5 * (z - a) ** 2 / (sigma) ** 2)
		return gauss


	def motion(self, x, y, t):
		w = 2
		dt = 0.2 
		r = 0.5
		# multiplying to accomodate the change in the scale wrt the actual scale space and the velocity.
		x = x -   (r * math.sin(self.deg2rad(180 - t))) + (r * math.sin(self.deg2rad((180 - t) + w*(-dt))))
		y = y +   (r * math.cos(self.deg2rad(180 - t))) - (r * math.cos(self.deg2rad((180 - t) + w*(-dt))))
		t = t +   (w * (-dt))
		return t,x,y

	def observe(self):	
		for t in range(self.theta):
			for x in range(self.X):
				for y in range(self.Y):
					op = self.motion(x/4,y/4,(t))
					try:
						self.space[t][x][y] += self.space[round(op[0])][round(op[1] * 4)][round(op[2] * 4)]
					except IndexError:
						pass 
						 

	def interpret(self):
		max = -1
		cord = []
		for t in range(self.theta):
			for x in range(self.X):
				for y in range(self.Y):
					if (self.space[t][x][y] > max):
						max = self.space[t][x][y]
						cord = [t, x, y]
		return cord 

	def plot(self):
		self.data = [[0 for i in range(self.X)] for j in range(self.theta)]
		fig = plt.figure()
		ax = fig.add_subplot(111, projection = '3d')
		X = [i for i in range(self.X)]
		Y = [i for i in range(self.theta)]
		op = self.interpret()
		print('Predicted-distance: {}'.format(op[1]/4 - 4))
		print('Predicted-angle: {}'.format(op[0]))
		for t in range(self.theta):
			for x in range(self.X):
				self.data[t][x] = self.space[t][x][op[2]]
		z = np.array(self.data)
		x,y = np.meshgrid(X,Y)
		ax.plot_wireframe(x,y,z, rstride = 3, cstride = 3)
		plt.show()


s = StateSpace()
s.intial()
path = '/Users/pranavsankhe/School/Advanced Robotics/Homework 1/ranges2.dat'
with open(path) as book:
	content = book.read()  
entries = content.split()

# creating a list of measurements
measurements = [float(entries[9 + i]) for i in range(6)]

# for every measurement obtain the posterior probablity 
for i in range(6):
 
	s.sense(measurements[i])
	s.observe()
	s.plot()



