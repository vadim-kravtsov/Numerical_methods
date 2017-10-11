from math import exp, sin, pi

def p(x):
	return (1+x)/(2-x)

def q(x):
	return 1+exp(-x)

def f(x):
	return 1+sin((pi/2)*x)

def coefficients(N):
	a, b, c, d = [], [], [], []
	grid = (float(k)/N for k in xrange(N+1))
	for x in grid:
		print x, p(x)
		
coefficients(1000)