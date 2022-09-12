from math import sqrt
def euclidean_distance(elm1, elm2):
  distance = 0.0
  for i in range(len(elm1)-1):
    distance += (elm1[i] - elm2[i])**2
  return sqrt(distance)

import numpy as np
import random

class KNN_Regression:

  #already implemented
  def read_data(self, filename):
    
    full_dataset = np.genfromtxt(filename, delimiter=",")

    self.training_data = []
    self.validation_data = []
    self.test_data = []

    for eachdata in full_dataset.tolist():
        rand_num=random.random() #0.0<=rand_num<1.0
        if rand_num < 0.7:
          self.training_data.append(eachdata)
        elif rand_num < 0.85:
          self.validation_data.append(eachdata)
        else:
          self.test_data.append(eachdata)

  #already implemented
  def main_knn(self, k, phase):

    if phase==1:
      dataset=self.validation_data
    else:
      dataset=self.test_data

    sum=0  

    for eachdata in dataset:
      actual_class=eachdata[-1]             #last column contains the real class of the datapoint
      predicted_class=self.predict_each_data(eachdata, k)
      #print(predicted_class)

      Squared_Error=(actual_class-predicted_class[-1])**2
      sum+= Squared_Error
    min_sqr_error=sum/len(dataset)
    return min_sqr_error
    #print(min_sqr_error)

 
  #just implement this method
  def predict_each_data(self, datapoint, k):
    distances=[]
    for eachdata in self.training_data:
      dist = euclidean_distance(datapoint, eachdata)
      distances.append((eachdata, dist))
    distances.sort(key=lambda x: x[1])
    neighbors=[]
    for i in range(k):
      neighbors.append(distances[i][0])
    np_array=np.array(neighbors)
    #print(np_array)
    avg=np_array.mean(axis=0)
    return avg.tolist()
    
regression = KNN_Regression()
regression.read_data("diabetes.csv")
min_error=float('inf')
best_k=-1
for i in [3,5,7,9,11,13,15]:
  error=regression.main_knn(i, 1)
  print("For k={}, Mean Squard Error={}".format(i,error))

  if error<min_error:
    min_error=error
    best_k=i


print("Lowest value of k =",best_k)

test_error=regression.main_knn(best_k, 2)
print("Test Error: ", test_error)  



