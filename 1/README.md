# 1. Second order ODE with boundary conditions.

We want to solve any ODE like this:

![Link](http://latex.codecogs.com/png.latex?y''(x)&plus;p(x)y'(x)&plus;q(x)y(x)&space;=&space;f(x))

![Link](http://latex.codecogs.com/png.latex?\alpha_0y(a)&plus;\alpha_1y'(a)=A)

![Link](http://latex.codecogs.com/png.latex?\beta_0y(b)&plus;\beta_1y'(b)=B)

All we need is enter:

![Link](http://latex.codecogs.com/png.latex?a,b,p(x),q(x),f(x),\alpha_0,\alpha_1,\beta_0,\beta_1,&space;A,&space;B)  

in our programm.

### Sample:

For:

![Link](http://latex.codecogs.com/png.latex?y''&plus;\frac{1}{x}y'&plus;\frac{1}{2}y&space;=&space;\frac{1}{2}x^2&space;-&space;\ln{x}&space;&plus;&space;4)

![Link](http://latex.codecogs.com/png.latex?y(0)&plus;y'(0)=1)

![Link](http://latex.codecogs.com/png.latex?y(1)-\frac{1}{2}y'(1)=1.1137)

We have:
```python
p = lambda x: 1.0/x
q = lambda x: 0.5
f = lambda x: 0.5*(x**2) - log(x) + 4.0

alpha = [1.0, 1.0]
beta = [1.0, -0.5]
A, B = 1.0, 1.1137
```