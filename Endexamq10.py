import numpy as np
import matplotlib.pyplot as plt 
import math
def g(x):
	if abs(x)<= 1:
		return 1
	else:
		return 0
x_min = -10
x_max= 10
dx=np.array([0.1,0.02,0.01])

fig,axis = plt.subplots(3)

for i in range(3):
    h=dx[i]
    n=int((x_max-x_min)/h)+1
    f=np.zeros(n)
    x=np.linspace(x_min,x_max,n)

    for j in range(n):
        f[j]=g(x_min + j*h)

    dft = np.fft.fft(f, norm = 'ortho')
    k = 2*np.pi*np.fft.fftfreq(n, d = h)
    aft = h*np.exp(-1j*k*x_min)*dft*np.sqrt(n/(2*np.pi))


    axis[i].plot(k, np.real(aft), label =h)
    axis[i].set_xlabel("k")
    axis[i].set_ylabel("f(k)")
    axis[i].legend()

plt.show()


