from pandas_ods_reader import read_ods
import pandas as pd
import math
from math import *
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import os
import numpy as np



#/////////////////////////////////////////////////////////////////
# Get the data set

base_path = "/home/sohiab/IntelligentLab1/AILab1DataSet.ods"
sheet_index = 1

data = read_ods(base_path, 1, columns=["No.","Имя", "Цена($)/Кг","Страна","Регион","Размер","Цвет","Сладость","жесткость/влажность"])

DataFrame = pd.DataFrame(data,columns=["No.","Имя", "Цена($)/Кг","Страна","Регион","Размер","Цвет","Сладость","жесткость/влажность"])

UpdateD = DataFrame

#///////////////////////////////////////////////////////////////////////////////
#///////Get Similarity between all sets - jaccard_similarity///////////////////
print("///////////////////////////////////////////////////////////////////")
print('Получить сходство между всеми наборами - жаккардовое сходство:')
print("///////////////////////////////////////////////////////////////////\n")

AnB = 0;
AUB = 16;
itemsi = range(0,49);
itemsiv = range(1,49);
itemsj = [1,2,3,4,5,6,7,8];

similarity = []
similarityDis = []
for i in range(0,4):
    for iv in range(1,5):
        AnB = 0;
        for j in itemsj:
            if (data.iloc[i,j] == data.iloc[iv,j]) is not True:
                AnB +=1
            if j == 8:    
            #jaccard_similarity:
                similarity.append(AnB/AUB)
                Simi = AnB/AUB 
                #similarityDis.append((AUB-AnB)/AUB)
                if Simi >= 0.2 and Simi <= 1:
                    Si = int(Simi*100)
                    print(f'item#:{i} and item#:{iv} There Similarity is {Si}%')
            
         
#print(similarity)  
#print(" ")
#print(similarityDis) 
#print(data)

#////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
#Make all letter lower case
UpdateD['Имя'] = UpdateD['Имя'].str.lower()

UpdateD['Страна'] = UpdateD['Страна'].str.lower()

UpdateD['Регион'] = UpdateD['Регион'].str.lower()

UpdateD['Размер'] = UpdateD['Размер'].str.lower()
#Make some object to number
labelencoder=LabelEncoder()

UpdateD['Страна']=labelencoder.fit_transform(UpdateD['Страна'])
UpdateD['Регион']=labelencoder.fit_transform(UpdateD['Регион'])
UpdateD['Размер']=labelencoder.fit_transform(UpdateD['Размер'])
UpdateD['Цвет']=labelencoder.fit_transform(UpdateD['Цвет'])
UpdateD['Сладость']=labelencoder.fit_transform(UpdateD['Сладость'])
UpdateD['жесткость/влажность']=labelencoder.fit_transform(UpdateD['жесткость/влажность'])

#матрица корреляции 1:

corr_matrix = UpdateD.corr()
sn.heatmap(corr_matrix, annot=True)
plt.show()


#///////////////////Euclidean Distance///////////////////////////////////////
print("///////////////////////////////////////////////////////////////////")
#The Euclidean Distance between all rows in data:
print('Евклидово расстояние между всеми строками данных:')
print("///////////////////////////////////////////////////////////////////\n")

def euclidean_distance(r1, r2):
	Distance = 0.0
	for i in range(0,len(r1)):
		Distance += (r1[i] - r2[i])**2
	return sqrt(Distance)

itemsi = range(0,49);
itemsiv = range(1,49);

for i in range(0,4):
    for iv in range(1,5):
        row1=UpdateD.iloc[i][2:8].to_list()
        row2=UpdateD.iloc[iv][2:8].to_list()
    #print(row1)
    #print(row2)
    eu = euclidean_distance(row1,row2)
    print(f'The Euclidean Distance between: row#:{i} and row#:{iv} is {eu}')

#///////////////////Distance Between Two Object///////////////////////////////////////
print("///////////////////////////////////////////////////////////////////")
#The Euclidean Distance between Two object:
print('Евклидово расстояние между двумя объектами:')
print("///////////////////////////////////////////////////////////////////\n")

for i in range(0,4):
    for iv in range(1,5):
        v1=UpdateD.iloc[i,8]
        v2=UpdateD.iloc[iv,8]
        Vdiff = abs(v2-v1)
        if Vdiff == 0:
             print(f'жесткость/влажность объект#:{i} и объект#:{iv} похожий')
        elif Vdiff == 1:
             print(f'жесткость/влажность объект#:{i} и объект#:{iv} так близко')
        else:
             print(f'жесткость/влажность объект#:{i} и объект#:{iv} не похоже')


#///////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////
# Get Similarity Distance between two row - Jaccard
print("///////////////////////////////////////////////////////////////////")
print('Получить расстояние сходства между двумя строками - Жаккард:')
print("///////////////////////////////////////////////////////////////////\n")

def jaccard_distance(x,y):

    x1=set(x)
    x2=set(y)
            
    simalarity=float(len(x1.intersection(x2))/len(x1.union(x2)))
    result = 1-simalarity

    return result;


