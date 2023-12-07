from csv_to_graph import read_data,calculate_weigth
import time
from final_project_part1 import *
from aStar import a_star

import matplotlib.pyplot as plt

def create_h(dict_stations,destination):
    h={}
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


def check_if_adj_line_star(s,pred,line,dict_stations,j):
    curr_line = line[s]
    lines = set()
    x = []
    curr = j
    isExist = True
    changed_lines = False
    path = []
    current_node = j
    #print("t")
    while current_node in pred and current_node is not None:
       # print(line[curr], curr_line)
        if line[curr] != curr_line and changed_lines == False:
            curr_line = line[curr] 
            changed_lines = True
        elif line[curr] != curr_line and changed_lines == True:
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


def check_if_transfere_line_star(s,pred,line,dict_stations,j):
    curr_line = line[s]
    lines = set()

    x = []
    curr = j
    isExist = True
    changed_lines = False
    path = []
    current_node = j
    #print("t")
    while current_node in pred and current_node is not None:
       # print(line[curr], curr_line)
        lines.add(line[current_node])
        current_node = pred[current_node]


    if len(lines)>3:
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
    mark50 = len(nodes)//4

    for i in nodes[0:mark50]:
        
        temp = []
        for j in nodes[0:mark50]:
             if i != j:
                h = create_h(dict_stations,j)
                start = time.time()
                pred = a_star_t(g,i,j,h)
                diff = time.time() - start

                start1 = time.time()
                pred1 = dijkstra_early_stop(g,i,j)
                diff1 = time.time() - start1
                print(diff1,diff)
                if pred1 is not None:
                    for k in check_if_same_line_star(i,pred1,line,dict_stations,j):
                        results[k] = diff1
                
                if pred is not None:
                    for k in check_if_same_line_star(i,pred,line,dict_stations,j):
                        results1[k] = diff


        

    results1 = dict(sorted(results1.items()))  
    results = dict(sorted(results.items()))  

    plt.plot(results.keys(), results.values(), label='dijkstras')
    plt.plot(results1.keys(), results1.values(), label='a star')
     #plt.plot(x, y1, label='a star ')
    plt.xlabel('distance')
    plt.ylabel('time')
    plt.legend()
    plt.title(' Algorithm Performance')
    plt.show()

            

    print("P")



def adj_line_test():
    g,dict_stations,line = read_data()

    nodes = list(g.adj.keys())
    nodes.sort()
    

    x = []
    y = []
    y1 = []

    results = {}
    results1 = {}

    mark50 = len(nodes)//2
    for i in nodes[0:mark50]:
        
        temp = []
        for j in nodes[0:mark50]:
             if i != j:
                h = create_h(dict_stations,j)
                start = time.time()
                pred = a_star_t(g,i,j,h)
                diff = time.time() - start

                start1 = time.time()
                pred1 = dijkstra_early_stop(g,i,j)
                diff1 = time.time() - start1
                print(diff1,diff)
                if pred1 is not None:
                    for k in check_if_adj_line_star(i,pred1,line,dict_stations,j):
                        results[k] = diff1
                
                if pred is not None:
                    for k in check_if_adj_line_star(i,pred,line,dict_stations,j):
                        results1[k] = diff


        

    results1 = dict(sorted(results1.items()))  
    results = dict(sorted(results.items()))  

    plt.plot(results.keys(), results.values(), label='dijkstras')
    plt.plot(results1.keys(), results1.values(), label='a star')
     #plt.plot(x, y1, label='a star ')
    plt.xlabel('distance')
    plt.ylabel('time')
    plt.legend()
    plt.title(' adj line Algorithm Performance')
    plt.show()



def trasnfer_line_test():
    g,dict_stations,line = read_data()

    nodes = list(g.adj.keys())
    nodes.sort()
    

    x = []
    y = []
    y1 = []

    results = {}
    results1 = {}

    mark50 = len(nodes)//1
    for i in nodes[0:mark50]:
        
        temp = []
        for j in nodes[0:mark50]:
             if i != j:
                h = create_h(dict_stations,j)
                start = time.time()
                pred = a_star_t(g,i,j,h)
                diff = time.time() - start

                start1 = time.time()
                pred1 = dijkstra_early_stop(g,i,j)
                diff1 = time.time() - start1
                print(diff1,diff)
                if pred1 is not None:
                    for k in check_if_transfere_line_star(i,pred1,line,dict_stations,j):
                        results[k] = diff1
                
                if pred is not None:
                    for k in check_if_transfere_line_star(i,pred,line,dict_stations,j):
                        results1[k] = diff


        

    results1 = dict(sorted(results1.items()))  
    results = dict(sorted(results.items()))  

    plt.plot(results.keys(), results.values(), label='dijkstras')
    plt.plot(results1.keys(), results1.values(), label='a star')
     #plt.plot(x, y1, label='a star ')
    plt.xlabel('distance')
    plt.ylabel('time')
    plt.legend()
    plt.title(' trasnfer line Algorithm Performance')
    plt.show()

if __name__ == '__main__':
    same_line_test()