# Responsible for loading, cleaning, and transforming the dataset
from pandas_ods_reader import read_ods
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Global variables to store the datasets
processed_data = None
data = None
dataset_price = None
dataset_ff = None
dataset_full = None
dataset_country = None

def load_and_process_dataset():
    global processed_data, data, dataset_price, dataset_ff, dataset_full, dataset_country
    
    base_path = "/home/sohiab/Desktop/GitHubProjects/AI-Powered-Recommendation-System/AILab1DataSet.ods"
    sheet_index = 1

    # Reading the dataset
    dataset = read_ods(base_path, sheet_index, columns=["No.", "Имя", "Цена", "Страна", "Регион", "Размер", "Цвет", "Сладость", "жесткость"])
    data = pd.DataFrame(dataset)

    UpdateD = data.copy()

    # Preprocessing: Make all letters lowercase
    UpdateD['Имя'] = UpdateD['Имя'].str.lower()
    UpdateD['Страна'] = UpdateD['Страна'].str.lower()
    UpdateD['Регион'] = UpdateD['Регион'].str.lower()
    UpdateD['Размер'] = UpdateD['Размер'].str.lower()

    # Encoding categorical variables into numerical values
    labelencoder = LabelEncoder()
    UpdateD['Страна'] = labelencoder.fit_transform(UpdateD['Страна'])
    UpdateD['Регион'] = labelencoder.fit_transform(UpdateD['Регион'])
    UpdateD['Размер'] = labelencoder.fit_transform(UpdateD['Размер'])
    UpdateD['Цвет'] = labelencoder.fit_transform(UpdateD['Цвет'])
    UpdateD['Сладость'] = labelencoder.fit_transform(UpdateD['Сладость'])
    UpdateD['жесткость'] = labelencoder.fit_transform(UpdateD['жесткость'])

    # Creating datasets
    processed_data = UpdateD
    dataset_price = [[UpdateD['Имя'][i], UpdateD['Цена'][i]] for i in range(len(UpdateD))]
    dataset_ff = [[UpdateD['Имя'][i], UpdateD['Размер'][i], UpdateD['Цвет'][i], UpdateD['Сладость'][i], UpdateD['жесткость'][i]] for i in range(len(UpdateD))]
    dataset_full = [[UpdateD['Имя'][i], UpdateD['Цена'][i], UpdateD['Страна'][i], UpdateD['Регион'][i], UpdateD['Размер'][i], UpdateD['Цвет'][i], UpdateD['Сладость'][i], UpdateD['жесткость'][i]] for i in range(len(UpdateD))]
    dataset_country = [[UpdateD['Имя'][i], UpdateD['Страна'][i]] for i in range(len(UpdateD))]

# Load the dataset when the module is imported
load_and_process_dataset()
