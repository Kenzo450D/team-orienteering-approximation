#!/usr/bin/env python3

'''
In this graph class, we should be able to update the prizes of the graph.

1. Make a function to initialize the graph
2. Make a function to update the prizes of the graph
'''

import numpy as np

class Graph:
    def __init__(self, n:int=10):
        # -- initialize a graph with n vertices
        self.data = {} 
        if n == 10:
            self.data = self.graph_n10()
        
    
    def update_graph_prizes(self, path, gamma:int = 0.1):
        if type(gamma) == float:
            # -- equally discount everyone in the path
            # ignore if path has start vertex
            start_idx = 1 if path[0] == self.data['home'] else 0
            end_idx = len(path) if path[-1] == self.data['goal'] else len(path)-1
            for idx in range(start_idx, end_idx):
                self.data['prizes'][path[idx]] = self.data['prizes'][path[idx]] * gamma
        if type(gamma) == list:
            for idx in len(path):
                v = path[idx]
                self.data['prizes'][v] = self.data['prizes'][v] * gamma[idx]
        
        return
            


    def graph_n10(self):
        data = {}
        #                          0  1  2  3  4  5  6  7  8  9
        data['costs'] = np.array([[0, 2, 2, 2, 4, 4, 4, 6, 6, 6],  # 0
                                  [2, 0, 4, 2, 2, 4, 4, 4, 6, 6],  # 1
                                  [2, 4, 0, 2, 4, 2, 4, 6, 4, 6],  # 2
                                  [2, 2, 2, 0, 2, 2, 2, 4, 4, 4],  # 3
                                  [4, 2, 4, 2, 0, 4, 2, 2, 4, 4],  # 4
                                  [4, 4, 2, 2, 4, 0, 2, 4, 2, 4],  # 5
                                  [4, 4, 4, 2, 2, 2, 0, 2, 2, 2],  # 6
                                  [6, 4, 6, 4, 2, 4, 2, 0, 4, 2],  # 7
                                  [6, 6, 4, 4, 4, 2, 2, 4, 0, 2],  # 8
                                  [6, 6, 6, 4, 4, 4, 2, 2, 2, 0]]) # 9
        # data['prizes'] = np.array([0, 50, 50, 50, 50, 50, 50, 50, 50, 0], dtype=np.float64)
        data['prizes'] = np.array([0, 50, 50, 50, 50, 50, 50, 50, 50, 0], dtype=np.int32)
        data['depot_idx'] = 0
        data['home'] = 0
        data['goal'] = 9
        return data
