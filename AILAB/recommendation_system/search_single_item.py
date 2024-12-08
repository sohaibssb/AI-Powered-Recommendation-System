import random
import pandas as pd
from similarity import similarity
from similarity.metrics_by_likes import LikeOne

class SearchSingleItem:
    def __init__(self, dataset, datasetFF, datasetPrice):
        self.dataset = dataset
        self.datasetFF = datasetFF
        self.datasetPrice = datasetPrice

    def search(self, UpdateD):
        ii = 0
        ff = 49
        
        Date = UpdateD['Имя'].to_list()
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

        Input = input('Пожалуйста, выберите одну финтк из списка:\n ---->> ')

        if Input in Date:
            index = 0

            for i in range(ii, ff):
                if Date[i] == Input:
                    index = i
                    break                 
                    
            SimiData1 = {'Подобие-евклидово по Размер, Цвет, Сладость и жесткость': similarity(self.datasetFF, self.datasetFF[index], 'a')}
            SimiData2 = {'Сходство-евклидово по Цена($)/Кг': similarity(self.datasetPrice, self.datasetPrice[index], 'p')}
         
            recommended1 = pd.DataFrame(SimiData1)
            recommended2 = pd.DataFrame(SimiData2)
 
            print(recommended1)
            print(recommended2)                   

            print('\n')
            print('\n')

            print('Сходство рекомендаций по лайкам:\n')
            LikeDate = LikeOne(self.dataset, self.dataset[index])

            for Simi in LikeDate:
                print(Simi)

            print('\n')                   

        else:
            print("Другие варианты, возможно, вам понравятся:")
            index = random.randint(ii, ff)

            print('\n')
            LikeDate = LikeOne(self.dataset, self.dataset[index])

            for Simi in LikeDate:
                print(Simi)

            print('\n')
