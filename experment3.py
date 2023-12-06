from csv_to_graph import read_data
import time


def all_pair_test():
    g = read_data()
    nodes = list(g.adj.keys())

    for i in nodes:
        for j in nodes:
            if i != j :

    print("P")


if __name__ == '__main__':
    main()