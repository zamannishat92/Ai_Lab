import math as m
class HillClimbing:
 
  def __init__(self, lst):
    self.lst = lst
   
  def calc_cost(self, lst):
    cst=0

    for ind in range(0, len(lst)):
        curitem=lst[ind]

        for ind1 in range(ind+1, len(lst)):
            nextitem=lst[ind1]
            if nextitem<curitem: 
              cst+=1

    return cst
    
  def minimum_cost_child(self, lst):
    best=[]
    new_cst=float('inf')
    cost_list=[]
    for ind in range(0,len(lst)):
      for ind1 in range(ind+1,len(lst)):
        best=lst.copy()
        best[ind]=lst[ind1]
        best[ind1]=lst[ind]
        #print(best)
        cost=self.calc_cost(best)
        cost_list.append((best,cost))
    min_cost_child_list=min(cost_list,key = lambda t: t[1])
    return min_cost_child_list[0]
    
        
    
    

  def SteepestDescent(self):
    current_list = self.lst
    print(current_list)
    current_cost = self.calc_cost(current_list)
    print(current_cost)
    while current_cost!=0:
      lowest_cost_child_list = self.minimum_cost_child(current_list)
      lowest_cost_value = self.calc_cost(lowest_cost_child_list)
      if lowest_cost_value<current_cost:
        current_cost=lowest_cost_value
        current_list=lowest_cost_child_list
      else:
        break
    return current_list
    
mylist=[100,-50,8,10,-20,200,50]
ob=HillClimbing(mylist)
result=ob.SteepestDescent()
print(result) #your final output can be optimal / suboptimal
    