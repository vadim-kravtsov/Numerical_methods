import math

def simple_iter(f, a =1.0, e = 0.000000000001):
    y = f(a)
    c = abs(y-a)
    while c>e:
    	x = f(y)
    	c = abs(y-x)
    	y = x
    return(y)