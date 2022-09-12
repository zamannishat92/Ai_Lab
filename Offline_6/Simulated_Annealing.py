import math as m
import random as r
class HC_Simulated_Annealing:
  
  def __init__(self, lst):
    self.lst=lst

  def calc_cost(self, lst):
    cst=0

    for ind in range(0, len(lst)):
        curitem=lst[ind]

        for ind1 in range(ind+1, len(lst)):
            nextitem=lst[ind1]
            if nextitem<curitem: 
              cst+=1

    return cst
    
  def random_child(self, lst):
    random_child_list=[]
    index1 = r.randrange(0,len(lst))
    #print(index1)
    index2 = r.randrange(0,len(lst))
    #print(index2)
    random_child_list=lst.copy()
    random_child_list[index1]=lst[index2]
    random_child_list[index2]=lst[index1]
    return random_child_list
    
  def SimulatedAnnealing(self):
    current_list = self.lst
    print(current_list)
    current_cost = self.calc_cost(current_list)
    print(current_cost)
    temp=100
    t=1
    while t<float('inf'):
      current_temp = temp-(.01*t)
      t+=1
      #print(current_temp)
      if current_temp<=0:
        break
      else:
        next_child = self.random_child(current_list)
        next_child_cost = self.calc_cost(next_child)
        diff = next_child_cost - current_cost
        if next_child_cost<current_cost:
          current_cost=next_child_cost
          current_list=next_child
        else:
          prob=m.exp((-(diff)/current_temp))
          randnum=r.random() 
          if randnum < prob:
            current_cost=next_child_cost
            current_list=next_child
          else:
            continue
    #print(current_list)
    return current_list
        
    
   
mylist=[100,-50,8,10,-20,200,50]
ob=HC_Simulated_Annealing(mylist)
result=ob.SimulatedAnnealing()
print(result) #your final output can be optimal / suboptimal