#!/usr/bin/env python3


from get_graph import Graph
from single_robot_ptp import RecursiveAlgorithm
# from single_robot_orienteering import RecursiveAlgorithm
from math import log2
from math import ceil
from copy import copy

n_robots = 3   # set the number of robots
B = 30  # set the budget
# s = 0   # start vertex
s = [i for i in range(0,n_robots)] # different start vertex
t = 9   # end vertex
n_vertices = 10
prize_multiplier = 10

graph_env = Graph(10)

paths = []
k = 0

# -- print data
print ("Budget: ", B)
print ("Start vertex: ", s)
print ("End vertex: ", t)
print ("number of vertices: ", n_vertices)
print ("number of robots: ", n_robots)
print ("Prize multiplier: ", prize_multiplier)
print ("-"*100)

# -- calculate n_iter
n_iter = int(ceil(log2(n_vertices)))-1#+1
n_iter = 4
print ("Number of iterations: ", n_iter)


# -- reduce prizes of all start vertices to zero
for si in s:
    graph_env.data['prizes'][si] = 0


# loop through all robots
# graph_env.data['prizes'] = [0, 0, 0, 5, 5, 5, 5, 5, 5, 0]
for robot_idx in range(0, n_robots):
    ora = RecursiveAlgorithm(graph_env.data, multiplier=prize_multiplier)
    print (f"Robot: {robot_idx} :: Budget: {B},\tStart: {s[robot_idx]},\tEnd:{t},\tn_iter:{n_iter}")
    robot_path, m = ora.recursive_greedy(s[robot_idx], t, B, set([s[robot_idx],t]),n_iter)
    print (f"\tRobot Path for robot {robot_idx}:: {robot_path}")
    print (f"\tLength of path: {len(robot_path)}")
    print (f"\tPath prize - cost: ", m)
    print ("\t"+"-"*50)
    paths.append(robot_path)
    # -- update graph env
    prev_prizes =  copy(graph_env.data['prizes'])
    print ("Before prize update prizes: ")#, graph_env.data['prizes'])
    for idx,pi in enumerate(graph_env.data['prizes']):
        print (f"\tVertex: {idx} :: {graph_env.data['prizes'][idx]}")
    print ("\t"+"-"*50)
    graph_env.update_graph_prizes(robot_path)
    print (f"After update prizes      :")
    for idx,pi in enumerate(graph_env.data['prizes']):
        print (f"\tVertex: {idx} :: {prev_prizes[idx]}\t{graph_env.data['prizes'][idx]}")
    print ("="*60)
    # print (f"After update prizes      :{graph_env.data['prizes']}")
    # -- increment number of paths assigned
    k += 1

# print the paths
# for robot_idx, path in enumerate(paths):
    # print (f"Robot: {robot_idx}\tPath: {path}")

print ("="*100)