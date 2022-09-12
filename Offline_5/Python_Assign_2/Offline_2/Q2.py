#===================Q2=============================
import numpy as np
A = np.random.rand(8,10)
C = A.T
B = np.random.rand(8,10)
matrix_multiply=C@B
print(matrix_multiply)
D = A>0.5
print(D)
print(A[ : ,[5,8]])
print(B[2:6,3:8])
sum_A=A.sum(axis=1)
print(sum_A.mean())