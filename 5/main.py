import numpy as np
from math import sqrt, sin, pi, cos, log
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from numpy.linalg import solve

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

def Ritz(K, f, n, a, b, alpha):
	X = [(1+cos(k*pi/(n-1)))/2.0 for k in range(n)]
	X.sort()
	#print(X)
	Y = [f(s) for s in X]
	A = np.zeros((n,n))
	B = np.zeros(n)
	for i in range(n):
		for j in range(n):
			firstIntegral = integrate.quad(lambda x: alpha*chebyshev(2.0*x-1.0, i)*chebyshev(2.0*x-1.0, j), a, b) 
			secondIntegral = integrate.quad(lambda t: K(X[i],t)*chebyshev(2.0*t-1.0, i), a, b)
			thirdIntegral = integrate.quad(lambda x: (secondIntegral[0]*chebyshev(2.0*x-1.0, j)), a, b)
			A[i][j] = firstIntegral[0] + thirdIntegral[0]
		integral = integrate.quad(lambda x: f(x)*chebyshev(2.0*x - 1.0, i), a, b) 
		B[i] = integral[0]
	#print(A)
	C = solve(A, B)
	print(C)
	U = lambda x: sum([C[i]*chebyshev(2.0*x-1.0, i) for i in range(0, len(C))])
	y = []
	N = 50
	x = np.linspace(a,b,N)
	for i in range(N):
		#c = 0
		#for j in range(n):
		#	#print(U(n, x[j]))
		#	c += U(n, x[j])#*chebyshev(2.0*x[i]-1,j)
		y.append(U(x[i]))
		#print('%1.8f  %1.8f'%(x[i], y[i]))
	return x, y

def main():
	al = np.linspace(0.1,0.01,20)
	a, b = [0,1]
	#alpha = 0.005
	n = int(input('Enter n: '))
	#al = [0.05, 0.01, 0.005]	
	for alpha in al:
		K = lambda x, t: 1.0/(2.0+x+t)
		f = lambda x: 1.0/(x+2)*log(2.0*(x+2.0)/(x+3.0))
		X, Y = Ritz(K, f, n, a, b, alpha)
		#n = [n for _ in range(n)]
		#Y = list(map(U, n, X))
		plt.grid(True)
		plt.plot(X,Y)
		plt.savefig('result%s.svg'%alpha)
	plt.show()

if __name__ == '__main__':
	main()