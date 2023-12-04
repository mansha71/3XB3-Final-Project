import pandas as pd
from final_project_part1 import DirectedWeightedGraph
from math import sqrt

def calculate_weigth(lat1, long1, lat2, long2):
    distance = sqrt((lat2 - lat1)**2 + (long2 - long1)**2)
    return distance

def read_data():
    g = DirectedWeightedGraph()
    df = pd.read_csv (r'./london_stations.csv')
    dict_stations = {}
    for row in df.itertuples(index=False):
        g.add_node(row.id)
        dict_stations[row.id] = [row.latitude,row.longitude]
    df_conn = pd.read_csv (r'./london_connections.csv')
    for row in df_conn.itertuples(index=False):
        lat1 = dict_stations[row.station1][0]
        long1 = dict_stations[row.station1][1]
        lat2 = dict_stations[row.station2][0]
        long2 = dict_stations[row.station2][1]
        w = calculate_weigth(lat1,long1,lat2,long2)
        g.add_edge(row.station1,row.station2,w)
    return g
   


if __name__ == '__main__':
    read_data()