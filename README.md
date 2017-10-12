# Numerical methods labs

## 1. Second order ODE with boundary conditions.

We want to solve any ODE like this:

$$y''(x)+p(x)y'(x)+q(x)y(x) = f(x)$$
$$\alpha_0y(a)+\alpha_1y'(a)=A$$
$$\beta_0y(b)+\beta_1y'(b)=B$$

All we need is enter $$p,q,f,\alpha_0,\alpha_1,\beta_0,\beta_1, A, B$$ in our programm.

### Sample:

For:
$$y''+\frac{1}{x}y'+\frac{1}{2}y = \frac{1}{2}x^2 - \ln{x} + 4$$
$$y(0)+y'(0)=1$$
$$y(1)-\frac{1}{2}y'(1)=1.1137$$

We have:
~~~~{.python}
p = lambda x: 1.0/x
q =	lambda x: 0.5
f = lambda x: 0.5*(x**2) - log(x) + 4.0

alpha = [1.0, 1.0]
beta = [1.0, -0.5]
A, B = 1.0, 1.1137
~~~~