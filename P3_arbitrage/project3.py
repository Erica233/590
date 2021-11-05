"""
Math 560
Project 3
Fall 2021

Partner 1: Fangting Ma (fm128)
Partner 2: Kaifeng Yu (ky99)
Date: Nov 4 2021
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
    # initialize
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None
    start_vertex = adjList[0]
    start_vertex.dist = 0

    #Bellman-Ford
    for iter in range(0, len(adjList) - 1):
        #change = 0
        for u in adjList:
            for neighbor in u.neigh:
                if neighbor.dist > u.dist + adjMat[u.rank][neighbor.rank] + tol:
                    neighbor.dist = u.dist + adjMat[u.rank][neighbor.rank]
                    neighbor.prev = u
                    #change = 1
    #detect cycle
    vertex_in_cycle = None
    for u in adjList:
        for neighbor in u.neigh:
            if neighbor.dist > u.dist + adjMat[u.rank][neighbor.rank] + tol:
                print("detect")
                vertex_in_cycle = neighbor
                break
        if vertex_in_cycle:
            print("break")
            break

    #find the cycle
    reverse_cycle = []
    if vertex_in_cycle:
        reverse_cycle += [vertex_in_cycle.rank]
        curr_vertex = vertex_in_cycle.prev
        while curr_vertex:
            if curr_vertex.rank in reverse_cycle:
                reverse_cycle += [curr_vertex.rank]
                print(reverse_cycle)
                break
            reverse_cycle += [curr_vertex.rank]
            curr_vertex = curr_vertex.prev
            print(reverse_cycle)

    #remove vertices not in the cycle, and reverse back
    cycle_path = []
    print(reverse_cycle[::-1])
    for rank in reverse_cycle[::-1]:
        if rank in cycle_path:
            cycle_path.append(rank)
            print("cycle path", cycle_path)
            break
        cycle_path.append(rank)
        print("cycle path", cycle_path)


    return cycle_path
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    #return [[R for R in row] for row in rates]
    list = [[R for R in row] for row in rates]
    ##### Your implementation goes here. #####
    #list = [[-math.log(R) for R in row] for row in rates]
    #print("rates2mat")
    print(list)
    #print("rates2mat end")
    return [[-math.log(R) for R in row] for row in rates]
    #return list

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
