import networkx as nx
import os

def read_graph(filename):
    # contruct the graph based on adjacency list from the input file
    Graph = nx.Graph()
    adj_list = []
    with open(filename, 'r') as graph:
        i = 0
        for line in graph.readlines():
            if i == 0:
                val = line.split()
                nodes, edges, unweighted = int(val[0]), int(val[1]), int(val[2])
                i += 1
            else:
                adj_list.append(str(i) + ' ' + line)
                i += 1
    Graph = nx.parse_adjlist(adj_list, nodetype=int)
    # print(Graph.nodes())
    # print(Graph.edges())
    # print('No of nodes in G:', g.number_of_nodes(),'\nNo of Edges in G:', g.number_of_edges())
    return Graph, adj_list, nodes, edges

def writeOutput(filename, algo, cutoff, random_seed, vertex_cover, trace_output, folder):
    # write the solution and trace files
    print(folder)
    sol_file = folder + os.path.basename(filename)[:-6] + algo + str(cutoff) + "_" + str(random_seed) + ".sol" 
    trace_file = folder +  os.path.basename(filename)[:-6] + algo + str(cutoff) + "_" + str(random_seed) + ".trace" 
    with open(sol_file, 'w') as sol:
        sol.write(str(len(vertex_cover)) + "\n")
        for vert in vertex_cover[:-1]:
            sol.write(str(vert) + ",")
        sol.write(str(vertex_cover[-1]))
    
    with open(trace_file, 'w') as trace:
        for time, quality in trace_output:
            trace.write(str(time) + "," + str(quality) + "\n")