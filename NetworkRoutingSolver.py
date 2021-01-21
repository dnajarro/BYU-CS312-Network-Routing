#!/usr/bin/python3


from CS312Graph import *
import time
import math
from arrayqueue import ArrayQueue
from heapqueue import HeapQueue


class NetworkRoutingSolver:
    def __init__(self):
        self.previous_nodes = {}  # holds prev nodes; dictionary from current node object to its previous node object
        self.distances = {}  # holds the final total distance to each node from the start node; dictionary of node_id
        # to distance
        self.queue = []  # holds the node_id's of all the nodes to be explored
        self.network = None
        self.dest = None
        self.source = None

    def initializeNetwork(self, network):
        assert (type(network) == CS312Graph)
        self.network = network

    # finds the shortest path from the source node to the destination node
    # takes the distance to the dest node, then iteratively goes backward from the dest node back to the source node
    # finding the difference of distance between two neighbor nodes to find the weight of an edge
    def getShortestPath(self, destIndex):
        self.dest = destIndex
        path_edges = []
        nodes = self.network.getNodes()
        total_length = self.distances[self.dest]
        current = nodes[self.dest]
        one_before = self.previous_nodes[nodes[self.dest]]
        while one_before is not None:
            dist2 = self.distances[current.node_id]
            dist1 = self.distances[one_before.node_id]
            weight = dist2 - dist1
            path_edges.append((current.loc, one_before.loc, '{:.0f}'.format(weight)))
            current = one_before
            one_before = self.previous_nodes[one_before]
        return {'cost': total_length, 'path': path_edges}

    # Dijkstra's algorithm: includes both array queue implementation and min heap implementation
    def computeShortestPaths(self, srcIndex, use_heap):
        self.source = srcIndex
        nodes = self.network.getNodes()
        self.distances = {}
        self.previous_nodes = {}
        for i in nodes:
            self.distances[i.node_id] = math.inf
            self.previous_nodes[i] = None
        self.distances[self.source] = 0

        t1 = time.time()
        if not use_heap:
            self.queue = ArrayQueue()
            self.queue.make_queue(list(self.distances.keys()))
            while self.queue.length > 0:
                node_id = self.queue.deletemin(self.distances)
                if node_id is not None:
                    for edge in nodes[node_id].neighbors:
                        # if current distance is greater than distance if we take another path
                        if self.distances[edge.dest.node_id] > (self.distances[node_id] + edge.length):
                            self.distances[edge.dest.node_id] = self.distances[node_id] + edge.length
                            self.previous_nodes[nodes[edge.dest.node_id]] = nodes[node_id]
                            self.queue.decreasekey()
        else:
            self.queue = HeapQueue()
            self.queue.make_queue(list(self.distances.keys()), self.distances)
            while self.queue.length > 0:
                node_id = self.queue.deletemin(self.distances)
                if node_id is not None:
                    for edge in nodes[node_id].neighbors:
                        if self.distances[edge.dest.node_id] > (self.distances[node_id] + edge.length):
                            self.distances[edge.dest.node_id] = self.distances[node_id] + edge.length
                            self.previous_nodes[nodes[edge.dest.node_id]] = nodes[node_id]
                            self.queue.decreasekey(edge.dest.node_id, self.distances)
        t2 = time.time()
        return t2 - t1
