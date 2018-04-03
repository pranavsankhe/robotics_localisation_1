from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
X = [i for i in range(18*3 )]
Y = [i for i in range(18 * 3)]
x,y = np.meshgrid(X,Y)
z = np.sin(x ** 2 + y **2)
print(z)

# x,y,z = axes3d.get_test_data(0.1)
# print(x)

# x = [1,2,3,4,5,6,7]
# y = [1,2,3,4,5,6,7]
# z = [1,2,3,4,5,6,7]
ax.plot_wireframe(x,y,z, rstride = 1, cstride = 1)

# ax.scatter(X, Y, Z, c = 'r', marker = 'o')
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.set_zlabel('z-axis')

plt.show()

