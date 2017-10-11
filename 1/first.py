from math import log, sin, pi
import matplotlib.pyplot as plt

p = lambda x: (1.0+x**2)
q =	lambda x: log(1+x)
f = lambda x: 1.0+x

alpha = [0.0, 0.5]
beta = [1.0, 0.0]
A, B = 1.0, 0.0


def thomas_algorithm(N, a = 0.0, b = 1.0):
	X = [float(j)/N for j in xrange(N+1)]
	Y = [0.0 for i in xrange(N+1)]
	m, k, c, d = [], [], [], []
	h = (b - a)/N
	dif = alpha[1]-alpha[0]*h
	
	m.append(-2.0 + h*p(a))
	k.append(1.0 - h*p(a)+(h**2)*q(a))
	c.append(dif/(m[0]*dif+k[0]*alpha[1]))
	d.append((k[0]*A*h)/dif+f(a)*(h**2))
	
	grid = ((j[0], float(j[1])/N) for j in enumerate(xrange(1, N-1)))
	
	for (i, x) in grid:
		print i,x
		m.append(-2.0 + h*p(x))
		k.append(1.0 - h*p(x) + (h**2)*q(x))
		c.append(1.0/(m[i] - k[i]*c[i-1]))
		d.append(f(x)*h**2 - k[i]*c[i-1]*d[i-1])
	
	Y[N] = (beta[1]*c[N-2]*d[N-2] + B*h)/(beta[1]*(1.0+c[N-2]) + beta[0]*h)
	
	for i in xrange(N-1,0,-1):
		Y[i] = c[i-1]*(d[i-1] - Y[i+1])
		print Y[i]
	Y[0] = (alpha[1]*Y[1] - A*h)/dif
	return X, Y

def plot_result(N):
	x, y = thomas_algorithm(N)
	plt.ylabel('y')
	plt.xlabel('x')
	plt.grid(True)
	plt.plot(x, y)
	plt.show()

plot_result(200)