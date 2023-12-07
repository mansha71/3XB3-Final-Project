from csv_to_graph import read_data,calculate_weigth
import time
from final_project_part1 import *
from aStar import a_star

import matplotlib.pyplot as plt
def create_h(dict_stations,destination):
    h={}
    #print("dict")
    #print(dict_stations)
    lat2 = dict_stations[destination][0]
    long2 = dict_stations[destination][1]
    for row in dict_stations.keys():
        lat1 = dict_stations[row][0]
        long1 =  dict_stations[row][1]
        w = calculate_weigth(lat1,long1,lat2,long2)
        h[row] = w
    return h

def all_pair_test():
    g,dict_stations,line = read_data()
    nodes = list(g.adj.keys())
    nodes.sort()

    x = []
    y = []
    y1 = []

    for i in nodes:
        start = time.time()
        dijkstra(g,i)
        y.append(time.time()- start)
        x.append(i)
    

    for i in nodes:
        start = time.time()
        print(i)
        for j in nodes:
            if i != j:
                #print(j)
                h = create_h(dict_stations,j)
                a_star(g,i,j,h)
        y1.append((time.time()- start))
    plt.plot(x, y, label='dijkstras')
    plt.plot(x, y1, label='a star ')
    plt.xlabel('Number of nodes')
    plt.ylabel('Time ')
    plt.legend()
    plt.title('Mystery Algorithm Performance')
    plt.show()

def check_if_same_line(s,pred,line,dict_stations):
    curr_line = line[s]
    x = []
    for i in pred.keys():
        curr = i
        isExist = True
        path = []
        current_node = i
        print("t")
        while current_node in pred and current_node is not None:
            print(line[curr], curr_line)
            if line[curr] != curr_line:
                isExist = False
            current_node = pred[current_node]
        if isExist:
            print(i,s)
            lat2 = dict_stations[i][0]
            long2 = dict_stations[i][1]
        
            lat1 = dict_stations[s][0]
            long1 =  dict_stations[s][1]
            print(lat1,long1,lat2,long2)
            w = calculate_weigth(lat1,long1,lat2,long2)
            x.append(w)
        
    return x


def check_if_same_line_star(s,pred,line,dict_stations,j):
    curr_line = line[s]
    x = []
    curr = j
    isExist = True
    path = []
    current_node = j
    #print("t")
    while current_node in pred and current_node is not None:
       # print(line[curr], curr_line)
        if line[curr] != curr_line:
            isExist = False
        current_node = pred[current_node]


    if isExist:
        lat2 = dict_stations[j][0]
        long2 = dict_stations[j][1]
    
        lat1 = dict_stations[s][0]
        long1 =  dict_stations[s][1]
        w = calculate_weigth(lat1,long1,lat2,long2)
        x.append(w)
        
    return x

def same_line_test():
    g,dict_stations,line = read_data()
    nodes = list(g.adj.keys())
    nodes.sort()
    

    x = []
    y = []
    y1 = []

    results = {}
    results1 = {}
    for i in nodes:
        start = time.time()
        pred = dijkstra_pred(g,i)
        diff = time.time()- start
        temp1 = []
        temp = check_if_same_line(i,pred,line,dict_stations)
        #print("ecludiean")
        #print(temp)
        for i in temp:
            results[i] = diff

    results = dict(sorted(results.items()))    

    for i in nodes:
        start = time.time()
       # print(i)
        temp = []
        for j in nodes:
             if i != j:
                #print(j)
                h = create_h(dict_stations,j)
                pred,path = a_star(g,i,j,h)
                if pred is not None:
                    temp = temp + check_if_same_line_star(i,pred,line,dict_stations,j)
                
        diff = time.time() - start
        for i in temp:
            results1[i] = diff
    results1 = dict(sorted(results1.items()))    

    plt.plot(results.keys(), results.values(), label='dijkstras')
    #plt.plot(results1.keys(), results1.values(), label='astart')
     #plt.plot(x, y1, label='a star ')
    plt.xlabel('Ecludiean distance')
    plt.ylabel('Time')
    plt.legend()
    plt.title('Mystery Algorithm Performance')
    plt.show()

            

    print("P")


if __name__ == '__main__':
    same_line_test()