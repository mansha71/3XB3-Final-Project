import min_heap
import random
import final_project_part1


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
            relax_neighbors[neighbour] += 1
            if relax_neighbors[neighbour] <= thresold and dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


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
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist





def plot_runtimes_impl1(x, y1, y2):
    #drawing out the graph
    plt.plot(x, y1, label='ks rec')
    plt.plot(x, y2, label='ks brute force')
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
    n = 30
    weight_upper = 50
    max_relax = 50
    g = create_random_complete_graph(n,weight_upper)
    source = list(G.adj.keys())[0]
    correct_path = dijkstra(g,source)
    total = calc_path(correct_path,source)
    x = []
    y =[]
    y1 =[]

    for i in range(10,max_relax):
        path_total = calc_path(dijkstra_limit(g,source,i),source)
        diff = path_total/total

        y.append(diff)
        path_total = calc_path(bellman_ford_limit(g,source,i),source)
        diff = path_total/total
        x.append(i)



if __name__ == "__main__":
    main()