# OOP_HW3
Guy Gur-Arieh

How to run:

In the command line, run python main.py "[FILE NAME]", and it will plot the graph (as long as the chosen file is a viable .json file).

In order to do the testings, just remove the comment from the line "# check()" and it will run all the testings (including the checks on the large graphs so it will take a while).


# Algorithms:

shortest_path - uses Dijkstra's Algorithm, which calculates the shortest path from the source vertex to all its nearest neighbors until it reaches the destinations, then calculates the path and returns it and the total distance.

centerPoint - calculates the maximum distance between each vertex to the other, and then returns the vertex with the minimum maximum.

TSP - creates all possible permutations on the given cities list, then calculates each path and returns the path with the shortest distance.

plot_graph - simply plots the graph using matplotlib.pyplot. If the vertices have no position, it inserts random locations.

# Comparison:

Python:

x =  1000

Save: 0.015622138977050781s

Load: 0.0s

Plotting: 0.9582583904266357s

x =  10000

Save: 0.031280517578125s

Load: 0.046827077865600586s

Plotting: 8.063527822494507s

x =  100000

Save: 0.45635390281677246s

Load: 0.08066201210021973s

Plotting: 79.8804624080658s

x =  1000000

Save: 3.636035442352295s

Load: 0.8806850910186768s

Plotting: 855.8578388690948s



Java:

x = 1000

Save: 0.125s

Load: 0.047s

Plotting: 0.7s

x = 10000

Save: 0.083s

Load: 0.094s

Plotting: 0.7s

x = 100000

Save: 0.39s

Load: 0.375s

Plotting: 1.1s

x = 1000000

Save: 4.114s

Load: 3.116s

Plotting: 9s

# Conclusion:

python is faster than java in most cases, but matplotlib is way, way slower than java frame.
