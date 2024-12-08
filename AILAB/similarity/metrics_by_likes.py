from math import sqrt
from similarity.euclidean import euclidean_distance, euclidean_distance2 
from similarity.jaccard import jaccard_distance 

def LikeOne(AllData, Datar):
    # like one
    distances = list()

    for Trow in AllData:
        if Trow[0] == Datar[0]:
            continue

        dist = sqrt(euclidean_distance2([Datar[1]], [Trow[1]]) ** 2 + euclidean_distance(Datar[2:8], Trow[2:8]) ** 2)
        # dist = sqrt(euclidean_distance2(Datar[1:], Trow[1:]) ** 2)    

        distances.append((Trow[0], dist))

    distances.sort(key=lambda tup: tup[1])

    Simi = list()

    for i in range(0, 4):
        Simi.append(distances[i][0])

    ens = set(Simi)
    return Simi


def LikeList(AllData, DataRs):
    # like list data
    distances = list()

    for r1 in AllData:
        distances = list()

        for r1 in AllData:
            distances = list()

        for r1 in AllData:
            distance = sqrt(euclidean_distance(DataRs[0][1:2], r1[1:2]) ** 2 + jaccard_distance(DataRs[0][2:7], r1[2:7]) ** 2)
            # dist = sqrt(euclidean_distance([DataRs[1]], [r1[1]]) ** 2 + euclidean_distance(DataRs[2:7], r1[2:7]) ** 2)

            dataa = DataRs[0][0]

            for r2 in DataRs:
                if r2 == r1:
                    continue

                dist = sqrt(euclidean_distance(r2[1:2], r1[1:2]) ** 2 + jaccard_distance(r2[2:7], r1[2:7]) ** 2)
                # dist = sqrt(euclidean_distance([r2[1]], [r1[1]]) ** 2 + euclidean_distance(r2[2:7], r1[2:7]) ** 2)

                if dist < distance:
                    distance = dist
                    date = r2[0]

            distances.append((r1[0], distance))

    distances.sort(key=lambda tup: tup[1])

    Simi = list()

    for i in range(0, 8):
        Simi.append(distances[i][0])

    return Simi


def DisLikeList(AllData, Datars):
    # List of dislike data
    distances = list()

    for r2 in AllData:
        distance = sqrt(euclidean_distance([Datars[0][1]], [r2[1]]) ** 2 + jaccard_distance(Datars[0][2:8], r2[2:8]) ** 2)

        date = Datars[0][0]

        for r1 in Datars:
            if r1 == r2:
                continue

            dist = sqrt(euclidean_distance([r1[1]], [r2[1]]) ** 2 + jaccard_distance(r1[2:8], r2[2:8]) ** 2)

            if dist < distance:
                distance = dist
                date = r1[0]

        if r2 not in Datars:
            distances.append((r2[0], distance))

    # distances.sort(key=lambda tup: tup[1], reverse=True)
    distances.sort(key=lambda tup: tup[1])

    Simi = list()

    for i in range(8):
        Simi.append(distances[i][0])

    return set(Simi)
