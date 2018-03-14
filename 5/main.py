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
			firstIntegral = integrate.quad(lambda x: chebyshev(2.0*x-1.0, i)*chebyshev(2.0*x-1.0, j), a, b) 
			secondIntegral = integrate.dblquad(lambda x,t: K(x,t)*chebyshev(2.0*t-1.0, i)*chebyshev(2.0*x-1.0, j), a, b, lambda x: a, lambda x: b)
			A[i][j] = alpha*firstIntegral[0] + secondIntegral[0]
		integral = integrate.quad(lambda x: f(x)*chebyshev(2.0*x - 1.0, i), a, b) 
		B[i] = integral[0]
	#print(A)
	#print(B)
	C = solve(A, B)
	print(C)
	print(alpha)
	for line in A:
		for x in line:
			print('%1.3f'%x, end = ' ')
		print('')
	U = lambda x: sum([C[i]*chebyshev(2.0*x-1.0, i) for i in range(0, len(C))])
	y = []
	N = 50
	x = np.linspace(a,b,N)
	for i in range(N):
		y.append(U(x[i]))
	return x, y

def main():
	al = np.linspace(1e-1,1e-9,5)
	a, b = [0,1]
	eps = 1e-10
	#alpha = 0.005
	n = int(input('Enter n: '))
	#al = [1e-4]	
	for alpha in al:
		K = lambda x, t: 1.0/(2.0+x+t)
		f = lambda x: 1.0/(x+1)*log(2.0*(x+2.0)/(x+3.0))+eps*sin(100*x)
		X, Y = Ritz(K, f, n, a, b, alpha)
		#n = [n for _ in range(n)]
		#Y = list(map(U, n, X))
		plt.grid(True)
		plt.plot(X,Y)
		plt.savefig('result%s.svg'%alpha)
	plt.show()

if __name__ == '__main__':
	main()