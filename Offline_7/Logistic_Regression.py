import numpy as np
import math as m

class LogisticRegression:

  def __init__(self, filename):
    self.fulldataset = np.genfromtxt(filename,delimiter=",")
    x_data = self.fulldataset[:,:4]
    x_size = x_data.shape[0]
    #print(X)
    Y = self.fulldataset[:,-1]
    Y_size = Y.shape[0]
    #print(Y)
    one_arr = np.ones((x_size,1))
    X = np.concatenate((one_arr,x_data),axis=1)
    X_size = X.shape[0]

    x_training_size = int(X_size*0.80)
    self.X_train = X[0:x_training_size,:]
    x_valid_size = x_training_size+10
    self.X_valid = X[x_training_size:x_valid_size,:]
    x_test_size = x_valid_size+10
    self.X_test = X[x_valid_size:x_test_size,:]

    #print(self.X_train)
    #print(self.X_valid)
    #print(self.X_test)

    Y_training_size = int(Y_size*0.80)
    self.Y_train = Y[0:Y_training_size]
    Y_valid_size = Y_training_size+10
    self.Y_valid = Y[Y_training_size:Y_valid_size]
    Y_test_size = Y_valid_size+10
    self.Y_test = X[Y_valid_size:Y_test_size]
    

  def Calculate_cost(self, theta):
    x_list = self.X_train.tolist()
    sum = 0
    for eachrow in x_list:
      index = np.where(eachrow)
      #print(index)
      z = (theta @ eachrow).sum()
      output =1/ (1+m.exp(-1*z))
      print(output)
      if output>0.5:
        self.predict=1
      else:
        self.predict=0
      sum+=(y*m.log(self.predict)) + ((1-y)*m.log(1-self.predict))
    finalcost=sum*(-1/self.x_training_size)
    #print(finalcost)
    return finalcost

  def LR_Train(self, learning_rate):
    dim = 4
    curTheta = np.random.rand(1,dim+1)
    print(curTheta)
    curCost = self.Calculate_cost(curTheta)
    c = 0
    while c!=2000:
      c+=1
      
      for x in self.X_train:
        if x is self.fulldataset:
          y = self.fulldataset[-1]
        slope = (y-self.predict)*x
        nextTheta = curTheta - (slope*learning_rate)
      newCost = self.Calculate_cost(nextTheta)
      if newCost>curCost:
        break
      else:
        curTheta=nextTheta
        curCost=newCost
    return curTheta

  def LR_Valid(self, learning_rate, Theta):
    x_list = self.X_valid.tolist()
    for eachrow in x_list:
      z = (theta*eachrow).sum()
      y=1/(1+m.exp(-1*z))

      if y>0.5:
        print(1)
      else:
        print(0)
        
    '''
    - receive the Theta value and learning_rate as parameter
    - using the received Theta value calculate the accuracy of the X_valid data
    - return the accuracy value
    '''

  def Best_learning_rate(self):
    LR=[0.1, 0.01, 0.001, 0.0001, 0.00001]
    
    self.bestTheta=None
    self.bestLR=None
    bestAccuracy=0

    for eachlr in LR:
      curTheta=self.LR_Train(eachlr)
      curAccuracy=self.LR_Valid(eachlr, curTheta)

      if curAccuracy>bestAccuracy:
        bestAccuracy=curAccuracy
        self.bestTheta=curTheta
        self.bestLR=eachlr

    
  def LR_test(self, learning_rate):
    '''
    Calculate the accuracy of the X_test dataset using the bestTheta, bestLR values. 
    Print the accuracy value.
    '''

myob=LogisticRegression("LR - iris.csv")
myob.Best_learning_rate()
myob.LR_test()