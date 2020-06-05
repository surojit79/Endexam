import scipy.integrate as scint
import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
        return np.vstack((y[1], 4*(y[0]-x)))

def bc(ya, yb):
	return np.array([ya[0], yb[0]-2])

x = np.linspace(0,1)
y = np.zeros((2, x.size))
Sol = scint.solve_bvp(f, bc, x, y)
y_e=(np.exp(2))*(np.exp(2*x)-np.exp(-2*x))/(np.exp(4)-1)+x#exact solution
plt.plot(x,Sol.sol(x)[0],'g-o',label=r'numerical solution')
plt.plot(x,y_e,'r',label=r'exact solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
