#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
import numpy as np
from numpy.linalg import norm
from numpy.linalg import inv
import math
import functools
import fractions

s = int(input('Enter s:'))
A=1.0

a=[[0]*s for _ in xrange(s)] 

for i in xrange(s):
	for k in xrange(s):
		if i == k:
			a[i][i] = 2.0/(i+1)
		else:
			a[i][k] = 1.0/((i+1)*(k+1)*(i+k+2)) + 1.0/((i+1)**2+(k+1)**2)
			a[k][i] = 1.0/((i+1)*(k+1)*(i+k+2)) + 1.0/((i+1)**2+(k+1)**2)

matrix = np.mat(a)
print matrix
w , v = np.linalg.eig(matrix) # где w - собств.значения, а v - собственные вектора
maxW = max(w,key=abs)
print 'theory lambdamax: %f'%maxW
minW = min(w,key=abs)
print 'lambdamin', minW

def firstmetod(A):

	X=np.array([1]*s)
	X.resize(s,1)

	x=np.dot(A,X)
	x1=float(x[0][0])
	d = norm(x,ord=2) - norm(X,ord=2)
	n=0

	while abs(d) > 0.00000001:   # 10^8
		X=x
		x=np.dot(A,X)
		x1=float(x[0][0])
		n=n+1
		res = x
		x=x/x1
		d = norm(X,ord=2) - norm(x,ord=2)
	print n
	return res

lambdamax = firstmetod(matrix)
maxl = lambdamax[0][0]
print lambdamax
print 'calc lambdamax: %f'%maxl   #%f-float

ainv = inv(matrix) #обратная матрица
lambdamin = firstmetod(ainv)
minl = lambdamin[0][0]

print 'calc lambdamin: %f'%minl 
