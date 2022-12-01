





import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


from pandas_ods_reader import read_ods

import pandas as pd

base_path = "/home/sohiab/IntelligentLab1/AILab1DataSet.ods"
sheet_index = 1

data = read_ods(base_path, 1, columns=["No.","Имя", "Цена($)/Кг","Страна","Регион","Размер","Цвет","Сладость","жесткость/влажность"])


df = pd.DataFrame(data)

corr_matrix = df.corr()
sn.heatmap(corr_matrix, annot=True)
plt.show()