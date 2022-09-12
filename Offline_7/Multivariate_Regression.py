import numpy as np

class MultivariateLinearRegression:

  def __init__(self, filename):
    fulldataset = np.genfromtxt(filename,delimiter=",",skip_header = 1)
    dataset_size = fulldataset.shape[0]

    Y = fulldataset[:, -1]
    self.Y = np.array(Y)
    #s = self.Y.size
    #print(self.Y)
    x = fulldataset[:, :-1]
    self.x = np.matrix(x)
    #print(self.x)

    one_arr = np.matrix(np.ones((dataset_size,1)))
    self.X = np.concatenate((one_arr,self.x),axis=1)
    
    

  def MvLR_Model(self):
    tr = self.X.T
    #print(tr)
    B1 = tr @ self.Y
    #print(B1)
    mat_mul_x = tr @ self.X
    inv = np.linalg.inv(mat_mul_x)
    #print(inv)
    B = B1 @ inv
    print(B.T)
    
myob = MultivariateLinearRegression("MvLR - diabetes.csv")
myob.MvLR_Model()