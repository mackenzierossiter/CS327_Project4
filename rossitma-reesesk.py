## Mackenzie Rossiter and Sammi Reese

#How many Bitcoin nodes does the Bitcoin network in the data file have?

#!/usr/bin/python
import networkx as nx

#
# The following lines must appear at the beginning for graph drawing to work
# Do not touch them
import matplotlib
matplotlib.use('Agg')

# The following line imports Matplotlib so that you can draw a graph
import pylab as plt

# The following is needed to take arguments from command line
import sys

def load_and_display_file():
    graph1 = nx.read_graphml('small-bitcoingraph.graphml')
    return graph1 
    

def main():
    graph1 = load_and_display_file()
    
    # question 1 total nodes
    all_nodes = graph1.nodes()
    print("How many bitcoin nodes does the bitcoin network in the data file have?")
    print(len(all_nodes))


    # question 2 total edges
    all_edges = graph1.edges()
    print("How many bitcoin edges does the bitcoin network in the data file have?")
    print(len(all_edges))

    #Question 3 highest degree node
    max_degree = 0
    for node in all_nodes:
        if graph1.degree(node) > max_degree:
            max_degree = graph1.degree(node)
    
    nodes_largest_degree = []
    for node in graph1.nodes():
        if graph1.degree(node) == max_degree:
            nodes_largest_degree.append(node)
    print("Which node(s) has the highest degree, and what is that degree?")
    print("The following nodes have the highest degree: " + str(nodes_largest_degree) + " with a degree of " + str(max_degree))


    #Question 4 Smallest node degree
    all_nodes = list(graph1.nodes())
    min_degree = graph1.degree(all_nodes[0])
    for node in all_nodes:
        if graph1.degree(node) < min_degree:
            min_degree = graph1.degree(node)
    
    nodes_smallest_degree = []
    for node in graph1.nodes():
        if graph1.degree(node) == min_degree:
            nodes_smallest_degree.append(node)

    print("Which node(s) has the smallest degree, and what is that degree?")
    print("The following nodes have the smallest degree: " + str(nodes_smallest_degree) + " with a degree of " + str(min_degree))





if __name__ == "__main__":
    main()