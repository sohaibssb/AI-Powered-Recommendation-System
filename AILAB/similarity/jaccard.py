# similarity/jaccard.py

from data.dataset_handler import data 

# Get Similarity Distance between two rows - Jaccard

#print('Получить расстояние сходства между двумя строками - Жаккард:')

def jaccard_distance(x, y):
    x1 = set(x)
    x2 = set(y)

    similarity = float(len(x1.intersection(x2)) / len(x1.union(x2)))
    result = 1 - similarity
    #print("new test")
    #print(x1)
    #print(x2)
    #print(simalarity)
    #print(result)

    return result;

for i in range(0, 4):
    for iv in range(1, 5):
        x = data.iloc[i][2:3].to_list()
        y = data.iloc[iv][2:3].to_list()
        #print("x y")
        #print(x)
        #print(y)
        jacS = jaccard_distance(x, y)
        if jacS >= 0.1 and jacS <= 1:
            Si = int(jacS * 100)
            #print(f'item#:{i} and item#:{iv} There Similarity is {Si}%')
            #print(f'Jaccard - дистанционное сходство {i} и {iv} является {Si} %')

