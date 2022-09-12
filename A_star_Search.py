import math as m
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

class PQ_node_object():
    def __init__(self,nodenumber):
        self.nodenumber = nodenumber
        self.parent = None
        self.actual_cost=m.inf
        self.total_cost=m.inf
    
    def setparent(self,parent_value):
        self.parent = parent_value
    
    def setactual_cost(self,actual_cost):
        self.actual_cost = actual_cost
    
    def settotal_cost(self,total_cost):
        self.total_cost = total_cost


@dataclass(order=True)
class PrioritizedItem:
	priority: int 
	item: Any=field(compare=False)

class A_star:
    def build_adj_list(self,filename):
        with open(filename,"r") as f:
            firstline = f.readline()
            self.nodes, self.edges=[int(eachvalue) for eachvalue in firstline.split()]

            self.adj_list = [ [] for eachnode in range(0, self.nodes+1) ]

            for eachline in range(self.edges):
                curline=f.readline()
                leftnode, rightnode, weight=[int(eachvalue) for eachvalue in curline.split()]

                self.adj_list[leftnode].append([rightnode, weight])
            
            self.heuristic_value=[]
            lastline=f.readline()
            self.heuristic_value=[int(eachvalue) for eachvalue in lastline.split()]
        
    def main_A_star(self,source_node,destination_node):
        source_node_object=PQ_node_object(source_node)
        source_node_object.setactual_cost(0)
        source_node_object.settotal_cost(self.heuristic_value[0])

        visited=[]
        pq=PriorityQueue()
        pq.put(PrioritizedItem(self.heuristic_value[0],source_node_object))

        while not pq.empty():
            popped_item=pq.get()
            poppedd_node_object=popped_item.item
            poppedd_node_number=poppedd_node_object.nodenumber

            if poppedd_node_number==destination_node:
                destination_node_object=poppedd_node_object
                print('Source Node=>',source_node, 'Destinationa Node=>',destination_node)
                print('Path')
                while destination_node_object.parent is not None:
                    print (destination_node_object.parent.nodenumber)
                    destination_node_object=destination_node_object.parent
                break
            if poppedd_node_number is visited:
                continue
            else:
                visited.append(poppedd_node_number)

                neighbor_list=self.adj_list[poppedd_node_number]
                for each_neighbor in neighbor_list:
                    neighbor_node_number=each_neighbor[0]
                    weight=each_neighbor[1]

                    neighbor_object=PQ_node_object(neighbor_node_number)
                    neighbor_object.setparent(poppedd_node_object)
                    neighbor_object.setactual_cost(poppedd_node_object.actual_cost+weight)
                    neighbor_object.settotal_cost(self.heuristic_value[neighbor_node_number-1]+neighbor_object.actual_cost)

                    pq.put(PrioritizedItem(neighbor_object.total_cost, neighbor_object))
                

my_obj=A_star()
my_obj.build_adj_list('a_star_graph.txt')
my_obj.main_A_star(1,5)