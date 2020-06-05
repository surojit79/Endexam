import numpy as np
A=np.array([[2,1],[1,0],[0,1]])#1st matrix
B=np.array([[1,1,0],[1,0,1],[0,1,1]])#2nd matrix
U1, S1, V1=np.linalg.svd(A)
U2, S2, V2=np.linalg.svd(B)
print('Singular values for 1st matrix:',S1)
print('Singular values for 2nd matrix:',S2)
