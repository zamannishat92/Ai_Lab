import math as m
from queue import PriorityQueue


class PQ_Node:
	def __init__(self, nodenumber):
		self.node_number = nodenumber
		self.total_cost = m.inf
		self.parent = None 
		self.actual_cost=m.inf 

	def setparent(self,parentval):
		self.parent = parentval

	def update_cost(self,costval):
		self.actual_cost=costval

	def update_total_cost(self,costval):
		self.total_cost = costval

from dataclasses import dataclass,field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
	priority: int 
	item: Any=field(compare=False)

class A_Star:

	def __init__(self, src, dest):
		self.src_node=src
		self.goalnode=dest
		
		
	def build_adj_list(self,file_name):
		with open(file_name,"r") as f:
			firstline = f.readline()
			self.nodes,self.edges = [int(eachval) for eachval in firstline.split()]
			print(self.nodes, self.edges,self.goalnode)

			self.adj_list=[ [] for eachnode in range(0,self.nodes+1) ]
			self.heuristic_val=[]

			for eachline in range(self.edges):
				curline=f.readline()
				leftnode,rightnode,weight = [int(eachval) for eachval in curline.split()]
				self.adj_list[leftnode].append([rightnode,weight])

			
			lastline=f.readline()
			self.heuristic_val=[int(eachval) for eachval in lastline.split()]
			print(self.heuristic_val)

			for node in range(1,self.nodes+1):
				print(node,self.adj_list[node])



	def main_a_star(self):
		src_node_obj = PQ_Node(self.src_node)
		src_node_obj.update_total_cost(self.heuristic_val[0])
		src_node_obj.update_cost(0)

		E=[] #visited node track

		pq = PriorityQueue()
		pq.put(PrioritizedItem(self.heuristic_val[0],src_node_obj))

		while not pq.empty():
			popped_item = pq.get()
			popped_node_obj = popped_item.item
			popped_node_number = popped_node_obj.node_number

			if popped_node_number == self.goalnode:
				goal_node_obj = popped_node_obj
				while goal_node_obj.parent is not None:
					print(goal_node_obj.parent.node_number)
					goal_node_obj = goal_node_obj.parent
				break

			if popped_node_number in E:
				continue

			else:
				E.append(popped_node_number)

				neighbors_list = self.adj_list[popped_node_number]
				#print(neighbors_list )
				for eachneighbor in neighbors_list:
					neighbor_node_number = eachneighbor[0]
					#print(neighbor_node_number)
					edge_weight = eachneighbor[1]
					#print(edge_weight)

					neighbor_obj = PQ_Node(neighbor_node_number)
					neighbor_obj.setparent(popped_node_obj)
					neighbor_obj.update_cost(popped_node_obj.actual_cost+edge_weight)
					#print(popped_node_obj.actual_cost+edge_weight)
					neighbor_obj.update_total_cost(self.heuristic_val[neighbor_node_number-1]+neighbor_obj.actual_cost)
					#print(self.heuristic_val[neighbor_node_number-1]+neighbor_obj.actual_cost)
					
					pq.put(PrioritizedItem(neighbor_obj.total_cost,neighbor_obj))

ob=A_Star(1,5)
ob.build_adj_list("a_star_graph.txt")
ob.main_a_star()