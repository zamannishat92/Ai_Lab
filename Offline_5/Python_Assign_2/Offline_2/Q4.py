import numpy as np
import matplotlib.pyplot as plt
import random


class KmeansClustering:

  def __init__(self, num_clusters=1):
    self.k=num_clusters
    
  def read_data(self, file_name):
    self.datapoints=np.genfromtxt(file_name,delimiter=",")

  def initial_centers(self):
    init_center=random.sample(self.datapoints.tolist(),self.k)
    return np.array(init_center)

  def plot_initial_data(self,cluster_centers):
    x=self.datapoints[:,0]
    y=self.datapoints[:,1]

    plt.scatter(x,y,s=0.5,marker="*",label="initial data")

    

    cx=cluster_centers[:,0]
    cy=cluster_centers[:,1]

    plt.scatter(cx,cy,color="r",marker="^",label="center")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Initial data points")

    plt.legend()
    plt.show()
  
  def decide_cluster(self, point, cluster_centers):
    subtract_arr=cluster_centers-point
    squared_arr=subtract_arr**2
    summed_arr=squared_arr.sum(axis=1)
    return summed_arr.argmin()
    
  def cluster_formation(self, cluster_centers):
    full_cluster = {}
    for eachpoint in self.datapoints.tolist():
      point=eachpoint
      key=self.decide_cluster(point,cluster_centers)
      full_cluster[key]=point
    return full_cluster
    
  def new_center(self,full_cluster):
    data = list(full_cluster.items())
    fullcluster_nparr=np.array(data)
    new_center_coordinate=fullcluster_nparr.mean(axis=0)

  def switch_counts(self,prevcluster,newcluster):
    count1=0
    count2=0
    for point in prevcluster:
      count1 +=1
    for point in newcluster:
      count2 +=1

    return count2-count1
  
  def kmeans_algo(self):
    cluster_centers=self.initial_centers()
    self.plot_initial_data(cluster_centers)
    old_cluster=self.cluster_formation(cluster_centers)
    while True:
      newCenter=self.new_center(old_cluster)
      newcluster=self.cluster_formation(newCenter)
      if switch_counts(prevcluster,newcluster) <10:
        break
      else: 
       old_cluster=newcluster
    return old_cluster
        
  def plot_final_cluster(self, clusters):
    for key in clusters:
      points_list=clusters[key]
      numpy_list=np.array(points_list)
      x=numpy_list[:,0]
      y=numpy_list[:,1]
      
      plt.scatter(x,y,s=0.5,marker="*",label="Final data")
      cx=self.new_centers[:,0]
      cy=self.new_centers[:,1]
      plt.scatter(cx,cy,color="r",marker="^",label="center")
      plt.xlabel("x")
      plt.ylabel("y")
      plt.title("Final data points")
      plt.legend()
      plt.show()

obj=KmeansClustering(6)
obj.read_data("data.csv")
final_cluster=obj.kmeans_algo()            
obj.plot_final_cluster(final_cluster) 
      

    