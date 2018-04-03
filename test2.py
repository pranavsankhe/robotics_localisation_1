class Test():
	def __init__(self, a):
		self.a = a

	def __add__(self, obj): 
		return Test(self.a + obj.a)

	def __repr__(self):
		return 'This is what you input:{}'.format(self.a)

	def __mul__(self, obj):
		return Test(self.a * obj.a)

t = Test(3)
t2 = Test(4)
t3 = Test(5)
print(t + t2)
print(t * t2)
print(t * t3)

