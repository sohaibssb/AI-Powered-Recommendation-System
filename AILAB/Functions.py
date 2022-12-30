from pandas_ods_reader import read_ods
import pandas as pd
import math
from math import *
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import os
import numpy as np
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
from pprint import pprint


#“не найдено точного соответствия, однако, возможно, Вам понравится”

#/////////////////////////////////////////////////////////////////
# Get the data set

base_path = "/home/sohiab/IntelligentLab1/AILab1DataSet.ods"
sheet_index = 1

data = read_ods(base_path, 1, columns=["No.","Имя", "Цена","Страна","Регион","Размер","Цвет","Сладость","жесткость"])

DataFrame = pd.DataFrame(data,columns=["No.","Имя", "Цена","Страна","Регион","Размер","Цвет","Сладость","жесткость"])

UpdateD = DataFrame

#///////////////////////////////////////////////////////////////////////////////
#///////Get Similarity between all sets - jaccard_similarity///////////////////
print("///////////////////////////////////////////////////////////////////")
#print('Получить сходство между всеми наборами - жаккардовое сходство:')
print("///////////////////////////////////////////////////////////////////\n")

AnB = 0;
AUB = 16;
itemsi = range(0,49);
itemsiv = range(1,49);
itemsj = [1,2,3,4,5,6,7,8];

similarity = []
similarityDis = []
for i in range(0,49):
                    for iv in range(1,49):
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
                                    #print(f'item#:{i} and item#:{iv} There Similarity is {Si}%')
                            
            
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
UpdateD['жесткость']=labelencoder.fit_transform(UpdateD['жесткость'])

#матрица корреляции 1:

corr_matrix = UpdateD.corr()
sn.heatmap(corr_matrix, annot=True)
plt.show()


#///////////////////Euclidean Distance///////////////////////////////////////
print("///////////////////////////////////////////////////////////////////")
#The Euclidean Distance between all rows in data:
#print('Евклидово расстояние между всеми строками данных:')
print("///////////////////////////////////////////////////////////////////\n")

def euclidean_distance(r1, r2):

	Distance = 0.0
    

	for i in range(0,len(r1)):
		Distance += (r1[i] - r2[i])**2
	return sqrt(Distance)


def euclidean_distance2(r1, r2):

	Distance = 0.0
    
	for i in range(0,len(r2)):
		Distance += ((r1[i] * r2[i])/100)
	return Distance

#a = [10]
#b = [30,20,10,45]
#dddd = euclidean_distance2(a,b)
#Si = int(dddd*100)
#print("New Euclidean Distance Test")
#print(dddd)

'''
for i in range(0,4):
    for iv in range(1,5):
        #v1 = UpdateD.iloc[i,2]
        #v2 = UpdateD.iloc[iv,2]
        v1 = data.iloc[i][2:3].to_list()
        v2 = data.iloc[iv][2:3].to_list()
        print("v1")
        print(v1)
        print(v2)
        CosineS = euclidean_distance(v1,v2)
        print(f'eeeeeeeeeeeee - Сходство между {i} и {iv} является {CosineS}')
'''
#/////////////////////////////////////////////////////////////////////////////

'''
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
'''
#///////////////////Distance Between Two Object///////////////////////////////////////
print("///////////////////////////////////////////////////////////////////")
#The Euclidean Distance between Two object:
#print('Евклидово расстояние между двумя объектами:')
print("///////////////////////////////////////////////////////////////////\n")
'''
for i in range(0,4):
    for iv in range(1,5):
        v1=UpdateD.iloc[i,8]
        v2=UpdateD.iloc[iv,8]
        Vdiff = abs(v2-v1)
        if Vdiff == 0:
             #print(f'жесткость объект#:{i} и объект#:{iv} похожий')
        elif Vdiff == 1:
             #print(f'жесткость объект#:{i} и объект#:{iv} так близко')
        else:
             #print(f'жесткость объект#:{i} и объект#:{iv} не похоже')

'''
#///////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////
# Get Similarity Distance between two row - Jaccard
print("///////////////////////////////////////////////////////////////////")
#print('Получить расстояние сходства между двумя строками - Жаккард:')
print("///////////////////////////////////////////////////////////////////\n")


def jaccard_distance(x,y):

    x1=set(x)
    x2=set(y)
            
    simalarity=float(len(x1.intersection(x2))/len(x1.union(x2)))
    result = 1-simalarity
    #print("new test")
    #print(x1)
    #print(x2)
    #print(simalarity)
    #print(result)

    return result;


for i in range(0,4):
    for iv in range(1,5):
            x = data.iloc[i][2:3].to_list()
            y = data.iloc[iv][2:3].to_list()
            #print("x y")
            #print(x)
            #print(y)
            jacS = jaccard_distance(x,y)
            if jacS >= 0.1 and jacS <= 1:
                 Si = int(jacS*100)
                    #print(f'item#:{i} and item#:{iv} There Similarity is {Si}%')
                 #print(f'Jaccard - дистанционное сходство {i} и {iv} является {Si} %')
          
#/////////////////////////////////////////////////////////////////////////////////////
#///////////////////Cosine Similarity between Prices Object///////////////////////////////////////
print("///////////////////////////////////////////////////////////////////")
#print('Косинусное сходство между ценовыми объектами:')
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
def num_sim(n1, n2):
  """ calculates a similarity score between 2 numbers """
  return 1 - abs(n1 - n2) / (n1 + n2)



#//////////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////////////////
#///////////////Similarity Distance ///////////////////////////////////

def similarity(AllData,Datar,m):

    distances=list()
    ii = 0;
   
    for RowList in AllData:

        if RowList==Datar:

            continue

        if m=='a':

            #distb=euclidean_distance(Datar[2:3],RowList[2:3])
            distb=euclidean_distance(Datar[2:8],RowList[2:8])
            #print("inside similarity euclidean distance")
            #print(distb)
            distb = int(distb)
            if distb >= 3.5 and distb <= 6:
                dist = distb
            else:
                continue

        elif m=='p':

            #distb=jaccard_distance(Datar[1:],RowList[1:])
            distb=euclidean_distance2(Datar[1:],RowList[1:])
            #print("inside similarity jaccard distance")
            #print(distb)
            distb = int(distb)
            if distb >= 0 and distb <= 2:
                dist = distb
            else:
                continue
  
        distances.append((RowList[0],dist))
        ii+=1;
        
#ssss

    distances.sort(key=lambda tup: tup[1])

    Simi=list()
    LL = len(distances)
    #print(LL)

    for i in range(LL):

        Simi.append(distances[i][0])
        #Simi.append(dist[i][0])

    return Simi

#////////////////////////////////////////////////////////////

