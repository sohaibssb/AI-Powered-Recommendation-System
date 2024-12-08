import pandas as pd
from math import *
import random
import nltk
import sys
import os
from nltk.corpus import stopwords
from pprint import pprint

from data.dataset_handler import load_and_process_dataset
from similarity.euclidean import euclidean_distance, euclidean_distance2
from similarity.jaccard import jaccard_distance
from similarity.cosine import cosine_similarity, num_sim, similarity, similarity2
from similarity.metrics_by_likes import LikeOne, LikeList, DisLikeList

from recommendation_system.search_single_item import SearchSingleItem

# Load and process the dataset
datasets = load_and_process_dataset()

UpdateD = datasets["processed_data"]
data = datasets["data"] 
datasetPrice = datasets["dataset_price"]
datasetFF = datasets["dataset_ff"]
dataset = datasets["dataset_full"]
datasetCountry = datasets["dataset_country"]
df = dataset


print("\n Print all the data set - Распечатайте весь набор данных \n")
print(UpdateD)

print("///////////////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////////////")
print('                      Добро пожаловать                             ')
print('                           Финики                                  ')
print('                  Рекомендательная система                         ')
print("///////////////////////////////////////////////////////////////////\n")
while True:
  
    try:
        print("\n\t||||||||||||||||||")
        print("\t  Основной список")
        print("\t||||||||||||||||||\n")
        Enter=int(input('Пожалуйста,\n\n нажмите 1 если хотите искать по одному объекту \n\n нажмите 2 если хотите по списку лайков \n\n нажмите 3 если хотите по списку дизлайков\n\n нажмите 4 для параметрического поиска по фильтрам \n\n нажмите 5 если вы хотите умный диалог \n\n >> Для выхода нажмите 0 \n\n ---->> '))
    except ValueError:
        print("//////////////////////Error !! /////////////////////////////////")
        print("Пожалуйста, введите только цифры из списка ниже !!")
        print("///////////////////////////////////////////////////////////////\n")
        continue    
    ii =0
    ff = 49
    if Enter==1:

        SearchSingleItem.search(UpdateD)

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
                 
    elif Enter >= 6:

                print("\n\n///////////////////////////////////////////////////////////////////")
                print("///////////////////////////////////////////////////////////////////")
                print('                           Финики                                  ')
                print('                  Рекомендательная система                         ')
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

                

    elif Enter == 5:
            from sklearn import datasets
            from sklearn.cluster import KMeans
            from nltk.stem import PorterStemmer
            import re
            import nltk
            nltk.download('stopwords')
            from nltk.corpus import stopwords
            Date=UpdateD['Имя'].to_list()
            NDate1 = Date[0:15]
            NDate2 = Date[16:31]    
            NDate3 = Date[32:48] 
            NDataAll = Date[0:48]  
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
            print("\t|||||||||||||||||||||")
            print("\t диалоговая система")
            print("\t|||||||||||||||||||||\n")

            print("=======================================\tНамекать: найти, рекомендация, какие, покаже, похожий")
            print("=     ---           |||               =\t||||||||||||||||||")
            print("=   -------        |||||              =\tСладость: (слишком сладкий, сладкий, сироп, прайминги, медовый, кислый)")
            print("=  ---------      |||||||             =\t-----------------------------------------------------------------------")
            print("=  ---------     |||||||||            =\tСтрана: (Саудовская Аравия, Иран, Эмирейтс)")
            print("=   -------     |||||||||||      '    =\t-----------------------------------------------------------------------")
            print("=    ------      |||||||||      '''   =\tжесткость: (мягкий, полусухой, сухой)")
            print("=      ---         |||||       '''''' =\t-----------------------------------------------------------------------")
            print("=                   |||         ''''  =\tЦвет: (темно коричневый, коричневый, желтый, черный)")
            print("=                                ''   =\t-----------------------------------------------------------------------")
            print("=======================================\tРазмер: (большой, средний, маленький)")
            print("        =======================        \t-----------------------------------------------------------------------")
            print("          ===================          \tРегион: (Медина, Джидда, Эр-Рияд, Касим, Хардж, Гормозган, Хузестан,")
            print("            ===============            \tБушехер, Керман, Систан, Фарс, Аль-Айн, Лива, Абу-Даби)")
            print("            ===============            \t-----------------------------------------------------------------------")
            print("            ===============            \tЦена: (дорого, средний, недорогой)")
            print("              ===========              \t-----------------------------------------------------------------------\n")
            print("\n---------------------------------------------")
            print('Объясните, что вы хотите, простыми словами ?')
            print("---------------------------------------------\n")
            print(">> Для перехода в главное меню >> написать 'выход' \n")
        
            Dataset5 = data
            Test=0
            ex22 = 0
            exit7 = 0 #for Test77
            priceTest = 0 #for price number,, the last function
            while Test == 0:
                        
                        if ex22 == 1:
                            break
                        while Test == 0:            
                                    Dataset5 = data
                                    Question2 = input(' ---->>>> ')
                                    exx = 1
                                    exit = 0
                                    Ee = 1
                                    Ee1 = ["выход","выхо","выйти","выйт","exit"]
                                    exxx = 0
                                    for ii in range(0,5):
                                        if Ee1[ii] in Question2:
                                                Ee=0
                                                exit = 1
                                                print(">> До встречи <<")
                                                exxx = 1
                                                ex22 = 1
                                                break
                                    if exxx == 1:
                                        break

                                    #Apllying NLP Techniques - natural language processing
                                    Question22 = Question2.lower()
                                    pricenum = nltk.word_tokenize(Question22)
                                    result = re.sub(r'[^А-Яа-я ]', '', Question22)
                                    words = nltk.word_tokenize(result)
                                    filtered_words = [word for word in words if word.lower() not in stopwords.words('russian')]
                                    stemmer = PorterStemmer()
                                    stemmed_words = [stemmer.stem(word) for word in filtered_words]
                                    UserQ = " ".join(stemmed_words)
                                    #Greeting
                                    Greet = 0
                                    Question00 = ["привет","прив","здравству","здоро́в","чао!"]

                                    for i in range(0,5):
                                        if Question00[i] in UserQ:
                                            print("добро пожаловать!")
                                            Greet = 1
                                            
                                            break
                                    #Question List
                                    Question0 = ["финик","фник", "финиковый","фрукт", "фиников","фини", "финики", "финико", "date"]
                                    Question1 = ["найти", "найди","най", "выбери","выб", "выбрат", "докажи", "докаж", "рекомендац", "как", "какие", "покаже","пакаж","покаж","показат","показ","вид","рекоменд","хочу","хотет","нуж"] 
                                    Question2 = ["сладкий", "сладк", "сладк", "сладк", " "]
                                    Question3 = ["сладкий", "сладк", "конфе", "конф"]
                                    Question4 = ["сироп", "сиро", "сиропы", "сир"]
                                    Question5 = ["прайминги", "прайминг", "грунтовки", "грунтов"]
                                    Question6 = ["медовый", "мед", "мёд", "медо"]
                                    Question7 = ["похожий","похож", "схож","сходн","подобн","равн","одинаков","similar"]
                                    Question8 = ["не","нет","no","not"]

                                    #Answer List
                                    #Сладость
                                    AnsCL1 = ["слишком", "слишк", "слишко", "очен", "very"]
                                    AnsCL2 = ["сладкий", "сладк", "сладк", "сладк", "sweet"]
                                    AnsCL3 = ["сироп", "сиро", "сиропы", "сир", "syrup"]
                                    AnsCL4 = ["прайминги", "прайминг", "грунтовки", "грунтов", "priming"]
                                    AnsCL5 = ["медовый", "мед", "мёд", "медо", "honey"]
                                    AnsCL6 = ["кислый", "кисл", "прокисший", "прокисш", "sour"]
                                    #Страна
                                    AnsC1 = ["саудовская", "саудовскаяаравия", "саудовск", "арави", "saudi"]
                                    AnsC2 = ["иран", "ира", "иран", "iran", "eran"]
                                    AnsC3 = ["эмирейтс", "эмирей", "эмирейт", "арави", "emirates"]
                                    AnsC11 = ["страны", "стран","странах"]
                                    AnsC22 = ["растут", "рас","расти"]
                                    #жесткость
                                    AnsX1 = ["мягкий", "мягк", "легкий", "легк", "soft"]
                                    AnsX2 = ["полусухой", "полусух", "полу", "semi-dry", "semi"]
                                    AnsX3 = ["сухой", "сухо", "сушит", "сухие", "dry"]
                                    #Цвет
                                    AnsT1 = ["темно", "темнокоричневый", "темн", "dark", "darkbrown"]
                                    AnsT2 = ["коричневый", "коричне", "карий", "brown", "brow"]
                                    AnsT3 = ["желтый", "желт", "мед", "yellow", "yello"]
                                    AnsT4 = ["черный", "черн", "темный", "темн", "black"]
                                    #Размер
                                    AnsS1 = ["большой", "больш", "крупн", "широк", "larg"]
                                    AnsS2 = ["средний", "средн", "нормальн", "небольш", "medium"]
                                    AnsS3 = ["маленьк", "мал", "small", "небольш", "little"]
                                    #Регион
                                    AnsR1 = ["Медина", "Джидда", "Эр-Рияд", "Касим", "Хардж","Гормозган", "Хузестан", "Бушехер", "Керман", "Фарс","Аль-Айн", "Лива", "Абу Даби"]
                                    #######
                                    AnsR = [["медина", "медин", "medina", "madin"],["джидда", "джид", "jeddah", "jiddah"],["эр-рияд", "эррияд", "эр-рия", "riyadh"],["касим", "каси", "qasi", "qasim"],["хардж", "хард", "hardge", "kharge"],["гормозган", "гормозг", "горм", "gormozgan"],["хузестан", "хузест", "khuzestan", "khuzest"],["бушехер", "бушех", "busheher", "bush"],["керман", "керм", "kerman", "kerm"],["систан", "сист", "sistan", "sist"],["фарс", "фар", "farce", "farec"],["аль-айн", "альайн", "аль", "ain"],["лива", "лив", "liva", "leva"],["абу-даби", "абу", "abu", "abudhabi"]]
                                    #Цена
                                    priceL = ["цена","цен","стоимос","price"]
                                    AnsP1 = ["дорого","дорог","expensive","пышн"]
                                    AnsP2 = ["средний","средн","нормальн","регулярн"]
                                    AnsP3 = ["недорогой","недорог","дешевый","дешев"]
                                    exit7 = 0 #for Test77 
                                    TTa = 0
                                    TTb = 0
                                    Test7 = 0
                                    net = 0
                                    for i in range(0,9):
                                        if Question0[i] in UserQ:
                                            Test = 1
                                            Greet = 0
                                            break
                                    for i in range(0,20):
                                        if Question1[i] in UserQ and Test == 1:
                                            Test = 11
                                            break
                                    for i in range(0,3):
                                        if AnsC11[i] in UserQ:
                                            TTa = 222
                                            break
                                    for i in range(0,3):
                                        if AnsC22[i] in UserQ:
                                            TTb = 223
                                            break
                                    if TTa == 222 and (Test == 1 or Test == 11) and TTb == 223:
                                            Test = 22
                                    for i in range(0,3):
                                            if priceL[i] in UserQ:
                                                Test = 33
                                    for i in range(0,8):
                                        if Question7[i] in UserQ and (Test == 1 or Test == 11):
                                            Test = 11
                                            Test7 = 77
                                            break
                                    for i in range(0,4):
                                        if Question8[i] in result:
                                            net = 1
                                            break

                                    if Test == 11:
                                        for j in range(0,5): 
                                                if AnsCL1[j] in UserQ and AnsCL2[j] in UserQ:
                                                    filtered_df = Dataset5.query("Сладость == 'слишком сладкий' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsCL2[j] in UserQ:
                                                    filtered_df = Dataset5.query("Сладость == 'сладкий' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsCL3[j] in UserQ:
                                                    filtered_df = Dataset5.query("Сладость == 'сироп' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsCL4[j] in UserQ:
                                                    filtered_df = Dataset5.query("Сладость == 'прайминги' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsCL5[j] in UserQ:
                                                    filtered_df = Dataset5.query("Сладость == 'медовый' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsCL6[j] in UserQ:
                                                    filtered_df = Dataset5.query("Сладость == 'кислый' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsC1[j] in UserQ:
                                                    filtered_df = Dataset5.query("Страна == 'Саудовская Аравия' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsC2[j] in UserQ:
                                                    filtered_df = Dataset5.query("Страна == 'Иран' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsC3[j] in UserQ:
                                                    filtered_df = Dataset5.query("Страна == 'Эмирейтс' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsX1[j] in UserQ:
                                                    filtered_df = Dataset5.query("жесткость == 'мягкий' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsX2[j] in UserQ:
                                                    filtered_df = Dataset5.query("жесткость == 'полусухой' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsX3[j] in UserQ:
                                                    filtered_df = Dataset5.query("жесткость == 'сухой' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsT1[j] in UserQ:
                                                    filtered_df = Dataset5.query("Цвет == 'темно коричневый' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsT2[j] in UserQ:
                                                    filtered_df = Dataset5.query("Цвет == 'коричневый' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsT3[j] in UserQ:
                                                    filtered_df = Dataset5.query("Цвет == 'желтый' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsT4[j] in UserQ:
                                                    filtered_df = Dataset5.query("Цвет == 'черный' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsS1[j] in UserQ:
                                                    filtered_df = Dataset5.query("Размер == 'большой' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsS2[j] in UserQ:
                                                    filtered_df = Dataset5.query("Размер == 'средний' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,5): 
                                                if AnsS3[j] in UserQ:
                                                    filtered_df = Dataset5.query("Размер == 'маленький' ")
                                                    Dataset5 = filtered_df
                                        for j in range(0,13): 
                                            for k in range(0,4):
                                                if AnsR[j][k] in UserQ:
                                                    category = "Регион"
                                                    rr = AnsR1[j]
                                                    query = f"Регион == '{rr}'"
                                                    filtered_df = Dataset5.query(query)
                                                    Dataset5 = filtered_df
                                        for j in range(0,4): 
                                                if AnsP1[j] in UserQ:
                                                    query = "Цена >= 30"
                                                    filtered_df = df.query(query)
                                                    Dataset5 = filtered_df
                                        for j in range(0,4): 
                                                if AnsP3[j] in UserQ:
                                                    query = "Цена < 10"
                                                    filtered_df = df.query(query)
                                                    Dataset5 = filtered_df
                                                    net = 0
                                                    break
                                            
                                    if Test7 == 77:
                                        exit7 = 0
                                        co=1
                                        for j in range(len(NDataAll)): 
                                            for k in range(len(pricenum)):
                                                if NDataAll[j] in pricenum[k] and exit7 == 0:
                                                    ans77 = pricenum[k]
                                                    index=0;
                                                    for i in range(ii,ff):
                                                        if Date[i]==ans77:
                                                            index=i
                                                            break
                                                    Name=UpdateD['Имя'].to_list()
                                                    ListDates = []
                                                    LikeList11 = []
                                                    ListOfNames = ans77
                                                    ListDates.append(ListOfNames)                                       
                                                    LLN=[Name1 for Name1 in ListDates if Name1 in Name]
                                                    dataset_tests=[[UpdateD['Имя'][i],UpdateD['Цена'][i], UpdateD['Страна'][i],UpdateD['Регион'][i], UpdateD['Размер'][i],UpdateD['Цвет'][i],UpdateD['Сладость'][i],UpdateD['жесткость'][i]] for i in range(ii,ff) if UpdateD['Имя'][i] in LLN]
                                                    LikeList11=LikeList(dataset,dataset_tests)
                                                    print("\n")
                                                    print(f'Финики похожий на {ans77}:')
                                                    print("\n")
                                                    for Simi in LikeList11:
                                                            print(f'\t{co}- {Simi}\n')
                                                            co =1+co
                                                            exit7 = 1
                                                            Test = 0
                                                    print('\n')
                                                    #LikeList = []
                                                    break
                                    if Test == 22:
                                        print("\n") 
                                        print("Финики в основном выращивают в странах, расположенных в теплых,") 
                                        print("засушливых регионах с долгим летом и малым количеством осадков.")
                                        print("К основным странам, где выращивают финики, относятся:\n")
                                        print("Египет, Иран, Саудовская Аравия, Ирак, Объединенные Арабские Эмираты,\nАлжир, Тунис,Оман, Пакистан, Калифорния, США.")
                                        print("Вышеперечисленные страны являются основными производителями фиников,")
                                        print(" но в нашей системе рекомендаций мы сосредоточимся только на трех странах:\n")
                                        print("1- Саудовская Аравия")
                                        print("2- Иран")
                                        print("3- Эмираты")
                                        print("\n")
                                        exx = 0
                                        Test = 0
                                        break
                   
                                    if Test == 33:
                                            for j in range(0,4): 
                                                if AnsP1[j] in UserQ:
                                                    query = "Цена >= 30"
                                                    filtered_df = df.query(query)
                                                    Dataset5 = filtered_df
                                            for j in range(0,4): 
                                                if AnsP2[j] in UserQ:
                                                    query = "Цена < 30 and Цена >= 10 "
                                                    filtered_df = df.query(query)
                                                    Dataset5 = filtered_df
                                            for j in range(0,4): 
                                                if AnsP3[j] in UserQ:
                                                    query = "Цена < 10 "
                                                    filtered_df = df.query(query)
                                                    Dataset5 = filtered_df
                                                    net = 0
                                            #Last Function for Price by Number
                                            rr1 = list(range(30,46))
                                            strings = [str(x) for x in rr1] 
                                            for k in range(len(strings)):
                                                    for kk in range(len(pricenum)):
                                                            if strings[k] in pricenum[kk]:
                                                                UpdatePr = int(pricenum[kk])
                                                                if UpdatePr >= 30:
                                                                    query = "Цена >= 30"
                                                                    filtered_df = df.query(query)
                                                                    Dataset5 = filtered_df
                                                                    priceTest = 1
                                                                    break
                                            rr1 = list(range(10,30))
                                            strings = [str(x) for x in rr1] 
                                            for k in range(len(strings)):
                                                    for kk in range(len(pricenum)):
                                                            if strings[k] in pricenum[kk]:
                                                                UpdatePr = int(pricenum[kk])
                                                                if UpdatePr < 30 and UpdatePr >= 10:
                                                                    query = "Цена < 30 and Цена >= 10 "
                                                                    filtered_df = df.query(query)
                                                                    Dataset5 = filtered_df
                                                                    priceTest = 1
                                                                    break
                                            rr1 = list(range(1,10))
                                            strings = [str(x) for x in rr1] 
                                            for k in range(len(strings)):
                                                    for kk in range(len(pricenum)):
                                                            if strings[k] in pricenum[kk]:
                                                                UpdatePr = int(pricenum[kk])
                                                                if UpdatePr < 10:
                                                                    query = "Цена < 10"
                                                                    filtered_df = df.query(query)
                                                                    Dataset5 = filtered_df
                                                                    priceTest = 1
                                                                    break
                                    if len(Dataset5) == 49 and Greet == 0 and exit7 != 1:

                                        print("\nИзвините, я вас не понимаю, пожалуйста, объясните подробнее !!\n")
                                        Test = 0                             

                                    elif Test == 1 or Test == 11 or Test == 22 or Ee == 0 or Test == 33 or Test == 77:
                                            break
                                    elif Greet != 1 and exit7 != 1:

                                        print("не могу тебя понять, Можешь объяснить подробнее, пожалуйста !?")
                                        print("эта система рекомендаций только для финики !! \n")
                                        print("=============================================\n")
                                    elif exit7 == 1:
                                        break

                        if exx == 1 and exit7 == 0:  
                                        if exit == 1:
                                            break 
                                        if net == 1:
                                                lis = Dataset5['No.'].to_list()
                                                lisU = [x - 1 for x in lis]
                                                dataFrameNet = data.drop(lisU)
                                                print('\n Рекомендуемые финики для вас: \n')    
                                                print(dataFrameNet)
                                                Test = 0
                                                print("\n---------------------------------------------------------------------------------------------------------\n")
                                        elif len(Dataset5) != 49 and priceTest == 0:
                                                print('\n Рекомендуемые финики для вас:\n')    
                                                print(Dataset5)
                                                print("\n---------------------------------------------------------------------------------------------------------\n")
                                                Test = 0
                                        elif priceTest == 1:
                                                print('\n Рекомендуемые финики для вас:') 
                                                print('\n "Тот же ценовой диапазон"\n')    
                                                print(Dataset5)
                                                print("\n---------------------------------------------------------------------------------------------------------\n")
                                                Test = 0
                                                priceTest == 1
                                        elif len(Dataset5) != 49 and Greet != 1:
                                            Test = 0
                                            print('\n ------ Другие варианты, возможно, вам нравятся:------\n')    
                                                                
                                            print("\t\t||||||||||||")

                                            index=random.randint(0,15)

                                            recommended_dates=LikeOne(dataset,dataset[index])
                                            i=1
                                            for Simi in recommended_dates:
                                                #print(Simi)
                                                print(f'\t\t{i}: {Simi}')
                                                i =1+i
                                            print("\t\t||||||||||||\n")
                        if Test == 0:
                             print("\n---------------------------------------------")
                             print("Если вы хотите что-то еще, пожалуйста")
                             print('Объясните, что вы хотите, простыми словами ?')
                             print("---------------------------------------------\n")
                             print(">> Для перехода в главное меню >> написать 'выход' \n")
                             continue

       
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






