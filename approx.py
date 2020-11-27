import os
import time
import networkx as nx
from utils import read_graph, writeOutput

# Extracted maximum degree function
# for modularity if we decide to 
# use a different metric/heuristic
def best_node(degrees):
    return max(degrees, key=degrees.get)

# Construction Heuristic for Greedy Algorithm
# Greedily selects node of highest degree 
def approximate_vertex_cover(G, T):
    start_time = time.time()
    t_delta = 0
    times = []
    degree_list = dict(nx.degree(G))
    vertex_cover = list()
    top = best_node(degree_list)
    while t_delta < T and degree_list[top] > 0:
        degree_list[top] = -1
        vertex_cover.append(top)
        for node in nx.neighbors(G, top):
            degree_list[node] -= 1
        top = best_node(degree_list)
        t_delta = time.time() - start_time
        times.append([t_delta, len(vertex_cover)])
    return vertex_cover, times

def measure_performance(instance, time, seed):
    G, _, _, _ = read_graph(instance)
    T = time * 60
    cover, times = approximate_vertex_cover(G, T)
    writeOutput(instance, '_CH_', T, seed, cover, times)