for i in range(0,4):
    for iv in range(1,5):
            x = data.iloc[i][2:8].to_list()
            y = data.iloc[iv][2:8].to_list()
            jacS = jaccard_distance(x,y)
            print(f'Jaccard - дистанционное сходство {i} и {iv} является {jacS}')
          
#/////////////////////////////////////////////////////////////////////////////////////
#///////////////////Cosine Similarity between Prices Object///////////////////////////////////////
print("///////////////////////////////////////////////////////////////////")
print('Косинусное сходство между ценовыми объектами:')
print("///////////////////////////////////////////////////////////////////\n")

def cosine_similarity(v1,v2):
            
       x = v1
       y = v2
       sumxx, sumxy, sumyy = 0, 0, 0
       sumxx += x*x
       sumyy += y*y
       sumxy += x*y
       
       return sumxy/math.sqrt(sumxx*sumyy)

#itemsi = range(0,49);
#itemsiv = range(1,49);

for i in range(0,4):
    for iv in range(1,5):
        v1 = UpdateD.iloc[i,2]
        v2 = UpdateD.iloc[iv,2]
        CosineS = cosine_similarity(v1,v2)
        #print(f'Cosine - Сходство между {i} и {iv} является {CosineS}')

#//////////////////////////////////////////////////////////////////////////////////


#/////////////////////////////////////////////////////////////////////////
#///////////////Recomindation System//////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////
import nltk
nltk.download('punkt')

print("///////////////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////////////")
print('                      Добро пожаловать                             ')
print('                           Финики                                  ')
print('                  Рекомендательная система                         ')
print("///////////////////////////////////////////////////////////////////\n")
print("не могли бы вы сказать мне, пожалуйста, как вам нравятся финики ?")
print("и что вам не нравится на финики ? \n")

LikeList = []
DisLikeList = []

#вопрос/////////////

Questioni = input('Вы хотите финики из конкретной страны или из любого места ? (Да или нет)\n')
Questionii = Questioni.lower()
Optioni = ["да", "согласие", "yes"] 
Optionii = ["нет", "не", "No"]
flag = 0 
for i in range(0,3):
        if Optioni[i] in Questionii:
            flag = 1    
        elif Optionii[i] in Questionii:
            flag = 2

if flag == 1:

#вопрос/////////////
    Question4 = input('Вам нравится, что это из Саудовской Аравии?\n')

    Question44 = Question4.lower()

    Option1 = ["да", "согласие", "саудовск"] 
    Option2 = ["нет", "не", "No"]

    for i in range(0,3):
        if Option1[i] in Question44:
            LikeList.append("Саудовской Аравии")
        elif Option2[i] in Question44:
            DisLikeList.append("Саудовской Аравии")
#вопрос/////////////
    Question5 = input('Вам нравится, что это из Иран?\n')

    Question55 = Question5.lower()

    Option11 = ["да", "согласие", "Иран"] 
    Option22 = ["нет", "не", "No"]

    for i in range(0,3):
        if Option11[i] in Question55:
            LikeList.append("Иран")
        elif Option22[i] in Question55:
            DisLikeList.append("Иран")
#вопрос/////////////
    Question6 = input('Вам нравится, что это из Эмирейтс?\n')

    Question66 = Question6.lower()

    Option111 = ["да", "согласие", "Эмирейтс"] 
    Option222 = ["нет", "не", "No"]

    for i in range(0,3):
        if Option111[i] in Question66:
            LikeList.append("Эмирейтс")
        elif Option222[i] in Question66:
            DisLikeList.append("Эмирейтс")

#Первый вопрос/////////////
Test = 0
while Test == 0:

    Question1 = input('Какие финики самое мягкий или полусухой или сухой? \n')

    Question11 = Question1.lower()
    #ListAnswer = nltk.word_tokenize(Question11)
    ListAnswer = Question11
   

    #hardnessList1 = ["мягкий", "легкий", "слабый","мяг", "лег", "сла"] #слова-синонимы
    hardnessList1 = ["мяг", "легк", "слаб"] #слова-синонимы
    hardnessList2 = ["полусух", "полусух", "полусух"]
    hardnessList3 = ["сухой", "суши", "сдержан"]

    for i in range(0,3):
        if hardnessList1[i] in ListAnswer:
            LikeList.append("мягкий")
            Test = 1
        if hardnessList2[i] in ListAnswer:
            LikeList.append("полусухой")
            Test = 1
        if hardnessList3[i] in ListAnswer:
            LikeList.append("сухой")
            Test = 1
       
    if Test == 1:
        break
    print("Не могли бы вы подробнее объяснить!!")


