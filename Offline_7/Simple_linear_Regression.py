import numpy as np
import matplotlib.pyplot as plt
import math as m

class SimpleLinearRegression:

  def __init__(self, filename):
    fulldataset = np.genfromtxt(filename,delimiter=",",skip_header = 1)
    dataset_size = fulldataset.shape[0]

    self.training_size = int(dataset_size*.80)
    self.training_data = fulldataset[0:self.training_size,:]

    self.test_size = dataset_size - self.training_size
    self.test_data = fulldataset[self.training_size: , : ]

    

  def SLR_Model(self):
    x = self.training_data[: , 0]
    avg_x = x.mean()
    diff_x = x - avg_x
    square = diff_x**2
    sum_x = square.sum()
    sx = (sum_x/(self.training_size-1))**0.5
    #print(sx)

    y = self.training_data[: , 1]
    avg_y = y.mean()
    diff_y = y - avg_y
    square = diff_y**2
    sum_y = square.sum()
    sy = (sum_y/(self.training_size-1))**0.5

    product=diff_x*diff_y
    sum=product.sum()
    r = (sum)/((sum_x*sum_y)**0.5)
    #print(r)

    self.w1 = r*(sy/sx)
    self.w0 = avg_y - (self.w1*avg_x)

    print(self.w1)
    print(self.w0)
    

  def plotModel(self):
    x = self.training_data[:,0]
    y = self.training_data[:,1]

    plt.scatter(x,y)
    #predicted value = w0 + w1 * user_input
    demo_x1 = x.min()
    predicted_y1 = self.w0 + (self.w1*demo_x1)
    demo_x2 = x.max()
    predicted_y2 = self.w0 + (self.w1*demo_x2)

    plt.plot([demo_x1,demo_x2],[predicted_y1,predicted_y2])
    plt.show()
    
myob = SimpleLinearRegression("SLR.csv")
myob.SLR_Model()
myob.plotModel()