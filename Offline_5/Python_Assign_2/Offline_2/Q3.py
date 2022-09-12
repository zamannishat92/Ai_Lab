#====================Q3===========================
from matplotlib import pyplot as plt
import numpy as np
col2,col3,col4=np.genfromtxt("wine.csv", dtype=None,delimiter=",",usecols=(2,3,4),unpack=True)
plt.scatter(col2[:],col3[:],label="Col 2 & 3",marker="v")
plt.scatter(col2[:],col4[:],label="col 2 & 4",marker="x")

plt.xlabel("X - Axis(Col-2)")
plt.ylabel("Y - Axis(col3 & col4)")

plt.title("Scatter Plot")
plt.legend()

plt.show()
