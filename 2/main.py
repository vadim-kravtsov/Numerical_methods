from half_devide import half_devide_method
from math import sqrt

a, b  = [0.0, 1.0]
N = 100
A = -20
theta = 0.5 
h = (b-a)/N

X = [a+i*h for i in xrange(N+1)]
Y = [0.0 for _ in xrange(N+1)]
Z = [-1.0 for _ in xrange(N+1)]

c = [0.0, 0.0 , 0.0]
c[0] = (3.0/2.0*h*theta + (2.0*A*h**2*theta*(1.0-theta))/(1.0-A*h*(1.0-theta)) + 1.0)
c[1] = (3.0/2.0*h*(1.0-theta) + (2.0*A*h**2*(1.0-theta)**2)/(1.0-A*h*(1.0-theta)) - 1.0)
c[2] = -A*h*theta

G = lambda x: h*(x+theta*h)*sqrt((x+theta*h)**2+1)
grid = ((j[0], a+float(j[1])*(b-a)/N) for j in enumerate(xrange(0, N)))

for (i, x) in grid:
	F = lambda y: Y[i]*c[0] + y*c[1] + Z[i]*c[2] + G(X[i])+ sqrt((theta*Y[i]+(1.0-theta)*y)**2+1.0)
	Y[i+1] = half_devide_method(F)
	Z[i+1] = 1.0/(1.0-A*h*(1.0-theta))*(Z[i]*(1.0+A*h*theta) - Y[i]*2*h*theta - Y[i+1]*2*h*(1.0-theta) + h*(X[i]+theta*h)*sqrt((X[i]+theta*h)**2+1))
	print X[i], Y[i], Z[i]