def similarity2(AllData,Datar):

    distances=list()
   
    for RowList in AllData:
        
        if RowList[1]==Datar[1]:

            distances.append(RowList)
        

    distances.sort(key=lambda tup: tup[1])

    Simi=list()
    LL = len(distances)
    #print(LL)

    for i in range(LL):

        Simi.append(distances[i][0])
    

    return Simi

#///////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////

def LikeOne(AllData,Datar):
#like one
    distances=list()
   
    for Trow in AllData:

        if Trow[0]==Datar[0]:

            continue

        dist=sqrt(euclidean_distance2([Datar[1]],[Trow[1]])**2+euclidean_distance(Datar[2:8],Trow[2:8])**2)
        #dist=sqrt(euclidean_distance2(Datar[1:],Trow[1:])**2)
        
       

        distances.append((Trow[0],dist))

    distances.sort(key=lambda tup: tup[1])

    Simi=list()

    for i in range(0,4):

        Simi.append(distances[i][0])

    ens=set(Simi)
    return Simi



#///////////////////////////////////////////////////////////

def LikeList(AllData,DataRs):
#like list data

    distances=list()

    for r1 in AllData:

         distances=list()

    for r1 in AllData:

         distances=list()

    for r1 in AllData:

        distance=sqrt(euclidean_distance(DataRs[0][1:2],r1[1:2])**2+jaccard_distance(DataRs[0][2:7],r1[2:7])**2)
        #dist=sqrt(euclidean_distance([DataRs[1]],[r1[1]])**2+euclidean_distance(DataRs[2:7],r1[2:7])**2)

        dataa=DataRs[0][0]

        for r2 in DataRs:

            if r2==r1:

                continue

            dist=sqrt(euclidean_distance(r2[1:2],r1[1:2])**2+jaccard_distance(r2[2:7],r1[2:7])**2)
            #dist=sqrt(euclidean_distance([r2[1]],[r1[1]])**2+euclidean_distance(r2[2:7],r1[2:7])**2)

            if dist<distance:

                distance=dist

                date=r2[0]

        distances.append((r1[0],distance))

    distances.sort(key=lambda tup: tup[1])

    Simi=list()

    for i in range(0,8):

        Simi.append(distances[i][0])

    return Simi

#/////////////////////////////////////////////////////////////////////////////////


def DisLikeList(AllData,Datars):
#list of dislike date

    distances=list()

    for r2 in AllData:

        distance=sqrt(euclidean_distance([Datars[0][1]],[r2[1]])**2+jaccard_distance(Datars[0][2:8],r2[2:8])**2)

        date=Datars[0][0]

        for r1 in Datars:

            if r1==r2:

                continue

            dist=sqrt(euclidean_distance([r1[1]],[r2[1]])**2+jaccard_distance(r1[2:8],r2[2:8])**2)

            if dist<distance:

                distance=dist

                date=r1[0]

        if r2 not in Datars:

            distances.append((r2[0],distance))

    #distances.sort(key=lambda tup: tup[1],reverse=True)
    
    distances.sort(key=lambda tup: tup[1])

    Simi=list()

    for i in range(8):

        Simi.append(distances[i][0])
       

    return set(Simi)



#//////////////////////////Dataset///////////////////////////////////////////////////////////////


datasetPrice=[[UpdateD['Имя'][i],UpdateD['Цена'][i]] for i in range(0,49)]

datasetFF=[[UpdateD['Имя'][i],UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i], UpdateD['жесткость'][i]] for i in range(0,49)]

dataset=[[UpdateD['Имя'][i],UpdateD['Цена'][i],UpdateD['Страна'][i],UpdateD['Регион'][i],UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i], UpdateD['жесткость'][i]] for i in range(0,49)]

datasetCountry=[[UpdateD['Имя'][i],UpdateD['Страна'][i]] for i in range(0,49)]


