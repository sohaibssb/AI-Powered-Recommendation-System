from pandas_ods_reader import read_ods
import pandas as pd


import seaborn as sn
import matplotlib.pyplot as plt


base_path = "/home/sohiab/IntelligentLab1/AILab1DataSet.ods"
sheet_index = 1

data = read_ods(base_path, 1, columns=["No.","Имя", "Цена($)/Кг","Страна","Регион","Размер","Цвет","Сладость","жесткость/влажность"])

dff = pd.DataFrame(data,columns=["No.","Имя", "Цена($)/Кг","Страна","Регион","Размер","Цвет","Сладость","жесткость/влажность"])

'''
import os
import pandas as pd
import numpy as np
import seaborn as sn


# Loading the dataset
BIKE = read_ods(base_path, 1, columns=["No.","Имя", "Цена($)/Кг","Страна","Регион","Размер","Цвет","Сладость","жесткость/влажность"])

# Numeric columns of the dataset
numeric_col = ["No.", "Цена($)/Кг"]

# Correlation Matrix formation
corr_matrix = BIKE.loc[:,numeric_col].corr()
print(corr_matrix)

#Using heatmap to visualize the correlation matrix
sn.heatmap(corr_matrix, annot=True)

df11 = pd.DataFrame(data,columns=["No.", "Цена($)/Кг"])
corr = df11.corr()
corr.style.background_gradient(cmap='RdYlGn')
'''



'''///////////////////////////////////////////////////////////////////////////////////////'''


AnB = 0;
AUB = 16;

itemsi = range(0,49);
itemsiv = range(1,49);
itemsj = [1,2,3,4,5,6,7,8];

similarity = []
similarityDis = []
for i in itemsi:
    for iv in itemsiv:
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
            
         
         

print(similarity)  
print(" ")
print(similarityDis) 
print(data)
#матрица корреляции 1:
   
df1 = pd.DataFrame(similarity)

corr_matrix = df1.corr()
sn.heatmap(corr_matrix, annot=True)
plt.show()

#матрица корреляции 2:
   
df2 = pd.DataFrame(similarityDis)

corr_matrix = df2.corr()
sn.heatmap(corr_matrix, annot=True)
plt.show()

#матрица корреляции - For Data:
df3 = pd.DataFrame(data)

corr_matrix = df3.corr()
sn.heatmap(corr_matrix, annot=True)
plt.show()


       



        
    
    



'''

if (data.iloc[0,1] == data.iloc[1,1]) is not True:
    AnB +=1
if (data.iloc[0,2] == data.iloc[1,2]) is not True:
    AnB +=1
if (data.iloc[0,3] == data.iloc[1,3]) is not True:
    AnB +=1
if (data.iloc[0,4] == data.iloc[1,4]) is not True:
    AnB +=1
if (data.iloc[0,5] == data.iloc[1,5]) is not True:
    AnB +=1
if (data.iloc[0,6] == data.iloc[1,6]) is not True:
    AnB +=1
if (data.iloc[0,7] == data.iloc[1,7]) is not True:
    AnB +=1
if (data.iloc[0,8] == data.iloc[1,8]) is not True:
    AnB +=1 


print(AnB)

def jaccard_similarity(AnB, AUB):
    #Find intersection of two sets
    nominator = AnB

    #Find union of two sets
    denominator = AUB

    #Take the ratio of sizes
    similarity = nominator/denominator
    
    return similarity

similarity = jaccard_similarity(AnB, AUB)

print(similarity)

'''


'''
if (data.loc[0,["Имя"]] == data.loc[1,["Имя"]]) is not True:
    AnB +=1
if (data.loc[0,["Цена($)/Кг"]] == data.loc[1,["Цена($)/Кг"]]) is not True:
    AnB +=1
if (data.loc[0,["Страна"]] == data.loc[1,["Страна"]]) is not True:
    AnB +=1
if (data.loc[0,["Регион"]] == data.loc[1,["Регион"]]) is not True:
    AnB +=1
if (data.loc[0,["Размер"]] == data.loc[1,["Размер"]]) is not True:
    AnB +=1
if (data.loc[0,["Цвет"]] == data.loc[1,["Цвет"]]) is not True:
    AnB +=1
if (data.loc[0,["Сладость"]] == data.loc[1,["Сладость"]]) is not True:
    AnB +=1
if (data.loc[0,["жесткость/влажность"]] == data.loc[1,["жесткость/влажность"]]) is not True:
    AnB +=1   

if data.loc[0,["Цена($)/Кг"]] == data.loc[1,["Цена($)/Кг"]]:
    AnB =+1;
if data.loc[0,["Страна"]] == data.loc[1,["Страна"]]:
    AnB =+1;
if data.loc[0,["Регион"]] == data.loc[1,["Регион"]]:
    AnB =+1;
if data.loc[0,["Размер"]] == data.loc[1,["Размер"]]:
    AnB =+1;
if data.loc[0,["Цвет"]] == data.loc[1,["Цвет"]]:
    AnB =+1;
if data.loc[0,["Сладость"]] == data.loc[1,["Сладость"]]:
    AnB =+1;
if data.loc[0,["жесткость/влажность"]] == data.loc[1,["жесткость/влажность"]]:
    AnB =+1;


def jaccard_similarity(df1, df2):
    #Find intersection of two sets
    nominator = df1.intersection(df2)

    #Find union of two sets
    denominator = df1.union(df2)

    #Take the ratio of sizes
    similarity = len(nominator)/len(denominator)
    
    return similarity

similarity = jaccard_similarity(df1, df2)

print(similarity)
'''