#второй вопрос/////////////
Test = 0
while Test == 0:

    Question2 = input('Какие финики самое сладкий ? \n')
    Question22 = Question2.lower()
   
    sweetness11 = ["слишк", "очен", "чересчур", "приторно"] #слова-синонимы
    sweetness12 = ["сладк", "сладк", "сладк", ""]
    sweetness22 = ["сладкий", "сладк", "конфе", "конф"]
    sweetness33 = ["сироп", "сиро", "сиропы", "сир"]
    sweetness44 = ["прайминги", "прайминг", "грунтовки", "грунтов"]
    sweetness55 = ["медовый", "мед", "мёд", "медо"]
    sweetness66 = ["кислый", "кисл", "прокисший", "прокисш"]


    for i in range(0,4):
        if sweetness11[i] in Question22 and sweetness11[i] in Question22:
            LikeList.append("слишком сладкий")
            Test = 1
        if sweetness22[i] in Question22:
            LikeList.append("сладкий")
            Test = 1
        if sweetness33[i] in Question22:
            LikeList.append("сироп")
            Test = 1
        if sweetness44[i] in Question22:
            LikeList.append("прайминги")
            Test = 1
        if sweetness55[i] in Question22:
            LikeList.append("медовый")
            Test = 1
            LikeList.append("кислый")
        if sweetness66[i] in Question22:
            Test = 1
       
    if Test == 1:
        break
    print("Не могли бы вы подробнее объяснить!!")

#Третий вопрос/////////////
Test = 0
while Test == 0:

    Question3 = int(input('Какой ценовой диапазон предпочитаете? Пожалуйста, выберите из списка ниже: \n 1- от 5$ до 20$\n 2- от 20$ до 30$\n 3- от 30$ до 45$\n'))


    if Question3 == 1:
        LikeList.append("недорогой")
        Test = 1
    elif Question3 == 2:
        LikeList.append("средний") 
        Test = 1
    elif Question3 == 3:
        LikeList.append("дорогой")
        Test = 1

    if Test == 1:
        break 

    print("пожалуйста, введите правильный ввод!!")

#Четвертый вопрос/////////////

Question4 = input('Вам нравится, чтобы он был большим или средним?\n')
'''
Test = 0
while Test == 0:

    if Question3 == 1:
        LikeList.append("недорогой")
        Test = 1
    elif Question3 == 2:
        LikeList.append("средний") 
        Test = 1
    elif Question3 == 2:
        LikeList.append("дорогой")
        Test = 1

    if Test == 1:
        break 

    print("пожалуйста, введите правильный ввод!!")
'''
print(LikeList)
print(DisLikeList)
 









'''
for i in range(0,2):
    for j in range(0,4):
        if LikeList[4] == data.iloc[0,8]:
           print(i)
           print("good")
'''








#///////////////////////////////////////////////////////////////////////////////////////////////////////


'''

dataset1=[[UpdateD['Имя'][i],UpdateD['Цена($)/Кг'][i],UpdateD['Страна'][i],UpdateD['Регион'][i]] for i in range(0,25)]

dataset2=[[UpdateD['Имя'][i],UpdateD['Размер'][i],UpdateD['Цвет'][i]] for i in range(0,25)]

dataset3=[[UpdateD['Имя'][i],UpdateD['Сладость'][i], UpdateD['жесткость/влажность'][i]] for i in range(0,25)]

dataset=[[UpdateD['Имя'][i],UpdateD['Цена($)/Кг'][i],UpdateD['Страна'][i],UpdateD['Регион'][i],UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i], UpdateD['жесткость/влажность'][i]] for i in range(0,25)]

'''


'''
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def cosine_distanceSS(row1,row2):

    X_list = word_tokenize(row1)

    Y_list = word_tokenize(row2)

    sw = stopwords.words('russian')

    X_set = {w for w in X_list if not w in sw}

    Y_set = {w for w in Y_list if not w in sw}

    l1 =[];l2 =[]

    rvector = X_set.union(Y_set)

    for w in rvector:

        if w in X_set:

            l1.append(1)

        else:

            l1.append(0)

        if w in Y_set:

            l2.append(1)

        else:

            l2.append(0)

    c=0

    for i in range(len(rvector)):

        c+=l1[i]*l2[i]

    cosine_sim=c/float((sum(l1)*sum(l2))**0.5)

    return 1-cosine_sim


for i in range(0,4):
    for iv in range(1,5):
            x11 = data.iloc[i][2:8].to_list()
            y11 = data.iloc[iv][2:8].to_list()
            CosJJ = cosine_distanceSS(x11,y11)
            print(f'New Cosine - дистанционное сходство {i} и {iv} является {CosJJ}')





# New Function


def get_neighbors(train,test_row,num_neighbors,measure):

    distances=list()

    for train_row in train:

        if train_row==test_row:

            continue

        if measure=='e':

            dist=euclidean_distance(test_row[1:],train_row[1:])

        elif measure=='j':

            dist=jaccard_distance(test_row[1:],train_row[1:])

        else:

            dist=cosine_distance(test_row[1],train_row[1])

        distances.append((train_row[0],dist))

    distances.sort(key=lambda tup: tup[1])

    neighbors=list()

    for i in range(num_neighbors):

        neighbors.append(distances[i][0])

    return neighbors

'''