print("///////////////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////////////")
print('                      Добро пожаловать                             ')
print('                           Финики                                  ')
print('                  Рекомендательная система                         ')
print("///////////////////////////////////////////////////////////////////\n")
while True:
  
    try:
        Enter=int(input('Пожалуйста,\n\n нажмите 1 если хотите искать по одному объекту \n\n нажмите 2 если хотите по списку лайков \n\n нажмите 3 если хотите по списку дизлайков\n\n нажмите 4 для параметрического поиска по фильтрам \n\n нажмите 5 если вы хотите умный диалог \n\n Для выхода нажмите 0 \n\n ---->> '))
    except ValueError:
        print("//////////////////////Error !! /////////////////////////////////")
        print("Пожалуйста, введите только цифры из списка ниже !!")
        print("///////////////////////////////////////////////////////////////\n")
        continue    
    ii =0
    ff = 49
    if Enter==1:
                Date=UpdateD['Имя'].to_list()
                NDate1 = Date[0:15]
                NDate2 = Date[16:31]    
                NDate3 = Date[32:48]   
                print("\n")
                print("////////////////////////////////////// THE LIST of DATES - СПИСОК ФИНИКИ /////////////////////////////////////////////////////////////////////////////////////////////")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(NDate1)
                print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print(NDate2)
                print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print(NDate3)
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("\n")

                Input=input('Пожалуйста, выберите одну финтк из списка:\n ---->> ')

                #ResultsNum=int(input('Пожалуйста, сколько похожих товаров вы хотите видеть:\n'))

                if Input in Date:

                    index=0;

                    for i in range(ii,ff):

                        if Date[i]==Input:

                            index=i

                            break
                    
                    #print(UpdateD)
                    SimiData1={'Подобие-евклидово по Размер, Цвет, Сладость и жесткость':similarity(datasetFF, datasetFF[index],'a')}
                    SimiData2={'Сходство-евклидово по Цена($)/Кг':similarity(datasetPrice, datasetPrice[index],'p')}
                   
                    
                    
        
                    recommended1=pd.DataFrame(SimiData1)
                    recommended2=pd.DataFrame(SimiData2)
                    
            
                
                    print(recommended1)
                    print(recommended2)
               
                    
                   
                    

                    print('\n')

                    print('\n')

                #++++++++++++++++++++++++++++++++++++??????????????????????????????????????????????????
                    
                    print('Сходство рекомендаций по лайкам:\n')

                    LikeDate=LikeOne(dataset,dataset[index])
                    #print(LikeDate)
                
                    for Simi in LikeDate:

                        print(Simi)

                    print('\n')
                    

                else:

                    print("Другие варианты, возможно, вам понравятся:")

                    index=random.randint(ii,ff)

                    print('\n')

                    LikeDate=LikeOne(dataset,dataset[index])

                    for Simi in LikeDate:

                        print(Simi)

                    print('\n')

    #/////////////////////////////////////////////////////////////////////////////////////////////

    elif Enter==2:
                Date=UpdateD['Имя'].to_list()
                Name=UpdateD['Имя'].to_list()

                print()

                print(Name)

                print()

                ListDates = []

                k=1
                for k in range(0,49):
                
                    print("<<Пожалуйста, введите финик, которая вам нравится:")

                    ListOfNames = input(f"\n --> Нравится номер {k}: ")
                    ListDates.append(ListOfNames)

                    if ListOfNames in Date:

                        index=0;

                    for i in range(ii,ff):

                        if Date[i]==ListOfNames:

                            index=i

                            break

                    End = int(input("\n Вы хотите продолжить, пожалуйста, введите 1, в противном случае введите 0 >> "))

                    if End == 0:
                        break;
                
                print("Ваш список Вам нравится:\n ")
                print(ListDates)

                #ResultsNum=int(input('Пожалуйста, сколько похожих товаров вы хотите видеть >> \n'))

                #ListDates=ListDates.split(',')

            

                LLN=[Name1 for Name1 in ListDates if Name1 in Name]
                #o = 1
                if not LLN:
                #if o == 1:

                    print("Другие варианты, возможно, вам понравятся:")

                    index=random.randint(ii,ff)

                    print('\n')

                    #recommended_dates=LikeOne(dataset,dataset[index],ResultsNum)
                    recommended_dates=LikeOne(dataset,dataset[index])

                    for Simi in recommended_dates:

                        print(Simi)

                    print('\n')

                else:

                        
                    dataset_tests=[[UpdateD['Имя'][i],UpdateD['Цена'][i], UpdateD['Страна'][i],UpdateD['Регион'][i], UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i],UpdateD['жесткость'][i]] for i in range(ii,ff) if UpdateD['Имя'][i] in LLN]

                    print('\n Рекомендуемые финики для вас:\n')

                    LikeList=LikeList(dataset,dataset_tests)

                    for Simi in LikeList:

                        print(Simi)

    elif Enter==3:
                Date=UpdateD['Имя'].to_list()
                Name=UpdateD['Имя'].to_list()

                print()

                print(Name)

                print()

                DListDates = []

                k=1
                for k in range(0,49):
                
                    print("<<Пожалуйста, введите финик, которая вам не нравится:")

                    ListOfNames = input(f"\n --> Не Нравится номер {k}: ")
                    DListDates.append(ListOfNames)

                    if ListOfNames in Date:

                        index=0;

                    for i in range(ii,ff):

                        if Date[i]==ListOfNames:

                            index=i

                            break

                    End = int(input("\n Вы хотите продолжить, пожалуйста, введите 1, в противном случае введите 0 >> "))

                    if End == 0:
                        break;
                
                print("Ваш список Вам  не нравится:\n ")
                print(DListDates)

                #ResultsNum=int(input('Пожалуйста, сколько похожих товаров вы хотите видеть >> \n'))

                

                LLN=[Name1 for Name1 in DListDates if Name1 in Name]

                if not LLN:

                    print("Другие варианты, возможно, вам понравятся:")

                    index=random.randint(ii,ff)

                    print('\n')

                    DateRecom=LikeOne(dataset,dataset[index])

                    for Simi in DateRecom:

                        print(Simi)

                    print('\n')

                else:

                

                    dataset_tests=dataset_tests=[[UpdateD['Имя'][i],UpdateD['Цена'][i], UpdateD['Страна'][i],UpdateD['Регион'][i], UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i],UpdateD['жесткость'][i]] for i in range(ii,ff) if UpdateD['Имя'][i] in LLN]

                    print('\n Рекомендуемые финики не нравится для вас: \n')

                    DisLikeRecom=DisLikeList(dataset,dataset_tests)

                    for Simi in DisLikeRecom:

                        print(Simi)    


    elif Enter == 4:

    #/////////////////////////////////////////////////////////////////////////
    #///////////////Filter System//////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////
            AllDataFilter = data
            DataNumberFilter = UpdateD
            print("///////////////////////////////////////////////////////////////////")
            print("///////////////////////////////////////////////////////////////////")
            print('                           Финики                                  ')
            print('                  Рекомендательная система                         ')
            print('            параметрического поиска по фильтрам                    ')
            print("///////////////////////////////////////////////////////////////////\n")
        
            LikeList = []
            DisLikeList = []
            LikeList2 = []
            DisLikeList2 = []
            #datasetLike2=pd.DataFrame(columns=['Имя','Цена($)/Кг','Страна','Регион','Размер','Цвет','Сладость','жесткость/влажность'], index=range(0, 49))
            #datasetLike2=pd.DataFrame(columns=['Имя','Страна'], index=range(0, 49))
            #print(datasetLike2)

            #вопрос - Country /////////////
            Testss = 0
            while Testss == 0:
                Questioni = input('Вы хотите финики из конкретной страны или из любого места (Да или нет)? >> ')
                Questionii = Questioni.lower()
                Optioni = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
                Optionii = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
                Sign = 0 
                for i in range(0,10):
                    if Optioni[i] in Questionii:
                        Sign = 1   
                        Testss = 1 
                        break
                    elif Optionii[i] in Questionii:
                        LikeList.append(UpdateD)
                        LikeList2.append(data)
                        Sign = 2
                        Testss = 1
                        break 
                    else: 
                        Testss = 0
                if Testss == 0:
                        print("Ошибка !! мы не можем вас понять, пожалуйста, введите еще раз !!")
                else:
                    break

            if Sign == 1:

            #вопрос/////////////
                Testss = 0
                while Testss == 0:
                    Question4 = input('Вам нравится, что это из Саудовской Аравии? >> ')

                    Question44 = Question4.lower()

                    Option1 = ["да", "согласие", "саудовск","важно","yes", "соглас", "саудов","важн", "da","важ"] 
                    Option2 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","безразницы"]

                    for i in range(0,10):
                        if Option1[i] in Question44:                 
                            newDataF = UpdateD.loc[(UpdateD.Страна == 1)]
                            #newDataFTT = UpdateD.loc[(UpdateD.Страна == 0)]
                            #newitem = list(filter(newDataFTT,DataNumberFilter))
                            LikeList.append(newDataF)
                            #newDataF2 = data.loc[(data.Страна == "Саудовская Аравия"),(data.Страна == "Иран"),(data.Страна == "Эмирейтс")] 
                            #datasetLike2.append(newDataF2)
                            newdf1 = data.loc[(data.Страна == "Саудовская Аравия")] 
                            LikeList2.append(newdf1)
                            Sign  = 1
                            Testss = 1
                            break
                        elif Option2[i] in Question44:
                            newDataF = UpdateD.loc[(UpdateD.Страна == 1)]
                            DisLikeList.append(newDataF)
                            newDataF2 = data.loc[(data.Страна == "Саудовская Аравия")]
                            DisLikeList2.append(newDataF2)
                            Sign  = 1
                            Testss = 1
                            break
                        else:
                            Testss = 0
                    if Testss == 0:   
                         print("Ошибка !! мы не можем вас понять, пожалуйста, введите еще раз !!")
                    else:
                        break 
                if Sign == 1:
                    #вопрос/////////////
                    Testss = 0
                    while Testss == 0:
                            Question5 = input('Вам нравится, что это из Иран? >> ')

                            Question55 = Question5.lower()

                            Option11 = ["да", "согласие", "Иран","важно","yep", "согл", "y","важн", "da","важ"] 
                            Option22 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","безразницы"]

                            for i in range(0,10):
                                if Option11[i] in Question55:
                                    newDataF = UpdateD.loc[(UpdateD.Страна == 0)]
                                    LikeList.append(newDataF)
                                    newDataF2 = data.loc[(data.Страна == "Иран")] 
                                    LikeList2.append(newDataF2)
                                    Sign  = 1
                                    Testss = 1
                                    break
                                    #datasetLike2.append(newDataF2)                                       
                                elif Option22[i] in Question55:
                                    newDataF = UpdateD.loc[(UpdateD.Страна == 0)]
                                    DisLikeList.append(newDataF)
                                    newDataF2 = data.loc[(data.Страна == "Иран")]
                                    DisLikeList2.append(newDataF2)
                                    Sign  = 1
                                    Testss = 1
                                    break
                                else:
                                    Testss = 0
                            if Testss == 0:   
                                print("Ошибка !! мы не можем вас понять, пожалуйста, введите еще раз !!")
                            else:
                                break 
                if Sign == 1:  
            #вопрос/////////////
                        Testss = 0
                        while Testss == 0:
                                Question6 = input('Вам нравится, что это из Эмирейтс? >> ')

                                Question66 = Question6.lower()

                                Option111 = ["да", "согласие", "Эмирейтс","важно","yep", "согл", "y","важн", "da","важ"] 
                                Option222 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]

                                for i in range(0,10):
                                    if Option111[i] in Question66:
                                        newDataF = UpdateD.loc[(UpdateD.Страна == 2)]
                                        LikeList.append(newDataF)
                                        newDataF2 = data.loc[(data.Страна == "Эмирейтс")] 
                                        LikeList2.append(newDataF2)
                                        Sign  = 2
                                        Testss = 1
                                        break
                                    elif Option222[i] in Question66:
                                        newDataF = UpdateD.loc[(UpdateD.Страна == 2)]
                                        DisLikeList.append(newDataF)
                                        newDataF2 = data.loc[(data.Страна == "Эмирейтс")]
                                        DisLikeList2.append(newDataF2)
                                        Sign  = 2
                                        Testss = 1
                                        break
                                    else:
                                        Testss = 0
                                if Testss == 0:   
                                    print("Ошибка !! мы не можем вас понять, пожалуйста, введите еще раз !!")
                                else:
                                    break 
            if Sign == 2:  
                            print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                            for k in range(len(LikeList2)):
                                print(LikeList2[k])
                                print("-------------------------------------------------------------------------------------------------------------------\n")
                            print("\n")
                            #вопрос - Region /////////////
                            RegionList = []
                            RegionList2 = []
                            RegionData = []
                            RD = []
                            Question2  = input('Вы хотите искать по региону страны? (Да или нет)? >> ')
                        
                            Questioni22 = Question2.lower()
                            Optioni2 = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
                            Optionii2 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
                            Sign = 0 
                            for i in range(0,10):
                                    if Optioni2[i] in Questioni22:
                                        Sign = 1    
                                    elif Optionii2[i] in Questioni22:
                                        RegionList.append(LikeList2)
                                        RegionList2 = LikeList2
                                        
                            

                            if Sign == 1:
                                Sign = 0
                                for i in range(len(LikeList2)):
                                
                                    RegDa=LikeList2[i]['Регион'].to_list()
                                    RegionData.append(RegDa)

                                #for j in range(len(RegionData)):
                                    #RDD = list(dict.fromkeys(RegionData[j]))
                                    #RD.append(RDD)
                            
                                TT = []
                                for ii in range(len(RegionData)):
                                    TT = TT+ RegionData[ii]
                    

                                RDnew = list(dict.fromkeys(TT))

                                print("Пожалуйста, выберите Регионы из списка ниже по имени: \n ")
                                N=1
                                print("-------------")
                                for i in range(len(RDnew)):
                                        print(f"Регион#{+N}")
                                        pprint(RDnew[i])
                                        print("-------------")
                                        N=N+1
                                T = 0
                                B = 0
                                count = len(RDnew)
                                Ques = []
                                while T == 0:
                                        while B == 0:
                                            Questioni2 = input(' \n Войти Регион ----> ')
                                            if Questioni2 == Ques:
                                                print("Он уже выбран!! пожалуйста, введите другой!!")
                                            else:
                                                B=1
                                        B=0    
                                        if Questioni2 in RDnew:
                                            for y in range(len(LikeList2)):
                                                REGD = LikeList2[y].loc[(LikeList2[y].Регион == Questioni2)] 
                                                #REGD = data.loc[(data.Регион == Questioni2)] 
                                                RegionList.append(REGD)
                                                RegionList2.append(REGD)
                                            T =1
                                            count = count -1
                                            Ques = Questioni2
                                            if count == 0:
                                                T=1
                                                break
                                        else:
                                            print("Пожалуйста, введите название региона из списка !!")
                                        if T == 1:
                                            try:
                                                T=0
                                                ss = int(input("Если вы хотите продолжить добавление региона, нажмите 1, иначе нажмите 0: >> "))
                                            except ValueError:
                                                    print("--Error !! --")
                                                    print("Пожалуйста, введите только цифры !!")
                                                    continue
                                            if ss == 0:
                                                break
                                print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                                for k in range(len(RegionList2)):
                                    print(RegionList2[k])
                                    print("-------------------------------------------------------------------------------------------------------------------\n")
                                    print("\n")
                            if Sign == 0:        
                                    #вопрос - Size /////////////
                                    SizeData = []
                                    SD = []
                                    SizeList = []
                                    SizeList2 = []
                                            
                                    Question3  = input('Вы хотите искать по Размер? (Да или нет)? >> ')
                                
                                    Questioni33 = Question3.lower()
                                    Optioni3 = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
                                    Optionii3 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
                                    Sign = 0 
                                    for i in range(0,10):
                                            if Optioni3[i] in Questioni33:
                                                Sign = 1    
                                            elif Optionii3[i] in Questioni33:
                                                SizeList.append(RegionList2)
                                                SizeList2 = RegionList2
                                                

                                    if Sign == 1:              
                                                Sign = 0
                                                for i in range(len(RegionList2)):
                                                
                                                    RegDa=RegionList2[i]['Размер'].to_list()
                                                    SizeData.append(RegDa)
                                                
                                                TT = []
                                                for ii in range(len(SizeData)):
                                                    TT = TT+ SizeData[ii]
                                    

                                                SD = list(dict.fromkeys(TT))
                                        
                                                N=1
                                                print("Пожалуйста, выберите Размер из списка ниже по имени: \n ")
                                                print("-------------")
                                                for i in range(len(SD)):
                                                        print(f"Размер#{+N}")
                                                        pprint(SD[i])
                                                        print("-------------")
                                                        N=N+1
                                                T = 0
                                                B = 0
                                                count = len(SD)
                                                Ques = []

                                                while T == 0:
                                                        while B == 0:
                                                            Questioni2 = input(' \n Войти Размер ----> ')
                                                            if Questioni2 == Ques:
                                                                print("Он уже выбран!! пожалуйста, введите другой!!")
                                                            else:
                                                                B=1
                                                        B=0    
                                                        if Questioni2 in SD:
                                                            for y in range(len(RegionList2)):
                                                                REGD = RegionList2[y].loc[(RegionList2[y].Размер == Questioni2)] 
                                                                #REGD = data.loc[(data.Размер == Questioni2)] 
                                                                SizeList.append(REGD)
                                                                SizeList2.append(REGD)
                                                            T =1
                                                            count = count -1
                                                            Ques = Questioni2
                                                            if count == 0:
                                                                T=1
                                                                break
                                                        else:
                                                            print("Пожалуйста, введите название размера из списка !!")
                                                        if T == 1:
                                                            try:
                                                                T=0
                                                                ss = int(input("Если вы хотите продолжить добавление размера, нажмите 1, иначе нажмите 0: >> "))
                                                            except ValueError:
                                                                    print("--Error !! --")
                                                                    print("Пожалуйста, введите только цифры !!")
                                                                    continue
                                                            if ss == 0:
                                                                break      
                                        
                                                print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                                                for k in range(len(SizeList2)):
                                                    print(SizeList2[k])
                                                    print("-------------------------------------------------------------------------------------------------------------------\n")
                                                    print("\n")
                                    if Sign == 0:             
                                                #вопрос - Color /////////////
                                                ColorList = []
                                                ColorList2 = []
                                                ColorData = []
                                                CD = []
                                                Question4  = input('Вы хотите искать по Цвет? (Да или нет)? >> ')
                                            
                                                Questioni44 = Question4.lower()
                                                Optioni4 = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
                                                Optionii4 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
                                                Sign = 0 
                                                for i in range(0,10):
                                                        if Optioni4[i] in Questioni44:
                                                            Sign = 1    
                                                        elif Optionii4[i] in Questioni44:
                                                            ColorList.append(SizeList2)
                                                            ColorList2 = SizeList2
                                                            Sign = 0
                                                if Sign == 1:
                                                    Sign = 0
                                                    for i in range(len(SizeList2)):
                                                    
                                                        RegDa=SizeList2[i]['Цвет'].to_list()
                                                        ColorData.append(RegDa)
                                                    
                                                    TT = []
                                                    for ii in range(len(ColorData)):
                                                        TT = TT+ ColorData[ii]

                                                    CD = list(dict.fromkeys(TT))
                                                
                                                    N=1
                                                    print("Пожалуйста, выберите Цвет из списка ниже по имени: \n ")
                                                    print("-------------")
                                                    for i in range(len(CD)):
                                                            print(f"Цвет#{+N}")
                                                            pprint(CD[i])
                                                            print("-------------")
                                                            N=N+1
                                                
                                                    T = 0
                                                    B = 0
                                                    count = len(TT)
                                                    Ques = []
                                                    while T == 0:
                                                            while B == 0:
                                                                Questioni2 = input(' \n Войти Цвет ----> ')
                                                                if Questioni2 == Ques:
                                                                    print("Он уже выбран!! пожалуйста, введите другой!!")
                                                                else:
                                                                    B=1
                                                            B=0    
                                                            if Questioni2 in TT:
                                                                for y in range(len(SizeList2)):
                                                                    REGD = SizeList2[y].loc[(SizeList2[y].Цвет == Questioni2)] 
                                                                    #REGD = data.loc[(data.Цвет == Questioni2)] 
                                                                    ColorList.append(REGD)
                                                                    ColorList2.append(REGD)
                                                                T =1
                                                                count = count -1
                                                                Ques = Questioni2
                                                                if count == 0:
                                                                    T=1
                                                                    break
                                                            else:
                                                                print("Пожалуйста, введите название цвета из списка !!")
                                                            if T == 1:
                                                                try:
                                                                    T=0
                                                                    ss = int(input("Если вы хотите продолжить добавление цвета, нажмите 1, иначе нажмите 0: >> "))
                                                                except ValueError:
                                                                        print("--Error !! --")
                                                                        print("Пожалуйста, введите только цифры !!")
                                                                        continue
                                                                if ss == 0:
                                                                    break         
                                                    print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                                                    for k in range(len(ColorList2)):
                                                        print(ColorList2[k])
                                                        print("-------------------------------------------------------------------------------------------------------------------\n")
                                                    print("\n")
                                                if Sign == 0:
                                                    #вопрос - Sweetness /////////////
                                                    SweetList = []
                                                    SweetList2 = []
                                                    SweetData = []
                                                    SWD = []
                                                    Question5  = input('Вы хотите искать по Сладость? (Да или нет)? >> ')
                                                
                                                    Questioni55 = Question5.lower()
                                                    Optioni5 = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
                                                    Optionii5 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
                                                    Sign = 0 
                                                    for i in range(0,10):
                                                            if Optioni5[i] in Questioni55:
                                                                Sign = 1    
                                                            elif Optionii5[i] in Questioni55:
                                                                SweetList.append(ColorList2)
                                                                SweetList2 = ColorList2
                 
                                                    if Sign == 1:
                                                        Sign = 0
                                                        for i in range(len(ColorList2)):
                                                        
                                                            RegDa=ColorList2[i]['Сладость'].to_list()
                                                            SweetData.append(RegDa)
                                                        
                                                        TT = []
                                                        for ii in range(len(SweetData)):
                                                            TT = TT+ SweetData[ii]

                                                        SWD = list(dict.fromkeys(TT))
                                                    
                                                        N=1
                                                        print("Пожалуйста, выберите Сладость из списка ниже по имени: \n ")
                                                        print("-------------")
                                                        for i in range(len(SWD)):
                                                                print(f"Сладость#{+N}")
                                                                pprint(SWD[i])
                                                                print("-------------")
                                                                N=N+1
                                        
                                                        T = 0
                                                        B = 0
                                                        count = len(SWD)
                                                        Ques = []
                                                        while T == 0:
                                                                while B == 0:
                                                                    Questioni2 = input(' \n Войти Сладость ----> ')
                                                                    if Questioni2 == Ques:
                                                                        print("Он уже выбран!! пожалуйста, введите другой!!")
                                                                    else:
                                                                        B=1
                                                                B=0    
                                                                if Questioni2 in SWD:
                                                                    for y in range(len(ColorList2)):
                                                                        REGD = ColorList2[y].loc[(ColorList2[y].Сладость == Questioni2)] 
                                                                        #REGD = ColorList2.loc[(ColorList2.Сладость == Questioni2)] 
                                                                        SweetList.append(REGD)
                                                                        SweetList2.append(REGD)
                                                                    T =1
                                                                    count = count -1
                                                                    Ques = Questioni2
                                                                    if count == 0:
                                                                        T=1
                                                                        break
                                                                else:
                                                                    print("Пожалуйста, введите название Сладость из списка !!")
                                                                if T == 1:
                                                                    try:
                                                                        T=0
                                                                        ss = int(input("Если вы хотите продолжить добавление Сладость, нажмите 1, иначе нажмите 0: >> "))
                                                                    except ValueError:
                                                                            print("--Error !! --")
                                                                            print("Пожалуйста, введите только цифры !!")
                                                                            continue
                                                                    if ss == 0:
                                                                         break       
                                                        print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                                                        for k in range(len(SweetList2)):
                                                            print(SweetList2[k])
                                                            print("-------------------------------------------------------------------------------------------------------------------\n")
                                                        print("\n")
                                                    if Sign ==0:
                                                        #вопрос - hardness/humidity /////////////
                                                        HardList = []
                                                        HardList2 = []
                                                        HardData = []
                                                        HD = []
                                                        Question6  = input('Вы хотите искать по жесткость? (Да или нет)? >> ')
                                                    
                                                        Questioni66 = Question6.lower()
                                                        Optioni6 = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
                                                        Optionii6 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
                                                        Sign = 0 
                                                        for i in range(0,10):
                                                                if Optioni6[i] in Questioni66:
                                                                    Sign = 1    
                                                                elif Optionii6[i] in Questioni66:
                                                                    HardList.append(SweetList2)  
                                                                    HardList2 = SweetList2       

                                                        if Sign == 1:
                                                            Sign = 0
                                                            for i in range(len(SweetList2)):
                                                            
                                                                RegDa=SweetList2[i]['жесткость'].to_list()
                                                                HardData.append(RegDa)
                                                            
                                                            TT = []
                                                            for ii in range(len(HardData)):
                                                                TT = TT+ HardData[ii]

                                                            HD = list(dict.fromkeys(TT))
                                                        
                                                            N=1
                                                            print("Пожалуйста, выберите жесткость из списка ниже по имени: \n ")
                                                            print("-------------")
                                                            for i in range(len(HD)):
                                                                    print(f"жесткость#{+N}")
                                                                    pprint(HD[i])
                                                                    print("-------------")
                                                                    N=N+1

                                                            T = 0
                                                            B = 0
                                                            count = len(TT)
                                                            Ques = []
                                                            while T == 0:
                                                                    while B == 0:
                                                                        Questioni2 = input(' \n Войти жесткость ----> ')
                                                                        if Questioni2 == Ques:
                                                                            print("Он уже выбран!! пожалуйста, введите другой!!")
                                                                        else:
                                                                            B=1
                                                                    B=0    
                                                                    if Questioni2 in TT:
                                                                        for y in range(len(SweetList2)):
                                                                            REGD = SweetList2[y].loc[(SweetList2[y].жесткость == Questioni2)] 
                                                                            #REGD = data.loc[(data.жесткость == Questioni2)] 
                                                                            HardList.append(REGD)
                                                                            HardList2.append(REGD)
                                                                        T =1
                                                                        count = count -1
                                                                        Ques = Questioni2
                                                                        if count == 0:
                                                                            T=1
                                                                            break
                                                                    else:
                                                                        print("Пожалуйста, введите название жесткость из списка !!")
                                                                    if T == 1:
                                                                        try:
                                                                            T=0
                                                                            ss = int(input("Если вы хотите продолжить добавление жесткость, нажмите 1, иначе нажмите 0: >> "))
                                                                        except ValueError:
                                                                                print("--Error !! --")
                                                                                print("Пожалуйста, введите только цифры !!")
                                                                                continue
                                                                        if ss == 0:
                                                                            break           

                                                            print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                                                            for k in range(len(HardList2)):
                                                                print(HardList2[k])
                                                                print("-------------------------------------------------------------------------------------------------------------------\n")
                                                                print("\n")
                 
    elif Enter == 5:

                print("///////////////////////////////////////////////////////////////////")
                print("///////////////////////////////////////////////////////////////////")
                print('                           Финики                                  ')
                print('                  Рекомендательная система                         ')
                print('                        умный диалог                               ')
                print("///////////////////////////////////////////////////////////////////\n")

                #второй вопрос/////////////
                LikeList5 = []
                DaiList = data
                Test = 0
                Testss = 0
                Tests = 0
                while Tests == 0:
                    Questioni = input('Вы хотите финики из конкретной страны или из любого места (Да или нет)? >> ')
                    Questionii = Questioni.lower()
                    Optioni = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
                    Optionii = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
                    Sign = 0 
                    Testss = 0
                    for i in range(0,10):
                        if Optioni[i] in Questionii:
                            Sign = 1   
                            Testss = 1 
                            break
                        elif Optionii[i] in Questionii:
                            newDataF = DaiList.loc[(DaiList.Страна == "Саудовская Аравия")]
                            LikeList5.append(newDataF)
                            newDataF = DaiList.loc[(DaiList.Страна == "Иран")]
                            LikeList5.append(newDataF)
                            newDataF = DaiList.loc[(DaiList.Страна == "Эмирейтс")]
                            LikeList5.append(newDataF)
                            Sign = 2
                            Testss = 1
                            break 
                        else: 
                            Testss = 0
                    if Testss == 0:
                            print("Ошибка !! мы не можем вас понять, пожалуйста, введите еще раз !!")
                    else:
                        break

                if Sign == 1:
                        Testss = 0
                        while Testss == 0:
                            Question4 = input('Вам нравится, что это из Саудовской Аравии? >> ')

                            Question44 = Question4.lower()

                            Option1 = ["да", "согласие", "саудовск","важно","yes", "соглас", "саудов","важн", "da","важ"] 
                            Option2 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","безразницы"]

                            for i in range(0,10):
                                if Option1[i] in Question44:                 
                                    newDataF = DaiList.loc[(DaiList.Страна == "Саудовская Аравия")]
                                    LikeList5.append(newDataF)
                                    Sign  = 1
                                    Testss = 1
                                    break
                                elif Option2[i] in Question44:
                                    newDataF2 = data.loc[(data.Страна == "Саудовская Аравия")]
                                    #DisLikeList2.append(newDataF2)
                                    Sign  = 1
                                    Testss = 1
                                    break
                                else:
                                    Testss = 0
                            if Testss == 0:   
                                print("Ошибка !! мы не можем вас понять, пожалуйста, введите еще раз !!")
                            else:
                                break 
                        if Sign == 1:
                            #вопрос/////////////
                            Testss = 0
                            while Testss == 0:
                                    Question5 = input('Вам нравится, что это из Иран? >> ')
                                    Question55 = Question5.lower()
                                    Option11 = ["да", "согласие", "Иран","важно","yep", "согл", "y","важн", "da","важ"] 
                                    Option22 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","безразницы"]
                                    for i in range(0,10):
                                        if Option11[i] in Question55:
                                            newDataF2 = data.loc[(data.Страна == "Иран")] 
                                            LikeList5.append(newDataF2)
                                            Sign  = 1
                                            Testss = 1
                                            break
                                            #datasetLike2.append(newDataF2)                                       
                                        elif Option22[i] in Question55:
                                            newDataF2 = data.loc[(data.Страна == "Иран")]
                                            Sign  = 1
                                            Testss = 1
                                            break
                                        else:
                                            Testss = 0
                                    if Testss == 0:   
                                        print("Ошибка !! мы не можем вас понять, пожалуйста, введите еще раз !!")
                                    else:
                                        break 
                        if Sign == 1:  
                    #вопрос/////////////
                                Testss = 0
                                while Testss == 0:
                                        Question6 = input('Вам нравится, что это из Эмирейтс? >> ')

                                        Question66 = Question6.lower()

                                        Option111 = ["да", "согласие", "Эмирейтс","важно","yep", "согл", "y","важн", "da","важ"] 
                                        Option222 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]

                                        for i in range(0,10):
                                            if Option111[i] in Question66:
                                                newDataF2 = data.loc[(data.Страна == "Эмирейтс")] 
                                                LikeList5.append(newDataF2)
                                                Sign  = 2
                                                Testss = 1
                                                break
                                            elif Option222[i] in Question66:
                                                newDataF2 = data.loc[(data.Страна == "Эмирейтс")]
                                                Sign  = 2
                                                Testss = 1
                                                break
                                            else:
                                                Testss = 0
                                        if Testss == 0:   
                                            print("Ошибка !! мы не можем вас понять, пожалуйста, введите еще раз !!")
                                        else:
                                            break 
                '''
                print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                for k in range(len(LikeList5)):
                        print(LikeList5[k])
                        print("-------------------------------------------------------------------------------------------------------------------\n")
                        print("\n")
                '''      

                while Test == 0:
                        Sweet5 = []
                        LikeList51 = []
                        print('Какие финики самое сладкий ? \n')
                        print("(Намекать: слишком сладкий, сладкий, сироп, прайминги, медовый, кислый)\n")
                        Question2 = input(' ---->>>> ')
                        Question22 = Question2.lower()
                    
                        sweetness11 = ["слишком", "слишк", "очен", "чересчур", "приторно"] #слова-синонимы
                        sweetness12 = ["сладкий", "сладк", "сладк", "сладк", " "]
                        sweetness22 = ["сладкий", "сладк", "конфе", "конф"]
                        sweetness33 = ["сироп", "сиро", "сиропы", "сир"]
                        sweetness44 = ["прайминги", "прайминг", "грунтовки", "грунтов"]
                        sweetness55 = ["медовый", "мед", "мёд", "медо"]
                        sweetness66 = ["кислый", "кисл", "прокисший", "прокисш"]

                        TT = 0
                        for i in range(0,4):
                            if sweetness11[i] in Question22 and sweetness12[i] in Question22:
                                for y in range(len(LikeList5)):
                                    REGD = LikeList5[y].loc[(LikeList5[y].Сладость == "слишком сладкий")] 
                                    Sweet5.append(REGD)
                                Test = 1
                                TT = 1
                            if sweetness22[i] in Question22:
                                for y in range(len(LikeList5)):
                                    REGD = LikeList5[y].loc[(LikeList5[y].Сладость == "сладкий")] 
                                    Sweet5.append(REGD)
                                Test = 1
                            if sweetness33[i] in Question22:
                                for y in range(len(LikeList5)):
                                    REGD = LikeList5[y].loc[(LikeList5[y].Сладость == "сироп")] 
                                    Sweet5.append(REGD)
                                Test = 1
                            if sweetness44[i] in Question22:
                                 for y in range(len(LikeList5)):
                                    REGD = LikeList5[y].loc[(LikeList5[y].Сладость == "прайминги")] 
                                    Sweet5.append(REGD)
                                 Test = 1
                            if sweetness55[i] in Question22:
                                for y in range(len(LikeList5)):
                                    REGD = LikeList5[y].loc[(LikeList5[y].Сладость == "медовый")] 
                                    Sweet5.append(REGD)
                                Test = 1
                            if sweetness66[i] in Question22:
                                for y in range(len(LikeList5)):
                                    REGD = LikeList5[y].loc[(LikeList5[y].Сладость == "кислый")] 
                                    Sweet5.append(REGD)
                                Test = 1
                        
                        if Test == 1:
                            break
                        print("не могу тебя понять, Можешь объяснить подробнее, пожалуйста!?")

                    #Третий вопрос/////////////Price//////
             
                if TT == 1:
                     print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                     print(Sweet5[0])
                     print("-------------------------------------------------------------------------------------------------------------------\n")
                else:
                    print("\n")
                    print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                    for k in range(len(Sweet5)):
                        print(Sweet5[k])
                        print("-------------------------------------------------------------------------------------------------------------------\n")
                    print("\n")  
               
                
                Test = 0
                while Test == 0:
                        Price5 =[]
                        LikeList51 = []
                        Pricee = []
                        NewPricee5 = []
                        print('Какой ценовой диапазон предпочитаете? Пожалуйста,\n выберите из списка ниже: \n 1- дорогой \n 2- средний \n 3- недорогой\n')
                        Question3 = int(input(' ---->>>> '))
                   
                    #Question3 = int(input('Какой ценовой диапазон предпочитаете? Пожалуйста, выберите из списка ниже: \n 1- от 5$ до 20$\n 2- от 20$ до 30$\n 3- от 30$ до 45$\n'))
                    
                        for i in range(len(Sweet5)):
                                                                    
                                RegDa=Sweet5[i]['Цена'].to_list()
                                Pricee.append(RegDa)

                        if Question3 == 1:
                            for i in range(len(Pricee)):
                                for j in range(len(Pricee[i])):
                                    if Pricee[i][j] >= 30:
                                        PP = Pricee[i][j]
                                        REGD = Sweet5[i].loc[(Sweet5[i].Цена == PP)] 
                                        NewPricee5.append(REGD)
                            Test = 1
                        elif Question3 == 2:
                            for i in range(len(Pricee)):
                                for j in range(len(Pricee[i])):
                                    if Pricee[i][j] <= 30 and Pricee[i][j] >= 15:
                                        PP = Pricee[i][j]
                                        REGD = Sweet5[i].loc[(Sweet5[i].Цена == PP)] 
                                        NewPricee5.append(REGD)
                            Test = 1
                        elif Question3 == 3:
                            for i in range(len(Pricee)):
                                for j in range(len(Pricee[i])):
                                    if Pricee[i][j] <= 15:
                                        PP = Pricee[i][j]
                                        REGD = Sweet5[i].loc[(Sweet5[i].Цена == PP)] 
                                        NewPricee5.append(REGD)
                            Test = 1

                        if Test == 1:
                            break 

                        print("пожалуйста, введите правильный ввод!!")

                  #Третий вопрос///////
                if NewPricee5[0].empty == False:
                    print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                    for k in range(len(NewPricee5)):
                            print(NewPricee5[k])
                            print("-------------------------------------------------------------------------------------------------------------------\n")
                            print("\n")
                
                Test = 0
                while Test == 0:
                #вопрос/////////////
                        Hard5 = []
                        print('Какие финики самое мягкий или полусухой или сухой ? \n')
                        print("(Намекать: мягкий, полусухой, сухой)\n")
                        Question1 = input(' ---->>>> ')
                        Question11 = Question1.lower()
                        #ListAnswer = nltk.word_tokenize(Question11)
                        ListAnswer = Question11
                    

                        #hardnessList1 = ["мягкий", "легкий", "слабый","мяг", "лег", "сла"] #слова-синонимы
                        hardnessList1 = ["мяг", "легк", "слаб"] #слова-синонимы
                        hardnessList2 = ["полусух", "полусух", "полусух"]
                        hardnessList3 = ["сухой", "суши", "сдержан"]

                        for i in range(0,3):
                            if hardnessList1[i] in ListAnswer:
                                for y in range(len(NewPricee5)):
                                    REGD = NewPricee5[y].loc[(NewPricee5[y].жесткость == "мягкий")] 
                                    Hard5.append(REGD)
                                Test = 1
                            if hardnessList2[i] in ListAnswer:
                                for y in range(len(NewPricee5)):
                                    REGD = NewPricee5[y].loc[(NewPricee5[y].жесткость == "полусухой")] 
                                    Hard5.append(REGD)
                                Test = 1
                            if hardnessList3[i] in ListAnswer:
                                for y in range(len(NewPricee5)):
                                    REGD = NewPricee5[y].loc[(NewPricee5[y].жесткость == "сухой")] 
                                    Hard5.append(REGD)
                                Test = 1
                        
                        if Test == 1:
                            break
                        print("не могу тебя понять, Можешь объяснить подробнее, пожалуйста!?")
                if Hard5[0].empty == False:
                    print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                    for k in range(len(Hard5)):
                            print(Hard5[k])
                            print("-------------------------------------------------------------------------------------------------------------------\n")
                            print("\n")
                
                Test = 0
                while Test == 0:
                #вопрос/////////////
                        Size5 = []
                        print('Какой размер вы предпочитаете ? \n')
                        print("(Намекать: большой, средний, маленький)\n")
                        Question1 = input(' ---->>>> ')
                        Question11 = Question1.lower()
                        #ListAnswer = nltk.word_tokenize(Question11)
                        ListAnswer = Question11
                    

                        #hardnessList1 = ["мягкий", "легкий", "слабый","мяг", "лег", "сла"] #слова-синонимы
                        hardnessList1 = ["большой", "больш", "бол", "big"] #слова-синонимы
                        hardnessList2 = ["средний", "средн", "сре", "medium"]
                        hardnessList3 = ["маленький", "маленьк", "мале", "small"]

                        for i in range(0,3):
                            if hardnessList1[i] in ListAnswer:
                                for y in range(len(Hard5)):
                                    REGD = Hard5[y].loc[(Hard5[y].Размер == "большой")] 
                                    Size5.append(REGD)
                                Test = 1
                            if hardnessList2[i] in ListAnswer:
                                for y in range(len(Hard5)):
                                    REGD = Hard5[y].loc[(Hard5[y].Размер == "средний")] 
                                    Size5.append(REGD)
                                Test = 1
                            if hardnessList3[i] in ListAnswer:
                                for y in range(len(Hard5)):
                                    REGD = Hard5[y].loc[(Hard5[y].Размер == "маленький")] 
                                    Size5.append(REGD)
                                Test = 1
                        
                        if Test == 1:
                            break
                        print("не могу тебя понять, Можешь объяснить подробнее, пожалуйста!?")

                #Emp = Size5.empty()
                #if Emp == True:
                if Size5[0].empty == False:

                    print('\n\n --------------------------------- Рекомендуемые финики для вас --------------------------------------------------- \n\n')    
                    for k in range(len(Size5)):
                            print(Size5[k])
                            print("-------------------------------------------------------------------------------------------------------------------\n")
                            print("\n")
                if Size5 != ' ':
                    print('\n\n ---------------- Рекомендуемые финики для вас по выбранной вами цене -------------------------- \n\n')    
                    for k in range(len(NewPricee5)):
                            print(NewPricee5[k])
                            print("-------------------------------------------------------------------------------------------------------------------\n")
                            print("\n")

                    print("Другие варианты, возможно, вам нравятся:")
                    print("||||||||||||||||||||||||||||||||||||||||")

                    index=random.randint(0,15)

                    print('\n')
                    recommended_dates=LikeOne(dataset,dataset[index])

                    for Simi in recommended_dates:

                        print(Simi)

                        print('\n')

                

                    #второй вопрос/////////////

       
    elif Enter == 0:
        print("||||||||||||||||||")
        print("||||Good Bay||||||")
        print("||||До встречи||||")
        print("||||||||||||||||||")
        break
        
    else:

        print("//////////////////////Error !! /////////////////////////////////")
        print("Пожалуйста, введите действительные числа !!")
        print("///////////////////////////////////////////////////////////////\n")






