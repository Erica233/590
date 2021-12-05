"""
Math 560
Project 5
Fall 2021

Partner 1: Fangting Ma (fm128)
Partner 2: Kaifeng Yu (ky99)
Date: 3rd Dec, 2021
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    # initialize vertices
    for vertex in adjList:
        vertex.cost = math.inf
        vertex.prev = None
        vertex.visited = False
    # select and set the start vertex
    start = adjList[0]
    start.cost = 0

    # make the priority queue
    pqueue = PriorityQueue(adjList)

    while not pqueue.isEmpty():
        vertex = pqueue.deleteMin()
        vertex.visited = True
        for neighbor in vertex.neigh:
            if not neighbor.visited:
                if neighbor.cost > adjMat[vertex.rank][neighbor.rank]:
                    neighbor.cost = adjMat[vertex.rank][neighbor.rank]
                    neighbor.prev = vertex

    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    for vertex in adjList:
        makeset(vertex)
    X = []
    for edge in edgeList:
        u, v = edge.vertices
        if not find(u).isEqual(find(v)):
            X.append(edge)
            union(u, v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    ##### Your implementation goes here. #####
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    ##### Your implementation goes here. #####
    if not v.isEqual(v.pi):
        v.pi = find(v.pi)
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ##### Your implementation goes here. #####
    ru = find(u)
    rv = find(v)

    if ru == rv:
        return

    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        ru.pi = rv
        rv.height += 1
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    for vertex in adjList:
        vertex.visited = False

    tour = []
    stack = []

    start.visited = True
    stack.append(start)
    while len(stack) != 0:
        curr = stack.pop()
        tour.append(curr.rank)
        for neighbor in curr.mstN:
            if not neighbor.visited:
                neighbor.visited = True
                stack.append(neighbor)
    tour.append(start.rank)

    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
