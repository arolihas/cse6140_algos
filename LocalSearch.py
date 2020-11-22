# CSE6140 Project
import time
import sys
import random
import networkx as nx
import os
import utils

class Graph:
    """ Vertex class is used to represent individual vertices during search"""
    def __init__(self, filename, random_seed):
        self.Graph, self.adj_list, self.nodes, self.edges = utils.read_graph(filename)
        random.seed(random_seed)

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

    def maxIndSetInit(self, VertexCover, uncovered_vert):
        nx.set_node_attributes(self.Graph, 0, 'uncov') # tagx
        nx.set_node_attributes(self.Graph, 0, 'val')
        nx.set_node_attributes(self.Graph, 1, 'cov') # tagfree
        open_vert = []

        for vertex in uncovered_vert:
            self.Graph.nodes().data()[vertex]['uncov'] = 1
        for vertex in VertexCover:
            for neighbor in self.Graph.neighbors(vertex):
                if self.Graph.nodes().data()[neighbor]['uncov'] == 1:
                    self.Graph.nodes().data()[vertex]['cov'] = 0
                    self.Graph.nodes().data()[vertex]['val'] += 1
            if self.Graph.nodes().data()[vertex]['cov'] == 1:
                open_vert.append(vertex)
        
        return open_vert
    
    def minValVertex(self, covered_vertices):
        sampled_vertex = random.choice(covered_vertices)
        min_val_vert = sampled_vertex
        min_val = self.Graph.nodes().data()[min_val_vert]['val']
        for i in range(5):
            sampled_vertex = random.choice(covered_vertices)
            new_val = self.Graph.nodes().data()[sampled_vertex]['val']
            if new_val < min_val:
                min_val = new_val
                min_val_vert = sampled_vertex
        return min_val_vert
    
    def updateIndSet(self, uncovered_vertices, open_vertices, min_value_vertex):
        for vertex in self.Graph.neighbors(min_value_vertex):
            self.Graph.nodes().data()[vertex]['val'] += 1
            if self.Graph.nodes().data()[vertex]['uncov'] == 1:
                for neighbor in self.Graph.neighbors(vertex):
                    if neighbor != min_value_vertex:
                        self.Graph.nodes().data()[neighbor]['val'] -= 1
                self.Graph.nodes().data()[vertex]['cov'] = 0
                self.Graph.nodes().data()[vertex]['uncov'] = 0
                uncovered_vertices.remove(vertex)
        
        for vertex in self.Graph.neighbors(min_value_vertex):
            for neighbor in self.Graph.neighbors(vertex):
                if self.Graph.nodes().data()[neighbor]['uncov'] == 0 and self.Graph.nodes().data()[vertex]['val'] == 0:
                    if neighbor not in open_vertices:
                        open_vertices.append(neighbor)
                        self.Graph.nodes().data()[neighbor]['cov'] = 1
        
        self.Graph.nodes().data()[min_value_vertex]['val'] = 0
        self.Graph.nodes().data()[min_value_vertex]['cov'] = 1
        self.Graph.nodes().data()[min_value_vertex]['uncov'] = 1
        uncovered_vertices.append(min_value_vertex)
        return uncovered_vertices, open_vertices

    def cleanMaxIndSet(self, uncovered_vertices, open_vertices):
        while len(open_vertices) > 0:
            rand_vertex = random.choice(open_vertices)
            for vertex in self.Graph.neighbors(rand_vertex):
                self.Graph.nodes().data()[vertex]['val'] += 1
                if self.Graph.nodes().data()[vertex]['cov'] == 1 and self.Graph.nodes().data()[vertex]['uncov'] == 0:
                    self.Graph.nodes().data()[vertex]['cov'] = 0
                    open_vertices.remove(vertex)
            self.Graph.nodes().data()[rand_vertex]['uncov'] = 1
            self.Graph.nodes().data()[rand_vertex]['val'] = 0
            uncovered_vertices.append(rand_vertex)
            open_vertices.remove(rand_vertex)
        
        return uncovered_vertices, open_vertices
    
    def convertVC(self, VertexCover):
        for edge in self.Graph.edges():
            if edge[0] not in VertexCover and edge[1] not in VertexCover:
                VertexCover.append(edge[0])
        return VertexCover
            

class LocalSearch1:

    # Based on Heuristic from decisional version
    def __init__(self, filename, cutoff, random_seed):
        self.filename = filename
        self.graph = Graph(filename, random_seed)
        self.cutoff = cutoff
        self.random_seed = random_seed

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
        utils.writeOutput(self.filename, '_LS1_', self.cutoff, self.random_seed, finalVC, trace_out)

class LocalSearch2:

    # Based on Max indep set conversion
    def __init__(self, filename, cutoff, random_seed):
        self.filename = filename
        self.graph = Graph(filename, random_seed)
        self.cutoff = cutoff
        self.random_seed = random_seed
    

    def main(self):
        trace_out = []

        # Construct cover
        VC = self.graph.ConstructVC()
        num_nodes = self.graph.Graph.number_of_nodes()
        allVertIndices = list(self.graph.Graph.nodes)
        uncovered_vert_indices = list(set(allVertIndices) - set(VC))
        open_vertices = self.graph.maxIndSetInit(VC, uncovered_vert_indices)

        start_time = time.time()
        elapsetime = 0
        MaxIndSet = []

        while elapsetime < self.cutoff:
            if len(uncovered_vert_indices) >= len(MaxIndSet):
                if len(uncovered_vert_indices) > len(MaxIndSet):
                    trace_out.append([round(time.time() - start_time, 2), num_nodes - len(uncovered_vert_indices)])
                MaxIndSet = uncovered_vert_indices.copy()
                updated_graph = self.graph.Graph.copy()
                new_open_vertices = open_vertices.copy()
            else:
                uncovered_vert_indices = MaxIndSet.copy()
                self.graph.Graph = updated_graph.copy()
                open_vertices = new_open_vertices.copy()

            selected_vertices = list(set(allVertIndices) - set(uncovered_vert_indices))
            min_val_vertex = self.graph.minValVertex(selected_vertices)
            uncovered_vert_indices, open_vertices = self.graph.updateIndSet(uncovered_vert_indices, open_vertices, min_val_vertex)
            uncovered_vert_indices, open_vertices = self.graph.cleanMaxIndSet(uncovered_vert_indices, open_vertices)
            elapsetime = time.time() - start_time
        
        finalVC = self.graph.convertVC(list(set(allVertIndices) - set(MaxIndSet)))
        utils.writeOutput(self.filename, '_LS2_', self.cutoff, self.random_seed, finalVC, trace_out)