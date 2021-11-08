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

This function will use Bellman-Ford algorithm to detect cycle, 
if there exists a cycle, it means there is an opportunity of arbitrage.
If there exists a cycle, it will return a list of cycle path,
otherwise it will return an empty list.

INPUTS
adjList: The adjacency list for the currencies.
adjMat: The adjacency matrix of edge weights for the graph.
tol: tolerance value (default = 1e-15)

OUTPUTS
returns the detected cycle path
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
    # initialize dist and prev for each vertex
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None

    # choose a start vertex, and set its dist to zero
    start_vertex = adjList[0]
    start_vertex.dist = 0

    # perform Bellman-Ford (iterate |v|-1 times)
    for iter in range(0, len(adjList) - 1):
        for u in adjList:
            for neigh in u.neigh:
                if neigh.dist > u.dist + adjMat[u.rank][neigh.rank] + tol:
                    neigh.dist = u.dist + adjMat[u.rank][neigh.rank]
                    neigh.prev = u

    # perform an extra iteration to detect cycle, and pick a vertex in a cycle
    vertex_in_cycle = None
    for u in adjList:
        for neigh in u.neigh:
            # if a dist of a vertex changes, a cycle is detected
            if neigh.dist > u.dist + adjMat[u.rank][neigh.rank] + tol:
                neigh.prev = u
                vertex_in_cycle = neigh
                break
        if vertex_in_cycle:
            break

    # find a cycle path backwards
    reverse_cycle = []
    if vertex_in_cycle:
        reverse_cycle += [vertex_in_cycle.rank]
        curr_vertex = vertex_in_cycle.prev
        while curr_vertex:
            # if find the start of a cycle
            if curr_vertex.rank in reverse_cycle:
                reverse_cycle += [curr_vertex.rank]
                break
            reverse_cycle += [curr_vertex.rank]
            curr_vertex = curr_vertex.prev

    # remove vertices not in the cycle, and reverse back
    cycle_path = []
    for rank in reverse_cycle[::-1]:
        if rank in cycle_path:
            cycle_path.append(rank)
            break
        cycle_path.append(rank)

    return cycle_path
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat

This function will transfer the matrix of exchange rates into edge weights, 
which are -log(exchange rate).

INPUTS
rates: the matrix of exchange rates

OUTPUTS
return a matrix of edge weights
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
