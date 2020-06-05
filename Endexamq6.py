import numpy as np
import matplotlib.pyplot as plt
def f1(x,y1,y2):
    return 32*y1+66*y2+2*x/3+2/3
def f2(x,y1,y2):
	return -66*y1-133*y2-x/3-1/3
a=0
b=0.5
h=0.01
n=int((b-a)/h)
x=np.linspace(a,b,n+1)
y1=np.zeros((n+1,))
y2=np.zeros((n+1,))
y1[0]=1/3
y2[0]=1/3


for i in range(n):
	k1=h*f1(x[i],y1[i],y2[i])
	l1=h*f2(x[i],y1[i],y2[i])
	

	k2=h*f1(x[i]+0.5*h,y1[i]+0.5*k1,y2[i]+0.5*l1)
	l2=h*f2(x[i]+0.5*h,y1[i]+0.5*k1,y2[i]+0.5*l1)
	

	k3=h*f1(x[i]+0.5*h,y1[i]+0.5*k2,y2[i]+0.5*l2)
	l3=h*f2(x[i]+0.5*h,y1[i]+0.5*k2,y2[i]+0.5*l2)
	

	k4=h*f1(x[i]+h,y1[i]+k3,y2[i]+l3)
	l4=h*f2(x[i]+h,y1[i]+k3,y2[i]+l3)
	

	y1[i+1]=y1[i]+(k1+2*k2+2*k3+k4)/6
	y2[i+1]=y2[i]+(l1+2*l2+2*l3+l4)/6
	

plt.plot(x,y1,color='r',label="y1")
plt.plot(x,y2,color='g',label="y2")
plt.xlabel("x")
plt.title("Runge-Kutta 4th order method")
plt.legend()
plt.grid()
plt.show()

