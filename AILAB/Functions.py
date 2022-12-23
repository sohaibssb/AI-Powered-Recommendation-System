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




#“не найдено точного соответствия, однако, возможно, Вам понравится”

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
    print(LL)

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
    print(LL)

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


datasetPrice=[[UpdateD['Имя'][i],UpdateD['Цена($)/Кг'][i]] for i in range(0,49)]

datasetFF=[[UpdateD['Имя'][i],UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i], UpdateD['жесткость/влажность'][i]] for i in range(0,49)]

dataset=[[UpdateD['Имя'][i],UpdateD['Цена($)/Кг'][i],UpdateD['Страна'][i],UpdateD['Регион'][i],UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i], UpdateD['жесткость/влажность'][i]] for i in range(0,49)]

datasetCountry=[[UpdateD['Имя'][i],UpdateD['Страна'][i]] for i in range(0,49)]


print("///////////////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////////////")
print('                      Добро пожаловать                             ')
print('                           Финики                                  ')
print('                  Рекомендательная система                         ')
print("///////////////////////////////////////////////////////////////////\n")
while True:
  
    try:
        Enter=int(input('Пожалуйста,\n\n нажмите 1 если хотите искать по одному объекту \n\n нажмите 2 если хотите по списку лайков \n\n нажмите 3 если хотите по списку дизлайков\n\n нажмите 4 если вы хотите умный диалог \n\n Для выхода нажмите 0 \n\n ---->> '))
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
                    
                    print(UpdateD)
                    SimiData1={'Подобие-евклидово по Размер, Цвет, Сладость и жесткость/влажность':similarity(datasetFF, datasetFF[index],'a')}
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
                
                    print("<<Пожалуйста, введите финик, которая вам нравится>>")

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

                        
                    dataset_tests=[[UpdateD['Имя'][i],UpdateD['Цена($)/Кг'][i], UpdateD['Страна'][i],UpdateD['Регион'][i], UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i],UpdateD['жесткость/влажность'][i]] for i in range(ii,ff) if UpdateD['Имя'][i] in LLN]

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
                
                    print("<<Пожалуйста, введите финик, которая вам не нравится>>")

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

                

                    dataset_tests=dataset_tests=[[UpdateD['Имя'][i],UpdateD['Цена($)/Кг'][i], UpdateD['Страна'][i],UpdateD['Регион'][i], UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i],UpdateD['жесткость/влажность'][i]] for i in range(ii,ff) if UpdateD['Имя'][i] in LLN]

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
        print('             Рекомендательная система - Фильтр                     ')
        print("///////////////////////////////////////////////////////////////////\n")
      
        LikeList = []
        DisLikeList = []
        LikeList2 = []
        DisLikeList2 = []
        datasetLike2=pd.DataFrame(columns=['Имя','Цена($)/Кг','Страна','Регион','Размер','Цвет','Сладость','жесткость/влажность'], index=range(0, 49))
        
        #вопрос - Country /////////////

        Questioni = input('Вы хотите финики из конкретной страны или из любого места (Да или нет)? >>')
        Questionii = Questioni.lower()
        Optioni = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
        Optionii = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
        flag = 0 
        for i in range(0,10):
                if Optioni[i] in Questionii:
                    flag = 1    
                elif Optionii[i] in Questionii:
                    flag = 2

        if flag == 1:

        #вопрос/////////////
            Question4 = input('Вам нравится, что это из Саудовской Аравии? >> ')

            Question44 = Question4.lower()

            Option1 = ["да", "согласие", "саудовск","важно","yes", "соглас", "саудов","важн", "da","важ"] 
            Option2 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","безразницы"]

            for i in range(0,10):
                if Option1[i] in Question44:                 
                    newDataF = UpdateD.loc[(UpdateD.Страна == 1)]
                    LikeList.append(newDataF)
                    newDataF2 = data.loc[(data.Страна == "Саудовская Аравия")] 
                    datasetLike2.append(newDataF2)
                elif Option2[i] in Question44:
                    newDataF = UpdateD.loc[(UpdateD.Страна == 1)]
                    newDataF2 = data.loc[(data.Страна == "Саудовская Аравия")]
                    DisLikeList2.append(newDataF2)
                    DisLikeList.append(newDataF)
                   
        #вопрос/////////////
            Question5 = input('Вам нравится, что это из Иран? >>')

            Question55 = Question5.lower()

            Option11 = ["да", "согласие", "Иран","важно","yep", "согл", "y","важн", "da","важ"] 
            Option22 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","безразницы"]

            for i in range(0,10):
                if Option11[i] in Question55:
                    newDataF = UpdateD.loc[(UpdateD.Страна == 0)]
                    newDataF2 = data.loc[(data.Страна == "Иран")] 
                    datasetLike2.append(newDataF2)
                    LikeList.append(newDataF)
                elif Option22[i] in Question55:
                    newDataF = UpdateD.loc[(UpdateD.Страна == 0)]
                    newDataF2 = data.loc[(data.Страна == "Иран")]
                    DisLikeList2.append(newDataF2)
                    DisLikeList.append(newDataF)
        #вопрос/////////////
            Question6 = input('Вам нравится, что это из Эмирейтс? >>')

            Question66 = Question6.lower()

            Option111 = ["да", "согласие", "Эмирейтс","важно","yep", "согл", "y","важн", "da","важ"] 
            Option222 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]

            for i in range(0,10):
                if Option111[i] in Question66:
                    newDataF = UpdateD.loc[(UpdateD.Страна == 2)]
                    LikeList.append(newDataF)
                    newDataF2 = data.loc[(data.Страна == "Эмирейтс")] 
                    datasetLike2.append(newDataF2)
                elif Option222[i] in Question66:
                    newDataF = UpdateD.loc[(UpdateD.Страна == 2)]
                    newDataF2 = data.loc[(data.Страна == "Эмирейтс")]
                    DisLikeList2.append(newDataF2)
                    DisLikeList.append(newDataF)

        #вопрос - Region /////////////
            
            Question2  = input('Вы хотите искать по региону страны? (Да или нет)? >>')
          
            Questioni2 = Question2.lower()
            Optioni2 = ["да", "согласие", "yes","важно","yep", "согл", "y","важн", "da","важ"] 
            Optionii2 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
            flag = 0 
            for i in range(0,10):
                    if Optioni[i] in Questionii:
                        flag = 1    
                    elif Optionii[i] in Questionii:
                        flag = 2

            if flag == 1:

            #вопрос/////////////
                RegionData=datasetLike2['Регион'].to_list()
                RD = list(dict.fromkeys(RegionData))
                print(RD)
                print("Пожалуйста, выберите регионы из списка ниже: \n ")
                j=1
                for i in range(len(RD)):
                   
                   print(f"Регион#{+j}")
                   print(RD[i])
                   print("\n")
                   j=j+1

                Questioni2 = input(' \n---->')

                Question44 = Questioni2.lower()

                Option1 = ["да", "согласие", "саудовск","важно","yes", "соглас", "саудов","важн", "da","важ"] 
                Option2 = ["нет", "не", "no","не важно", "неважно","безразли","безразлично","без различно","без разницы","безразницы"]

                for i in range(0,10):
                    if Option1[i] in Question44:                 
                        newDataF = UpdateD.loc[(UpdateD.Страна == 1)]
                        LikeList.append(newDataF)
                    else:
                        continue
                       
           


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

        #Третий вопрос/////////////Price//////
        '''
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
        '''
        #Третий вопрос///////

        Test = 0
        while Test == 0:

            Question4 = input('Вам нравится, чтобы он был большим или средним?\n')

            if Question4 == 1:
                LikeList.append("недорогой")
                Test = 1
            elif Question4 == 2:
                LikeList.append("средний") 
                Test = 1
            elif Question4 == 3:
                LikeList.append("дорогой")
                Test = 1

            if Test == 1:
                break 

            print("пожалуйста, введите правильный ввод!!")   

    elif Enter == 5:

    #/////////////////////////////////////////////////////////////////////////
    #///////////////Recomindation System//////////////////////////////////////
    #/////////////////////////////////////////////////////////////////////////


        print("///////////////////////////////////////////////////////////////////")
        print("///////////////////////////////////////////////////////////////////")
        print('                           Финики                                  ')
        print('                  Рекомендательная система                         ')
        print("///////////////////////////////////////////////////////////////////\n")
        print("не могли бы вы сказать мне, пожалуйста, как вам нравятся финики ")
        print("и что вам не нравится на финики \n")

        LikeList = []
        DisLikeList = []

        #вопрос/////////////

        Questioni = input('Вы хотите финики из конкретной страны или из любого места (Да или нет)? >>')
        Questionii = Questioni.lower()
        Optioni = ["да", "согласие", "yes","важно"] 
        Optionii = ["нет", "не", "No","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]
        flag = 0 
        for i in range(0,3):
                if Optioni[i] in Questionii:
                    flag = 1    
                elif Optionii[i] in Questionii:
                    flag = 2

        if flag == 1:

        #вопрос/////////////
            Question4 = input('Вам нравится, что это из Саудовской Аравии? >>')

            Question44 = Question4.lower()

            Option1 = ["да", "согласие", "саудовск","важно"] 
            Option2 = ["нет", "не", "No","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]

            for i in range(0,3):
                if Option1[i] in Question44:
                    LikeList.append("Саудовской Аравии")
                elif Option2[i] in Question44:
                    DisLikeList.append("Саудовской Аравии")
        #вопрос/////////////
            Question5 = input('Вам нравится, что это из Иран? >>')

            Question55 = Question5.lower()

            Option11 = ["да", "согласие", "Иран","важно"] 
            Option22 = ["нет", "не", "No","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]

            for i in range(0,3):
                if Option11[i] in Question55:
                    LikeList.append("Иран")
                elif Option22[i] in Question55:
                    DisLikeList.append("Иран")
        #вопрос/////////////
            Question6 = input('Вам нравится, что это из Эмирейтс? >>')

            Question66 = Question6.lower()

            Option111 = ["да", "согласие", "Эмирейтс","важно"] 
            Option222 = ["нет", "не", "No","не важно", "неважно","безразли","безразлично","без различно","без разницы","без разницы"]

            for i in range(0,3):
                if Option111[i] in Question66:
                    LikeList.append("Эмирейтс")
                elif Option222[i] in Question66:
                    DisLikeList.append("Эмирейтс")

        #Первый вопрос/////////////
        Test = 0
        while Test == 0:

            Question1 = input('Какие финики самое мягкий или полусухой или сухой? >>')

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

        #Третий вопрос/////////////Price//////
        '''
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
        '''
        #Третий вопрос///////

        Test = 0
        while Test == 0:

            Question4 = input('Вам нравится, чтобы он был большим или средним?\n')

            if Question4 == 1:
                LikeList.append("недорогой")
                Test = 1
            elif Question4 == 2:
                LikeList.append("средний") 
                Test = 1
            elif Question4 == 3:
                LikeList.append("дорогой")
                Test = 1

            if Test == 1:
                break 

            print("пожалуйста, введите правильный ввод!!")

       
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

    #print("пожалуйста, введите правильный ввод!!")
'''
'''
print(LikeList)
print(DisLikeList)
 

ii = 0
ff = 0
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
                        ii=0
                        ff=49
           
if flag == 1:

#вопрос/////////////
        Question4 = input('Вам нравится, что это из Саудовской Аравии?\n')

        Question44 = Question4.lower()

        Option1 = ["да", "согласие", "саудовск"] 
        Option2 = ["нет", "не", "No"]

        for i in range(0,3):
            if Option1[i] in Question44:
                ii=0
                ff=21
            
                
#вопрос/////////////
        Question5 = input('Вам нравится, что это из Иран?\n')

        Question55 = Question5.lower()

        Option11 = ["да", "согласие", "Иран"] 
        Option22 = ["нет", "не", "No"]

        for i in range(0,3):
            if Option11[i] in Question55:
                if ff == 21:
                    ii=0
                    ff=36
                else:
                    ii=21
                    ff=36
#вопрос/////////////
        Question6 = input('Вам нравится, что это из Эмирейтс?\n')

        Question66 = Question6.lower()

        Option111 = ["да", "согласие", "Эмирейтс"] 
        Option222 = ["нет", "не", "No"]

        for i in range(0,3):
            if Option111[i] in Question66:
                if ii == 0 and ff == 36:
                    ii=0
                    ff=49
                elif ii==21:
                    ii=21
                    ff=49
                else:
                    ii=36
                    ff=49

        Name=UpdateD['Имя'].to_list()
        print(data.iloc[ii,ff])





'''


'''
for i in range(0,2):
    for j in range(0,4):
        if LikeList[4] == data.iloc[0,8]:
           print(i)
           print("good")



ii =0
ff = 49
        
Enter=int(input('Пожалуйста,\n нажмите 1 если хотите искать по одному объекту \n нажмите 2 если хотите по списку лайков \n нажмите 3 если хотите по списку дизлайков\n'))

if Enter==1:

            Date=UpdateD['Имя'].to_list()

            Input=input('\n Пожалуйста, выберите одну финтк из списка:\n')

            print(data.iloc[ii,ff])
            print("\n")

            ResultsNum=int(input('введите количество собак, похожих на ту, которую вы хотите увидеть\n'))

            if Input in Date:

                index=0;

                for i in range(ii,ff):

                    if Date[i]==Input:

                        index=i

                        break

                GetData={'Similarity-euclidean':similarity(datasetPrice, datasetPrice[index], ResultsNum,'e'),'Price Similarity-jaccard':similarity(datasetFF, datasetFF[index], ResultsNum,'j')}

                recommended=pd.DataFrame(GetData)

                print('\n')

                print(recommended)

                print('\n')

                print('neighboors after the combination of the three proximity measure using the formula of the magnitude of a 3D vector\n')

                recommended_dates=LikeOne(dataset,dataset[index],ResultsNum)

                for Simi in recommended_dates:

                    print(Simi)

                print('\n')

            else:

                print("no exact match found, but maybe you will like it")

                index=random.randint(ii,ff)

                print('\n')

                recommended_dates=LikeOne(dataset,dataset[index],ResultsNum)

                for Simi in recommended_dates:

                    print(Simi)

                print('\n')

elif Enter==2:

            Name=UpdateD['Имя'].to_list()

            print()

            print(Name)

            print()

            list_names=input('пожалуйста, введите таблицу названий пород собак, которые вам нравятся, разделите запятой\n')

            list_names=list_names.split(',')

            LLN=[Name1 for Name1 in list_names if Name1 in Name]

            if not LLN:

                print("no exact match found, but maybe you will like it")

                index=random.randint(0,25)

                print('\n')

                recommended_dates=LikeOne(dataset,dataset[index],ResultsNum)

                for Simi in recommended_dates:

                    print(Simi)

                print('\n')

            else:

                print('\nthese are the name of dog breeds that we found:')

                print(LLN)

                print()
                       
                dataset_tests=[[UpdateD['Имя'][i],UpdateD['Цена($)/Кг'][i],UpdateD['Страна'][i],UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i],UpdateD['жесткость/влажность'][i]] for i in range(ii,ff) if UpdateD['Имя'][i] in LLN]

                print('\n the n breeds of dogs recommended according to your table of dogs that you like\n')

                LikeList=LikeList(dataset,dataset_tests,5)

                print()

                for Simi in LikeList:

                    print(Simi)

elif Enter==3:

            Name=UpdateD['Имя'].to_list()

            print()

            print(Name)

            print()

            ListNames=input('пожалуйста, введите таблицу названий пород собак, которые вам нравятся, разделите запятой\n')

            ListNames=ListNames.split(',')

            LLN=[Name1 for Name1 in ListNames if Name1 in Name]

            if not LLN:

                print("no exact match found, but maybe you will like it")

                index=random.randint(ii,ff)

                print('\n')

                DateRecom=LikeOne(dataset,dataset[index],ResultsNum)

                for Simi in DateRecom:

                    print(Simi)

                print('\n')

            else:

                print('\nthese are the name of dog breeds that we found:')

                print(LLN)

                print()
               

                dataset_tests=[[UpdateD['Имя'][i],UpdateD['Цена($)/Кг'][i],UpdateD['Страна'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i],UpdateD['жесткость/влажность'][i]] for i in range(ii,ff) if UpdateD['Имя'][i] in ListNames]

                print('\n the n breeds of dogs recommended according to your table of dogs that you do not like\n')

                DisLikeRecom=DisLikeList(dataset,dataset_tests,5)

                print()

                for Simi in DisLikeRecom:

                    print(Simi)       

'''

