from math import sqrt
from data.dataset_handler import data

# from data.dataset_handler import processed_data, data, dataset_price, dataset_ff, dataset_full, dataset_country

# Euclidean Distance

# The Euclidean Distance between all rows in data:
#print('Евклидово расстояние между всеми строками данных:')

def euclidean_distance(r1, r2):
    Distance = 0.0
    for i in range(0, len(r1)):
        Distance += (r1[i] - r2[i]) ** 2
    return sqrt(Distance)

def euclidean_distance2(r1, r2):
    Distance = 0.0
    for i in range(0, len(r2)):
        Distance += ((r1[i] * r2[i]) / 100)
    return Distance

#a = [10]
#b = [30, 20, 10, 45]
#dddd = euclidean_distance2(a, b)
#Si = int(dddd * 100)
#print("New Euclidean Distance Test")
#print(dddd)

