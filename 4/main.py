import numpy as np
from math import sqrt, sin, pi, cos
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def chebyshev(x, n):
	'''
	Chebyshev polynomials of the first kind. 
	n - order of polynom.
	'''
	if n == 0:
		y = 1
	elif n == 1:
		y = x
	else:
		y = 2.0*x*chebyshev(x, n-1)-chebyshev(x, n-2)
	return y

def fredgolm(a, b, f, n):
	'''
	Solve Fredholm Integral Equations of the Second Kind 
	by the collocation method.
	'''
	x = [(1+cos(k*pi/(n-1)))/2.0 for k in xrange(n)]
	y = [f(s) for s in x]
	M = np.zeros((n,n))
	for i in xrange(n):
		for j in xrange(n):
			integr = integrate.quad(lambda t: ((1.0/2.0*x[i]*t 
				   + 2*sqrt(1.0 + 1.0/12.0*(x[i]+t)))*chebyshev(2.0*t-1.0,j)), a, b)
			M[i][j] = chebyshev(2.0*x[i]-1.0,j) - integr[0]
	A = np.linalg.solve(M,y)
	y = []
	x = np.linspace(a,b,n)
	for i in xrange(n):
		c = 0
		for j in xrange(n):
			c += A[j]*chebyshev(x[i],j)
		y.append(f(x[i])-c)
		print '%1.8f  %1.8f'%(x[i], y[i])
	return x, y

def main():
	a, b = [0,1]
	f = lambda x: x+sqrt(1.0+x)
	n = int(input('Enter n: '))
	x, y = fredgolm(a,b,f,n)
	plt.grid()
	plt.plot(x,y,'o')
	plt.show()

if __name__ == '__main__':
	main()