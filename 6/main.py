import numpy as np
from math import sqrt, sin, pi, cos, log
import matplotlib.pyplot as plt
import pylab
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

a, b = [0,1]
koeff = int(input('Enter k: '))
n = koeff*10 				
#numb of layers
m = koeff**2*1000	
h = (b - a)/float(n)
tau = h**2/3
print(tau*m)
sigma = tau/h**2
x = [a+i*h for i in range(n+1)]
t = [i*tau for i in range(m+1)]
	

def phi(x):
	return 1.0/(1.0+x**2)**2

def explicit_method():
	U = np.empty((m+1, n+1))
	for i in range(n+1):
		U[0][i] =  phi(x[i])
	for k in range(1,m+1):
		for i in range(1, n):
			U[k][i] = (1-tau-2*sigma)*U[k-1][i]+sigma*U[k-1][i+1]+sigma*U[k-1][i-1]
		U[k][0] = (4*U[k][1]-U[k][2])/3.0
		U[k][n] = (4*U[k][n-1]-U[k][n-2])/3.0
	return U

def implicit_method():
	U = np.empty((m+1, n+1))
	for i in range(n+1):
		U[0][i] =  phi(x[i])
	for k in range(1,m+1):
		#alpha, beta = [-sigma/(1.0+2*sigma+tau)], [-U[k-1][0]/(1.0+2*sigma+tau)]
		alpha, beta = [1],[0]
		for i in range(1, n):
			alpha.append(sigma/(1-alpha[i-1]*sigma+2*sigma+tau))
			beta.append((sigma*beta[i-1]+U[k-1][i])/(1+2*sigma+tau-sigma*alpha[i-1]))
		alpha.append(1)
		beta.append(0)
		U[k][n] = ( -alpha[n] * beta[n-1] - beta[n] ) / ( alpha[n] * alpha[n-1] - 1 )
		for i in range(n-1,-1,-1):
			U[k][i] = alpha[i]*U[k][i+1]+beta[i]
	return U

def plot_surface(x, t, U):
	fig = pylab.figure()
	ax = Axes3D(fig)
	x, t = np.meshgrid(x, t)
	ax.plot_surface(x, t, U,cmap = cm.jet)
	ax.set_xlabel('x')
	ax.set_ylabel('t')
	ax.set_zlabel('U(x,t)')
	pylab.show()

def main():
	U = explicit_method()
	for i in range(0,n+1,koeff):
		print("%1.8f "%U[n+1][i], end = '')
	print('\n')
	#plot_surface(x, t, U)
	U = implicit_method()
	#plot_surface(x, t, U)
	for i in range(0,n+1,koeff):
		print("%1.8f "%U[n+1][i], end = '')
	print('\n')

main()