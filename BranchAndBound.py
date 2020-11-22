import argparse
import networkx as nx
import operator
import time
import os
import sys
import utils

def BnB(G, T):
    # start timer
    start_time = time.time()
    end_time = start_time
    delta_time = end_time - start_time
    solution_times = []

    # init solution vertex cover sets, empty frontier set, and upper bound
    frontier = []
    best_cost_solution = []
    curr_best = []
    upper_bound = G.number_of_nodes()

    # append init max degree node to frontier (node, state, (parent, state))
    g_copy = G.copy()
    v = max_degree_node(g_copy)
    frontier.append((v[0], 0, (-1, -1)))
    frontier.append((v[0], 1, (-1, -1)))

    while frontier != [] and delta_time < T:
        # choose node with the most promising configuration
        (vx, state, parent) = frontier.pop()
        backtrack = False

        # expand by making choices
        # if vx is not selected, make all neighbors = 1, store neighbors and remove from g_copy
        if state == 0:
            for node in list(g_copy.neighbors(vx)):
                curr_best.append((node, 1))
                g_copy.remove_node(node)
        # if vx is selected, make all neighbors = 0, remove from G
        elif state == 1:
            g_copy.remove_node(vx)
        else:
            pass

        curr_best.append((vx, state))
        curr_best_size = calc_vc_size(curr_best)

        # if solution found
        if g_copy.number_of_edges() == 0:
            if curr_best_size < upper_bound:
                best_cost_solution = curr_best.copy()
                print('Current best cost solution size: ', curr_best_size)
                upper_bound = curr_best_size
                solution_times.append([time.time() - start_time, curr_best_size])
            backtrack = True
        # if not, dead end
        else:
            curr_lb = calc_lower_bound(g_copy) + curr_best_size
            if curr_lb < upper_bound:
                # prune lb
                vy = max_degree_node(g_copy)
                frontier.append((vy[0], 0, (vx, state)))
                frontier.append((vy[0], 1, (vx, state)))
            else:
                # end of path, backtrack to parent
                backtrack = True

        # for each new config
        if backtrack == True:
            if frontier != []:
                nextnode_parent = frontier[-1][2]

                # backtrack to the level of nextnode_parent
                if nextnode_parent in curr_best:
                    idx = curr_best.index(nextnode_parent) + 1
                    while idx < len(curr_best):
                        mynode, mystate = curr_best.pop()
                        g_copy.add_node(mynode)
                        
                        # find all connected edges to vx in Graph G or edges connected to nodes not in current vc set
                        curVC_nodes = list(map(lambda t:t[0], curr_best))
                        for nd in G.neighbors(mynode):
                            # add edges of vx back to g_copy that were possibly deleted
                            if (nd in g_copy.nodes()) and (nd not in curVC_nodes):
                                g_copy.add_edge(nd, mynode)
                # backtrack to the root node
                elif nextnode_parent == (-1, -1):
                    curr_best.clear()
                    g_copy = G.copy()
                else:
                    print('Backtracking step error')

        # calculate total time
        end_time = time.time()
        delta_time = end_time-start_time
        if delta_time > T:
            print('Cutoff time reached')

    return best_cost_solution, solution_times

# find node with max degree in remaining graph
def max_degree_node(g):
    deglist = g.degree(g.nodes())
    v = ()
    max_degree = 0
    for i, j in deglist:
        if (j > max_degree):
            max_degree = j
            v = (i, j)
    return v

# calculate lower bound
def calc_lower_bound(graph):
    lb = graph.number_of_edges() / max_degree_node(graph)[1]
    if lb > int(lb):
        return int(lb) + 1
    else:
        return int(lb)

# calculate the size of a vertex covers defined as nodes with state = 1
def calc_vc_size(vc):
    vc_size = 0
    for element in vc:
        vc_size = vc_size + element[1]
    return vc_size

def main(inst, time, seed):
    # create graph
    g, adj_list, nodes, edges = utils.read_graph(inst)
    cutoff = 600

    # run branch and bound
    vertices, solution_times = BnB(g, cutoff)
    print(vertices, solution_times)

    # remove false nodes in vertex degree = 0
    for element in vertices:
        if element[1] == 0:
            vertices.remove(element)

    # convert to right format for writing
    vertex_cover = []
    for v, d in vertices:
        vertex_cover.append(v)
    print('vertex_cover: ', vertex_cover)
    print('trace_output: ', solution_times)

    # write outputs to file
    utils.writeOutput(inst, '_BnB_', cutoff, seed, vertex_cover, solution_times)