#!/usr/bin/python
# CSE6140 Project
import time
import sys
import random
import networkx as nx
import os

class Graph:
    """ Vertex class is used to represent individual vertices during search"""
    def __init__(self, filename, random_seed):
        self.Graph = nx.Graph()
        random.seed(random_seed)
        self.adj_list = []
        with open(filename, 'r') as graph:
            i = 0
            for line in graph.readlines():
                if i == 0:
                    val = line.split()
                    self.nodes, self.edges, unweighted = int(val[0]), int(val[1]), int(val[2])
                    i += 1
                else:
                    self.adj_list.append(str(i) + ' ' + line)
                    i += 1
        self.Graph = nx.parse_adjlist(self.adj_list, nodetype=int)
    

    # ConstructVC method (Algorithm 2 from paper)
    def ConstructVC(self):
        VertexCover = []
        self.loss_function = dict.fromkeys(self.Graph.nodes(), 0)
        self.gain_function = dict.fromkeys(self.Graph.nodes(), 0)
        nx.set_edge_attributes(self.Graph, 0, 'covered')
        nx.set_node_attributes(self.Graph, 0, 'inSet')
        nx.set_node_attributes(self.Graph, 0, 'loss')
        nx.set_node_attributes(self.Graph, 0, 'gain')

        for edge in self.Graph.edges().data():
            if edge[2]['covered'] == 0:
                if self.Graph.degree(edge[0]) > self.Graph.degree(edge[1]):
                    addNode = edge[0]
                else:
                    addNode = edge[1]
                VertexCover.append(addNode)
                self.Graph.nodes().data()[addNode]['inSet'] = 1
                for neighbor in self.Graph.neighbors(addNode):
                    self.Graph[addNode][neighbor]['covered'] = 1
        
        for vertex in VertexCover:
            for neighbor in self.Graph.neighbors(vertex):
                if self.Graph.nodes().data()[neighbor]['inSet'] == 0:
                    self.Graph.nodes().data()[vertex]['loss'] += 1

        for vertex in VertexCover:
            if self.Graph.nodes().data()[vertex]['loss'] == 0:
                self.Graph.nodes().data()[vertex]['inSet'] = 0
                VertexCover.remove(vertex)
                for neighbor in self.Graph.neighbors(vertex):
                    if self.Graph.nodes().data()[neighbor]['inSet'] == 1:
                        self.Graph.nodes().data()[neighbor]['loss'] += 1
        
        return VertexCover

    # randomly sample 5 vertices and select onw with lowest loss to remove from cover
    # Follows BMS Heurisitc from paper (Algorithm 3)
    def pickRandomVertex(self, VertexCover):
        sampled_vert = random.choice(VertexCover)
        for i in range(5):
            selected_vert = random.choice(VertexCover)
            if self.loss_function[selected_vert] < self.loss_function[sampled_vert]:
                sampled_vert = selected_vert
        return sampled_vert

    def pickVertexFromUncoveredEdge(self, uncovered_edges):
        edge = random.choice(list(uncovered_edges))
        if self.Graph.nodes().data()[edge[0]]['gain'] > self.Graph.nodes().data()[edge[1]]['gain']:
            return edge[0]
        else:
            return edge[1]

    def removeVertex(self, VertexCover, vertex, uncovered_edges):
        for neighbor in self.Graph.neighbors(vertex):
            if self.Graph.nodes().data()[neighbor]['inSet'] == 1:
                self.Graph.nodes().data()[neighbor]['loss'] += 1
            else:
                self.Graph.nodes().data()[neighbor]['gain'] += 1 
                self.Graph.nodes().data()[vertex]['gain'] += 1
                self.Graph[vertex][neighbor]['covered'] = 0
                uncovered_edges.add((vertex,neighbor))
                uncovered_edges.add((neighbor,vertex))
        self.Graph.nodes().data()[vertex]['inSet'] = 0
        self.Graph.nodes().data()[vertex]['loss'] = 0
        VertexCover.remove(vertex)
        return VertexCover, uncovered_edges
    
    def addVertex(self, VertexCover, vertex, uncovered_edges):
        for neighbor in self.Graph.neighbors(vertex):
            if self.Graph.nodes().data()[neighbor]['inSet'] == 1:
                self.Graph.nodes().data()[neighbor]['loss'] -= 1
            else:
                self.Graph.nodes().data()[neighbor]['gain'] -= 1 
                self.Graph.nodes().data()[vertex]['gain'] -= 1
                self.Graph[vertex][neighbor]['covered'] = 1
                if (vertex,neighbor) in uncovered_edges or (neighbor,vertex) in uncovered_edges:
                    uncovered_edges.remove((vertex,neighbor))
                    uncovered_edges.remove((neighbor,vertex))
        self.Graph.nodes().data()[vertex]['inSet'] = 1
        self.Graph.nodes().data()[vertex]['gain'] = 0
        VertexCover.append(vertex)
        return VertexCover, uncovered_edges

class LocalSearch1:
    def __init__(self, filename, cutoff, random_seed):
        self.filename = filename
        self.graph = Graph(filename, random_seed)
        self.cutoff = cutoff
        self.random_seed = random_seed

    def writeOutput(self, VertexCover, trace_output):
        sol_file = "./Output/" + os.path.basename(self.filename)[:-6] + "_LS1_" + str(self.cutoff) + "_" + str(self.random_seed) + ".sol" 
        trace_file = "./Output/" +  os.path.basename(self.filename)[:-6] + "_LS1_" + str(self.cutoff) + "_" + str(self.random_seed) + ".trace" 
        with open(sol_file, 'w') as sol:
            sol.write(str(len(VertexCover)) + "\n")
            for vert in VertexCover[:-1]:
                sol.write(str(vert) + ",")
            sol.write(str(VertexCover[-1]))
        
        with open(trace_file, 'w') as trace:
            for time, quality in trace_output:
                trace.write(str(time) + "," + str(quality) + "\n")

    def main(self):
        trace_out = []
        uncovered_edges = set()

        # Construct cover
        VC = self.graph.ConstructVC()
        isVC = True
        start_time = time.time()
        elapsetime = 0
        while elapsetime < self.cutoff:
            if isVC:
                finalVC = VC.copy()
                trace_out.append([round(time.time() - start_time, 2), len(finalVC)])
                lossInVC = {key: value for key, value in self.graph.loss_function.items() if key in VC}
                min_vertex = min(lossInVC, key=lambda x: lossInVC[x])
                min_loss = self.graph.loss_function[min_vertex]
                VC, uncovered_edges = self.graph.removeVertex(VC, min_vertex, uncovered_edges)
            random_vert = self.graph.pickRandomVertex(VC)
            VC, uncovered_edges = self.graph.removeVertex(VC, random_vert, uncovered_edges)
            if len(uncovered_edges) > 0:
                new_vert = self.graph.pickVertexFromUncoveredEdge(uncovered_edges)
                VC, uncovered_edges = self.graph.addVertex(VC, new_vert, uncovered_edges)
            if len(uncovered_edges) > 0:
                isVC = False
            else:
                isVC = True
            elapsetime = time.time() - start_time
        self.writeOutput(finalVC, trace_out)





