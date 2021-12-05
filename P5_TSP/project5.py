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

This function will implement Prim's Algorithm, which is used to get 
the minimal spanning tree by finding the lightest cost edge 
leading out of the current tree then adding the edge to the tree.

INPUTS
adjList: a adjacency list of vertices.
adjMat: a adjacency matrix storing edge weights.

OUTPUTS
there is no return, it directly modifies the vertices' attributes
"""
def prim(adjList, adjMat):
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
        # get the next vertex
        vertex = pqueue.deleteMin()
        vertex.visited = True

        for neighbor in vertex.neigh:
            # if the edge leads out, update
            if not neighbor.visited:
                if neighbor.cost > adjMat[vertex.rank][neighbor.rank]:
                    neighbor.cost = adjMat[vertex.rank][neighbor.rank]
                    neighbor.prev = vertex


################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.

This function will implement Kruskal's Algorithm, which is used to get 
the minimal spanning tree by repeatedly adding the mininum cost edge 
that will not form a cycle, until there are no more edges can be added.

INPUTS
adjList: a adjacency list of vertices.
edgeList: a list of edges objects.

OUTPUTS
returns the MST, which is a list of edge objects
"""
def kruskal(adjList, edgeList):
    # initialize all singleton sets for each vertex
    for vertex in adjList:
        makeset(vertex)

    mst = []
    for edge in edgeList:

        # if the min edge crosses a cut, add it to MST
        u, v = edge.vertices
        if not find(u).isEqual(find(v)):
            mst.append(edge)
            union(u, v)

    return mst

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset

This function will create a singleton set with root v.

INPUTS
v: a vertex

OUTPUTS
there is no return
"""
def makeset(v):
    v.pi = v
    v.height = 0


"""
find
This function will return the root of the set that contains v.
Note: we will use path compression here.

INPUTS
v: a vertex

OUTPUTS
return the root vertex of the set that contains v
"""
def find(v):
    if not v.isEqual(v.pi):
        v.pi = find(v.pi)
    return v.pi

"""
union

This function will union the sets of vertices v and u.

INPUTS
u: a vertex
v: a vertex

OUTPUTS
there is no return
"""
def union(u,v):
    # find the roots of the trees for u and v
    ru = find(u)
    rv = find(v)

    if ru == rv:
        return

    # make shorter set point to taller set
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    # if both set have same height, arbitrarily break the tie
    else:
        ru.pi = rv
        rv.height += 1
    return

################################################################################

"""
TSP

This function will use depth first search to go through the MST 
to give an approximation solution to traveling salesman problem.

INPUTS
adjList: a adjacency list of vertices.
start: the start vertex

OUTPUTS
returns a list of vertex ranks representing the cycle tour sequence
"""
def tsp(adjList, start):
    # initialize the vertices
    for vertex in adjList:
        vertex.visited = False

    tour = []
    stack = []

    # visit the start vertex
    start.visited = True
    stack.append(start)

    while len(stack) != 0:
        # get the next vertex
        curr = stack.pop()
        tour.append(curr.rank)

        # visit its unvisited neighbors
        for neighbor in curr.mstN:
            if not neighbor.visited:
                neighbor.visited = True
                stack.append(neighbor)
                
    # return back to the start vertex
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
