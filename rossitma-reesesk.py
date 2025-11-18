## Mackenzie Rossiter and Sammi Reese

#How many Bitcoin nodes does the Bitcoin network in the data file have?

#!/usr/bin/python
import networkx as nx

#
# The following lines must appear at the beginning for graph drawing to work
# Do not touch them
import matplotlib
import pygeoip
matplotlib.use('Agg')
from collections import Counter

# The following line imports Matplotlib so that you can draw a graph
import pylab as plt

# The following is needed to take arguments from command line
import sys

GEOIP = pygeoip.GeoIP("/scratch/reesesk/GeoIP.dat", pygeoip.MEMORY_CACHE)

def load_and_display_file():
    graph1 = nx.read_graphml('full-bitcoin.graphml')
    return graph1.to_undirected()


country_cache = {}
def ip_to_country(ip):
    if ip in country_cache:
        return country_cache[ip]
    country = GEOIP.country_name_by_addr(ip)
    if country is None:
        country = "Unknown"
    country_cache[ip] = country
    return country


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

    degrees = dict(graph1.degree())
    #Question 5 Top 10 nodes by degree
    country_map = {n: ip_to_country(n) for n in all_nodes}

    top_10 = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Top 10 nodes by degree:")
    for ip, deg in top_10:
        print(f"IP: {ip}, Degree: {deg}, Country: {country_map[ip]}")


    #Question 6 top 5 countries by # of nodes
    countries = list(country_map.values())
    top_countries = Counter(countries).most_common(5)
    print("Top 5 countries by number of nodes:")
    for country, count in top_countries:
        print(f"{country}: {count}")

if __name__ == "__main__":
    main()
