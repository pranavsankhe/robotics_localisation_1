import math

def main():
	map = list()
	size = 57
	sigma = 0.75
	# assigning a prior probablity that is unifrom across the state space.
	prior = float(1 / (size*size))
	P = [[prior for j in range(size)]  for i in range(size)]
	
	# getting the measurement values from the file 
	path = '/Users/pranavsankhe/Downloads/ranges1.dat'
	with open(path) as book:
		content = book.read()  
	entries = content.split()

	# creating a list of measurements
	measurements = [float(entries[9 + i]) for i in range(6)]

	# for every measurement obtain the posterior probablity 
	for i in range(6):
		# P = beam(measurements[i], sigma)
		P = sense(P, measurements[i])
		P = observe(P, measurements[i])
		interpret(P)

# def beam(z, sigma):
# 	# q = []
# 	# for i in range(57):
# 	# 	temp = []
# 	# 	for j in range(57):
# 	p = gaussian(float(j/3), z, sigma)
# 	# 	temp.append(p)
# 	# q.append(p)
# 	return q

# this function is final 
def gaussian(x, sigma, z):
	gauss = 1/(math.sqrt(2 * math.pi * (sigma ** 2))) * math.exp(-0.5 * (x - z) ** 2 / (sigma) ** 2)
	return gauss 
	

# this function is final 
def sense(P, z):
	print(z)

	z = z * 3
	q = []
	for i in range(57):
		temp = []
		for j in range(57):
				temp.append(P[i][j] * gaussian(j, 0.75, z)) 
		q.append(temp)

	s = 0
	for i in q:
		s = sum(i)
	q = [[j/s for j in i] for i in q]
	return q 


def observe(P, r):
	q = []
	p_move = 0.75

	for i in range(len(P)):
		temp  = []
		for j in range(len(P[i])):
			if (i <=2 or j >=54):
				s = 0.25 * P[i][j]
			else:
				s = 0.75 * (P[i-3][ (j+3) ])
				s = s + (0.25 * (P[i][j]))
			temp.append(s)
		q.append(temp)
	return 


# final function 
def show(p):
	rows = ['[' + ','.join(map(lambda x: '{0:.8f}'.format(x),r)) + ']' for r in p]
	print ('[' + ',\n '.join(rows) + ']')

# this function is final 
def interpret(p):
	max = 0
	cord = []
	for i in range(len(p)):
		for j in range(len(p[i])):
			if p[i][j] > max:
				max = p[i][j]

				cord = [i/3 - 1, j/3 +1]
	print(cord)


if __name__ == "__main__":
	main()
