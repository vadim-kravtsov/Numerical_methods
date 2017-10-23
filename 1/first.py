from math import log, sin, pi, exp
import matplotlib.pyplot as plt

p = lambda x: (x + 3.0/2.0)
q =	lambda x: (x+1.0)/(x+3.0)
f = lambda x: 4.0*x**3+11.5*x**2+17.0*x+8.5

alpha = [1.0, 0.0]
beta = [0.76, 1.0]
A, B = 3.0, 16.08
a, b = 0.0, 1.0

def thomas_algorithm(N, a = a, b = b, A = A, B = B ):
	X = [a+float(j)*(b-a)/N for j in xrange(N+1)]
	Y = [0.0 for i in xrange(N+1)]

	m, k, c, d, u, v = [], [], [], [], [], []
	h = (b - a)/N
	kap, nu = [], []
	
	r = (4.0 - 2.0*(2.0 - q(a+h)*h**2)/(2.0+p(a+h)*h))*alpha[1]
	z = 2.0*alpha[0]*h - 3.0*alpha[1] - alpha[1]*(p(a+h)*h - 2.0)/(2.0+p(a+h)*h)
	kap.append((-r/z))
	nu.append(((2.0*h*A + 2.0*alpha[1]*f(a+h)*(h**2)/(2.0 + p(a+h)*h))/z))

	r = (-4.0 + 2.0*(2.0 - q(b-h)*(h**2))/(2.0-p(b-h)*h))*beta[1]
	z = 2.0*beta[0]*h + 3.0*beta[1] - beta[1]*(p(b-h)*h + 2.0)/(2.0-p(b-h)*h)
	kap.append((-r/z))
	nu.append(((2.0*h*B - 2.0*beta[1]*f(b-h)*(h**2)/(2.0-p(b-h)*h))/z))

	u.append(kap[0])
	v.append(nu[0])

	print u, v
	grid = ((j[0], a+float(j[1])*(b-a)/N) for j in enumerate(xrange(0, N)))
	
	for (i, x) in grid:
		m.append(1.0 + (h/2.0)*p(x))
		k.append(2.0 - (h**2)*q(x))
		c.append(1.0 - (h/2.0)*p(x))
		d.append(((h**2)*f(x)))
	for i in xrange(1, N):
		u.append((m[i])/(k[i] - c[i]*u[i-1]))
		v.append(((c[i]*v[i-1]-d[i])/(k[i]-c[i]*u[i-1])))
	
	Y[N] = (-kap[1]*v[N-1]-nu[1])/(kap[1]*u[N-1]-1.0)
	
	for i in xrange(N-1, 0 ,-1):
		Y[i] = u[i]*Y[i+1] + v[i]

	Y[0] = u[0]*Y[1] + v[0]

	for i in xrange(N):
		print '%12e %12e'%(X[i],Y[i])
	return X, Y

plt.title('The graphs of the solution of equation:')
plt.ylabel('y')
plt.xlabel('x')
plt.grid(True)
plt.xlim(a,b)

def plot_result(N, a = a, b = b, A = A, B = B):
	x, y = thomas_algorithm(N, a, b, A, B)
	plt.plot(x, y)
	
plot_result(10)
plt.savefig('result.png')
plt.show()


#thomas_algorithm(320)