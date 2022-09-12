import numpy as np
import matplotlib.pyplot as plt
import random

#-----------------------------------Start your implementation from here---------------------------------------------

class KmeansClustering:

  def __init__(self, num_clusters=1):
    '''Within this constructor declare an instance variable that will store the value of 'num_clusters' argument'''
    
  def read_data(self, file_name):
    '''Read all the data from the file 'file_name' as a 2D numpy array 
    and store the numpy array to an instance variable'''
    
  def initial_centers(self):
    '''Use the random.sample(...) function to randomly choose the initial cluster centers 
    and return the cluster centers as a 2D numpy array.'''
    
  def plot_initial_data(self, cluster_centers):
    '''Will scatter plot all the data points (already stored in instance variable of this class) 
    and also scatter plot all the 'cluster_centers' using a different symbol and color.'''
    
  def decide_cluster(self, point, cluster_centers):
    '''Will take input a 'point' and 'cluster_centers' data. 
    Calculate the distance from the point to all the other cluster_centers using Euclidean distance 
    and return the cluster number (0/1/2...) where the point belongs to.'''
    
  def cluster_formation(self, cluster_centers):
    '''Will take input the 'cluster_centers' and assign all the data points to the closest cluster.
    Return a dictionary of the following form:
    
    full_cluster={
      0:[[1,2],[3,4],[5,6]], #Key 0 is the cluster number and the values are the points of that cluster.
      1:[[7,8],[9,10]],
      ...
    }

    Steps:
    - Initialize full_cluster to an empty dictionary 
    - For each data point call the decide_cluster(...) function 
    and according to the return value of decide_cluster() assign the point to the appropriate cluster in full_cluster.
    '''
    
  def new_center(self, full_cluster):
    '''Will take input the full_cluster dictionary object as input 
    and will calculate the center for all the clusters. 
    It will return all the centers of the clusters as a 2D numpy array.'''
    
  def switch_counts(self, prevcluster, newcluster):
    '''Will take input two full_cluster objects and will compare them 
    and return the count of how many points have changed their groups.'''

  def kmeans_algo(self):
    '''
    1. Call the initial_centers(...) method to set the initial centers.
    2. Call the plot_initial_data(...) method to show the initial plot of the data
    3. Call the cluster_formation(...) method to build the initial cluster (for example, old_cluster)
    4. While True:
    5.      Call the new_center(...) method to calculate the new_centers from the old_cluster
    6.      Call the cluster_formation(...) method to again build updated cluster (for example, new_cluster)
    7.      Call the switch_counts(...) method to compare both the old and new clusters
    8.      If the total number of switches are less than 10 then exit from this while loop
    9.      Else set the new_cluster as old_cluster and rotate again
    10.End While
    11.return the old_cluster as your final result

    '''

  def plot_final_cluster(self, clusters):
    '''Will take input a full cluster dictionary object as input.
    For each cluster draw a different scatter plot and also show the centers of the each cluster'''
    
#---------------------------------------------End of your implementation--------------------------------------------------	



#Creating the object and calling necessary methods
#I have implemented this section for you ;)
obj=KmeansClustering(6)
obj.read_data("data.csv")                  #will read the data from the file and store in a 2D numpy array (for example, datapoints)
final_cluster=obj.kmeans_algo()            #calling the main kmeans clustering algorithm for cluster formation
obj.plot_final_cluster(final_cluster)      #will scatter plot all the clusters with corresponding centers

