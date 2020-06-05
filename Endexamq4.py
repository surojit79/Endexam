import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n=1024
x=np.linspace(0,1,1024)
y=np.random.rand(n)


k=2*np.pi*np.fft.fftfreq(n, d=1/(n-1))
dft=np.fft.fft(y,norm='ortho')
power_spec=(dft)**2/n

k_max, k_min = max(k), min(k)
print("k_max: ", k_max, "k_min: ", k_min)

plt.subplots()
plt.plot(x,y,'r',label=r'Random numbers')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

plt.subplots()
plt.plot(k,power_spec,'g',label=r'Power spectrum')
plt.xlabel('k')
plt.ylabel('Power_spectrum')
plt.legend()
plt.show()

plt.subplots()
plt.hist(power_spec,range=(k_min,k_max),bins=5,density=True,label=r'Histogram')
plt.xlabel('k')
plt.legend()
plt.show()




