import math
from similarity.euclidean import euclidean_distance, euclidean_distance2  # Import necessary functions

def cosine_similarity(v1, v2):
    x = v1
    y = v2
    sumxx, sumxy, sumyy = 0, 0, 0
    sumxx += x * x
    sumyy += y * y
    sumxy += x * y
    
    return sumxy / math.sqrt(sumxx * sumyy)

# itemsi = range(0, 49)
# itemsiv = range(1, 49)
def num_sim(n1, n2):
    """ calculates a similarity score between 2 numbers """
    return 1 - abs(n1 - n2) / (n1 + n2)

# Similarity Distance 
def similarity(AllData, Datar, m):
    distances = list()
    ii = 0

    for RowList in AllData:
        if RowList == Datar:
            continue

        if m == 'a':
            # distb = euclidean_distance(Datar[2:3], RowList[2:3])
            distb = euclidean_distance(Datar[2:8], RowList[2:8])
            # print("inside similarity euclidean distance")
            # print(distb)
            distb = int(distb)
            if distb >= 3.5 and distb <= 6:
                dist = distb
            else:
                continue

        elif m == 'p':
            # distb = jaccard_distance(Datar[1:], RowList[1:])
            distb = euclidean_distance2(Datar[1:], RowList[1:])
            # print("inside similarity jaccard distance")
            # print(distb)
            distb = int(distb)
            if distb >= 0 and distb <= 2:
                dist = distb
            else:
                continue

        distances.append((RowList[0], dist))
        ii += 1

    distances.sort(key=lambda tup: tup[1])

    Simi = list()
    LL = len(distances)
    # print(LL)

    for i in range(LL):
        Simi.append(distances[i][0])
        # Simi.append(dist[i][0])

    return Simi

def similarity2(AllData, Datar):
    distances = list()

    for RowList in AllData:
        if RowList[1] == Datar[1]:
            distances.append(RowList)

    distances.sort(key=lambda tup: tup[1])

    Simi = list()
    LL = len(distances)
    # print(LL)

    for i in range(LL):
        Simi.append(distances[i][0])

    return Simi
