 
def main():
	map = list()
	size = 18
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
		P = sense(P, measurements[i])


def beam():
	pass


def sense(P, z):

	pass


def observe(P, ):
	p_move = 0.75

	for i in range(len(map)):
		temp  = []
		for j in range(len(map[i])):
			pass
			#s = p_move * ()


if __name__ == "__main__":
	main()
