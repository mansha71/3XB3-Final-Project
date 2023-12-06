from final_project_part1 import *
import random
import min_heap

import heapq

def a_star(G, s, d, h):
    # Initialize the open set with the start node
    open_set = []
    heapq.heappush(open_set, (0, s))

    # Predecessors and costs to reach the nodes
    predecessors = {s: None}
    g_score = {node: float('inf') for node in G.adj}
    g_score[s] = 0

    # The f_score combines the g_score with the heuristic.
    f_score = {node: float('inf') for node in G.adj}
    f_score[s] = h[s]

    while open_set:
        # Pop the node with the lowest f_score
        _, current = heapq.heappop(open_set)

        # Check if the destination is reached
        if current == d:
            path = []
            while current is not None:
                path.insert(0, current)
                current = predecessors[current]
            return predecessors, path

        for neighbor in G.adjacent_nodes(current):
            # Tentative g_score for this neighbor
            tentative_g_score = g_score[current] + G.w(current, neighbor)

            # Check if this path to neighbor is better
            if tentative_g_score < g_score[neighbor]:
                predecessors[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h[neighbor]

                # Add or update the neighbor in the open set
                if neighbor not in [item[1] for item in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    # Return None if no path is found
    return None, []

def test_a_star(num_nodes, weight_limit):
    G = create_random_complete_graph(num_nodes, weight_limit)
    heuristic = {node: 1 for node in G.adj}

    # Randomly choose start and destination nodes
    start = random.randint(0, num_nodes - 1)
    destination = random.randint(0, num_nodes - 1)
    while destination == start:
        destination = random.randint(0, num_nodes - 1)

    pred, path = a_star(G, start, destination, heuristic)
    print(f"Path from {start} to {destination} in graph with {num_nodes} nodes: {path}")

# Test cases
print("Small Graph Test")
test_a_star(5, 10)

print("\nMedium Graph Test")
test_a_star(10, 20)

print("\nLarge Graph Test")
test_a_star(20, 30)

print("\nDense Graph Test")
test_a_star(15, 5)

print("\nSparse Graph Test")
test_a_star(10, 50)