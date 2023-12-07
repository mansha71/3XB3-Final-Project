import pandas as pd
from final_project_part1 import DirectedWeightedGraph
import math

def calculate_weigth(lat1, lon1, lat2, lon2):
    #print("Valeus")
    #print(lat1, long1, lat2, long2)
    #distance = sqrt((lat2 - lat1)**2 + (long2 - long1)**2)
    #print(distance)
    #return distance
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    radius_of_earth = 6371  # Earth radius in kilometers

    # Calculate the distance
    distance = radius_of_earth * c
    return distance

def read_data():
    g = DirectedWeightedGraph()
    df = pd.read_csv (r'./london_stations.csv')
    dict_stations = {}
    line ={}
    for row in df.itertuples(index=False):
        g.add_node(row.id)
        dict_stations[row.id] = [row.latitude,row.longitude]
    df_conn = pd.read_csv (r'./london_connections.csv')
    for row in df_conn.itertuples(index=False):
        lat1 = dict_stations[row.station1][0]
        long1 = dict_stations[row.station1][1]
        lat2 = dict_stations[row.station2][0]
        long2 = dict_stations[row.station2][1]
        line[row.station1] = row.line
        line[row.station2] = row.line
        w = calculate_weigth(lat1,long1,lat2,long2)
        g.add_edge(row.station1,row.station2,w)
        g.add_edge(row.station2,row.station1,w)

    return (g,dict_stations,line)
   


if __name__ == '__main__':
    read_data()