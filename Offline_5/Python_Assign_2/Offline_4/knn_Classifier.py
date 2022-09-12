import numpy as np
import random

class KNN_Classifier:

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

    right_classify_cnt=0  #for accuracy calculation

    for eachdata in dataset:
      actual_class=eachdata[-1]             #last column contains the real class of the datapoint
      predicted_class=self.predict_each_data(eachdata, k)
      #print(predicted_class)

      if actual_class==predicted_class:
        right_classify_cnt+=1

    accuracy=right_classify_cnt/len(dataset)
    return accuracy

  def euclidean_distance(self,elm1, elm2):
    distance = 0.0
    for i in range(len(elm1)-1):
      distance += (elm1[i] - elm2[i])**2
    return distance
 
  #just implement this method
  def predict_each_data(self, datapoint, k):
    distances=list()
    for eachdata in self.training_data:
      dist = euclidean_distance(datapoint, eachdata)
      distances.append((eachdata, dist))
    distances.sort(key=lambda x: x[1])
    neighbors=[]
    for i in range(k):
      neighbors.append(distances[i][0])
    #print(neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction
    #print(prediction)



classifier = KNN_Classifier()
classifier.read_data("iris.csv")
max_accuracy=0
best_k=-1
for i in [3,5,7,9,11,13,15]:
  accuracy=classifier.main_knn(i, 1)
  print("For k={}, Validation Accuracy={}".format(i,accuracy*100))

  if accuracy>max_accuracy:
    max_accuracy=accuracy
    best_k=i

print("Best value of k =",best_k)

test_accuracy=classifier.main_knn(best_k, 2)
print("Test Accuracy: ", test_accuracy*100)

'''
    ==============REPORT=====================
    For k=3, Validation Accuracy=100.0
    For k=5, Validation Accuracy=100.0
    For k=7, Validation Accuracy=100.0
    For k=9, Validation Accuracy=96.0
    For k=11, Validation Accuracy=96.0
    For k=13, Validation Accuracy=96.0
    For k=15, Validation Accuracy=96.0

    From above,The Best value of k = 3

    Now i'm going to calculate the test accuracy for the value of k=3. 
    Test Accuracy:  95.23809523809523
'''
    
  
    