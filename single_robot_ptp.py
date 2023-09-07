import numpy as np
import sys

class RecursiveAlgorithm:
    def __init__(self, graph_data, multiplier=1):
        self.costs = graph_data['costs']
        self.prizes = graph_data['prizes']
        self.depot_idx = graph_data['depot_idx']
        self.num_nodes = len(self.costs)
        self.multiplier = multiplier
        print ("Prizes: ", self.prizes)

    def get_path_cost(self, path):
        ''' Calculates the sum of each edges in the path.
        Input:
            path: list of vertices in the path
        Output:
            cost <int>: cost of the edges in the path
        '''
        cost = 0
        for i in range(1, len(path)):
            cost += self.costs[(path[i-1],path[i])]
        return cost

    def get_path_prize(self, path):
        ''' Calculates the sum of prizes of all vertices in the path
        Input:
            path: list of vertices in the path
        Output:
            prize <int>: prizes of the vertices in the path
        '''
        prize = sum([self.prizes[i] for i in path])
        return prize

    def get_ptp_prize_cost_difference(self, path):
        ''' Calculates the difference between the sum of prizes and the sum of costs of all vertices in the path
        Input:
            path: list of vertices in the path
        Output:
            prize_cost_diff <int>: difference between the sum of prizes and the sum of costs of the vertices in the path
        '''
        prize = self.get_path_prize(path)
        cost = self.get_path_cost(path)
        prize_cost_diff = self.multiplier*prize - cost
        return prize_cost_diff

    def recursive_greedy(self, s: int, t: int, b: int, r_set: set, n_iter:int=0, prefix:str=""):
        ''' Calculates orienteering path from s to t within budget b.
        '''
        c = self.costs 
        if c[s,t] > b: # line 3
            return None, None # no path from s to t within budget b
        path = [s, t] # line 5
        if n_iter == 0:
            return path, self.get_ptp_prize_cost_difference(path)
        
        # -- get m
        m = self.get_ptp_prize_cost_difference(path)
        # print(f"{prefix}m: {m}")

        # -- iterate over all vertices
        v_set = set([i for i in range(0, self.num_nodes)])

        # -- remove the numbers in r_set
        v_set -= r_set

        # -- iterate over v_set
        for v_m in v_set: # line 8
            # try all budget split
            for b_val in range(2, b, 2): # line 9
                r_1 = r_set.union(set([v_m]))
                b_1 = b_val
                b_2 = b - b_val
                path_1, m_path_1 = self.recursive_greedy(s, v_m, b_1, r_1, n_iter-1, prefix+"\t") # line 10
                if path_1 is None:
                    continue
                r_2 = r_set.union(set(path_1))
                path_2, m_path_2 = self.recursive_greedy(v_m, t, b_2, r_2, n_iter-1, prefix+"\t") # line 11
                if path_2 is None:
                    continue
                path_new = path_1 + path_2[1:]
                m_new = self.get_ptp_prize_cost_difference(path_new)
                if m_new > m: # line 12
                    path = path_new
                    m = m_new
        return path, m