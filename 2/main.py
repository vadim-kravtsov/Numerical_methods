import matplotlib.pyplot as plt
from half_devide import half_devide_method
from simple_iter import *
from math import sqrt

a, b  = [0.0, 1.0]
theta = 0.5

def main(N):
	A = -1000.0 
	h = (b-a)/N
	
	X = [a+i*h for i in xrange(N+1)]
	Y = [1.0 for _ in xrange(N+1)]
	Z = [-10.0 for _ in xrange(N+1)]
	
	c = [0.0, 0.0 , 0.0, 0.0]
	c[0] = (3.0/4.0*h*(1.0-theta) + (A*theta*(1.0-theta)*h**2/2.0)/(1.0-A*theta*h/2) + 1.0)
	c[1] = (3.0/4.0*h*theta + (A*theta**2*h**2/2)/(1.0-A*theta*h/2) - 1.0)
	c[2] = -(A*h*(1.0-theta)/2 + ((2.0-theta)*A**2*h**2*theta/4)/(1.0-A*theta*h/2))
	c[3] = -((A*h**2*theta/4)/(1.0-A*h*theta/2))
	
	G = lambda x: (x+h/2.0)*sqrt((x+h/2.0)**2+1.0)
	grid = ((j[0], a+float(j[1])*(b-a)/N) for j in enumerate(xrange(0, N)))
	
	for (i, x) in grid:
		F = lambda y: -(Y[i]*c[0] + Z[i]*c[2] + c[3]*G(X[i]) + h/2.0*sqrt((theta*y+(1.0-theta)*Y[i])**2+1.0))/c[1]
		Y[i+1] = simple_iter(F)
		Z[i+1] = (1.0/(1.0-A*h*theta/2.0))*(Z[i]*(1.0+(1.0-theta)*A*h/2.0) 
			- Y[i]*h*(1.0-theta) 
			- Y[i+1]*h*theta 
			+ h/2*G(X[i]))
	return X, Y, Z

plt.title('The graphs of the solution of equation:')
plt.ylabel('y')
plt.xlabel('x')
plt.grid(True)
plt.xlim(a,b)

N = int(input('Enter N:'))
def plot_result(N):
	x, y, z = main(N)
	plt.plot(x, y)
	plt.plot(x, z)
X, Y, Z = main(N)
for i in xrange(N):
	print X[i], Y[i], Z[i] 

plot_result(N)
plt.savefig('result.png')
plt.show()
