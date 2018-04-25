import numpy as np
from math import sqrt, sin, pi, cos, log
import matplotlib.pyplot as plt
import pylab
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def phi(x):
	return 1.0/(1+x**2)**2

def heat_equation_solve():
	pass

def plot_surface(x, t, U):
	fig = pylab.figure()
	ax = Axes3D(fig)
	x, t = np.meshgrid(x, t)
	ax.plot_surface(x, t, U,cmap = cm.jet)
	pylab.show()

def main():
	a, b = [0,1]
	#numb of x
	n = 50 				
	#numb of layers
	m = 5000 	
	h = (b - a)/float(n)
	tau = h**2/3
	sigma = tau/h**2
	x = [a+i*h for i in range(n+1)]
	t = [i*tau for i in range(m+1)]
	U = np.empty((m+1, n+1))
	for i in range(n+1):
		U[0][i] =  phi(x[i])
	for k in range(1,m+1):
		for i in range(1, n):
			U[k][i] = (1-tau-2*sigma)*U[k-1][i]+sigma*U[k-1][i+1]+sigma*U[k-1][i-1]
		U[k][0] = (4*U[k][1]-U[k][2])/3.0
		U[k][n] = (4*U[k][n-1]-U[k][n-2])/3.0
	plot_surface(x, t, U)
	print(U)




main()