import min_heap
import random
from final_project_part1 import *
import matplotlib.pyplot as plt
import time


def dijkstra_limit(G, source,thresold):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())
    relax_neighbors = {}

    #Initialize priority queue/heap and distances
    for node in nodes:
        relax_neighbors[node] = 0
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if relax_neighbors[neighbour] <= thresold and dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                relax_neighbors[neighbour] += 1
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return (dist,relax_neighbors)


def bellman_ford_limit(G, source,thresold):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())
    relax_neighbors = {}
    #Initialize distances
    for node in nodes:
        relax_neighbors[node] = 0
        dist[node] = float("inf")
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if relax_neighbors[neighbour] <= thresold and dist[neighbour] > dist[node] + G.w(node, neighbour):
                    relax_neighbors[neighbour] += 1
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return (dist,relax_neighbors)





def plot_runtimes_impl1(x, y1, y2):
    #drawing out the graph
    plt.plot(x, y1, label='dijkstras')
    plt.plot(x, y2, label='bell ford')
    plt.xlabel('Number of Items')
    plt.ylabel('Runtime (s)')
    plt.legend()
    plt.title('Ks Recursion vs Ks Brute Force')
    plt.show()

def calc_path(path,source):
    total = 0
    for i in path.keys():
        total += path[i]
    return total

def main():
    #expermint 1 a
    n = 40
    weight_upper = 50
    max_relax = 50
    g = create_random_complete_graph(n,weight_upper)
    source = list(g.adj.keys())[0]
    correct_path = dijkstra(g,source)
    total = calc_path(correct_path,source)
    x = []
    y =[]
    y1 =[]
    for i in range(1,max_relax):
        path_total = calc_path(dijkstra_limit(g,source,i)[0],source)
        diff = path_total/total
        y.append(diff)
        path_total = calc_path(bellman_ford_limit(g,source,i)[0],source)
        diff = path_total/total
        x.append(i)
        y1.append(diff)
    plot_runtimes_impl1(x,y,y1)


def main():
    #expermint 1 a
    weight_upper = 50
    max_relax = 50
    limit =1000000000000
    x = []
    y =[]
    y1 =[]
    for i in range(1,50):
        g = create_random_complete_graph(i,i)
        source = list(g.adj.keys())[0]
        relax1 = max(dijkstra_limit(g,source,limit)[1].values())
        print(relax1)
       
        y.append(relax1)
        relax2 =  max(bellman_ford_limit(g,source,limit)[1].values())
        print(relax2)
        x.append(i)
        y1.append(relax2)
    print(y1)
    print("ff")
    print(y)
    plt.plot(x, y, label='dijkstras')
    plt.plot(x, y1, label='bell ford')
    plt.xlabel('Number of nodes')
    plt.ylabel('Number of Relaxation')
    plt.legend()
    plt.title('Ks Recursion vs Ks Brute Force')
    plt.show()





def main2():
    #expermint 2 a
    n = 40
    weight_upper = 50
    max_relax = 50
    g = create_random_complete_graph(n,weight_upper)
    source = list(g.adj.keys())[0]
    correct_path = dijkstra(g,source)
    total = calc_path(correct_path,source)
    x = []
    y =[]
    y1 =[]
    for i in range(1,max_relax):
        path_total = calc_path(dijkstra_limit(g,source,i),source)
        diff = path_total/total
        y.append(diff)
        path_total = calc_path(bellman_ford_limit(g,source,i),source)
        diff = path_total/total
        x.append(i)
        y1.append(diff)
    plot_runtimes_impl1(x,y,y1)




def main3():
    #expermint 2 a
    n = 40
    weight_upper = 50
    max_nodes = 100
    max_relax = 50
    limit = 20
    g = create_random_complete_graph(n,weight_upper)
    source = list(g.adj.keys())[0]
    correct_path = dijkstra(g,source)
    total = calc_path(correct_path,source)
    x = []
    y =[]
    y1 =[]
    for i in range(1,max_nodes):

        g = create_random_complete_graph(i,i)
        source = list(g.adj.keys())[0]
        path_total = calc_path(dijkstra_limit(g,source,limit)[0],source)
        diff = path_total/total
        y.append(0)
        path_total = calc_path(bellman_ford_limit(g,source,limit)[0],source)
        diff = path_total/total
        x.append(i)
        y1.append(diff)
    plot_runtimes_impl1(x,y,y1)


def mystery_fuction_exp():
    max_nodes = 500
    x=[]
    y=[]
    for i in range(1,max_nodes):
        g = create_random_complete_graph(i,i)
        source = list(g.adj.keys())[0]
        start = time.time()
        mystery(g)
        diff = time.time() - start
       
        y.append(diff)
        x.append(i)
    plt.plot(x, y, label='mystery')
    plt.xlabel('Number of nodes')
    plt.ylabel('Time ')
    plt.legend()
    plt.title('Mystery Algorithm Performance')
    plt.show()




if __name__ == "__main__":
    mystery_fuction_exp()