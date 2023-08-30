#!/usr/bin/env python3


from get_graph import Graph
from single_robot_orienteering import RecursiveAlgorithm
from math import log2
from math import ceil

n_robots = 2   # set the number of robots
B = 30  # set the budget
s = 0   # start vertex
t = 9   # end vertex
n_vertices = 10

graph_env = Graph(10)

paths = []
k = 0

# -- print data
print ("Budget: ", B)
print ("Start vertex: ", s)
print ("End vertex: ", t)
print ("number of vertices: ", n_vertices)
print ("number of robots: ", n_robots)
print ("-"*100)

# -- calculate n_iter
n_iter = int(ceil(log2(n_vertices)))+1
print (n_iter)


# loop through all robots
for robot_idx in range(0, n_robots):
    ora = RecursiveAlgorithm(graph_env.data)
    robot_path = ora.recursive_greedy(s, t, B, set([s,t]),n_iter)
    print (f"Robot Path for robot {robot_idx}:: {robot_path}")
        # get_single_robot_orienteering(graph_env, B, s, t)
    paths.append(robot_path)
    # -- update graph env
    # print ("Before prize update prizes: ", graph_env.data['prizes'])
    graph_env.update_graph_prizes(robot_path)
    # print (f"After update prizes      :{graph_env.data['prizes']}")
    # -- increment number of paths assigned
    k += 1

# print the paths
# for robot_idx, path in enumerate(paths):
    # print (f"Robot: {robot_idx}\tPath: {path}")

print ("="*100)