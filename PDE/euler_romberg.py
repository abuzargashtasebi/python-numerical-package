import numpy as np

'''
Solve y' = f(x, y) with initial condition y(x0)=y0 using the 
Euler-Romberg
'''
def euler_romberg(n, h, er, x0, y0):
    x = [x0] #initial conditions
    y = [y0] #initial conditions
    la = 10 #maximum number of subdivisions
    t = [0] * la
    nl = [0] #table of number of steps per abscissa
    for i in range(0, n):
        xc = x[i]
        yc = y[i]
        t[0] = y[i] + h * f(xc, yc)
        l = 0
        lm = 1
        et = 1.0
        while l < la and et >= er:
            xc = x[i]
            yc = y[i]
            for j in range(0,lm):
                xc += h / lm
                yc += h / lm * f(xc,yc)
            t[l+1] = yc
            k = l
            mm = 2
            et = 1.0
            if k > 0:
                while et >= er and k > 0:
                    t[k] = (mm * t[k+1] - t[k]) / (mm - 1)
                    et = abs(t[k] - t[k-1])
                    k -= 1
                    mm *= 2
            if k == 0:
                l += 1
                lm *= 2
        x.append(x[i] + h)
        y.append(t[k])
        nl.append(l)
    return x, y, nl

'''
Example: 
(Solve y' = x*x*y with y(0)=1 for x0=0 up to x1=1.0, 
exact solution is y = exp(x^3/3).
'''

# y' = f(x,y)
def f(x,y):
    return x * x * y

# exact solution
def fx(x):
    return np.exp(x**3 / 3)

x0 = 0
x1 = 1
y0 = 1 #value of y at x0
h = 0.2
er = 1.0e-6

ncalc = int((x1 - x0) / h)

x, y, nl =  euler_romberg(ncalc, h, er, x0, y0)

print("x \t y_estimate \t y_exact \t error \t n subdivisions")
for n in range(0, ncalc):
    yex = fx(x[n+1])
    ef = abs(yex - y[n+1])
    print("{:.1f}\t{:.6f}\t{:.6f}\t{:.8f}\t{}".format(x[n+1], y[n+1], yex, ef, nl[n+1]))