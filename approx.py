import os
import time
import networkx as nx

# Extracted maximum degree function
# for modularity if we decide to 
# use a different metric/heuristic
def best_node(degrees):
    return max(degrees, key=degrees.get)

# Construction Heuristic for Greedy Algorithm
# Greedily selects node of highest degree 
def approximate_vertex_cover(G):
    degree_list = nx.degree(G)
    vertex_cover = list()
    top = best_node(degree_list)
    while degree_list[top] > 0:
        degree_list[top] = -1
        vertex_cover.append(top)
        for node in nx.neighbors(G, top):
            degree_list[node] -= 1
        top = best_node(degree_list)
    return vertex_cover

