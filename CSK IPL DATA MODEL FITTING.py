import os
os.system('cls')
import pandas as pd
import seaborn as sea
import matplotlib as plot
CSK_DATA="E:\datasets for programming\IPL DATA SET FOR MACHINE LEARNING PURPOSE.xlsx"
my_data=pd.read_excel(CSK_DATA)
my_data.columns
my_data.head(10)
my_data=my_data.dropna()
Y=my_data.CSK_ING_SCORE
CSK_KEY_POINTS=['CSK_RUNRATE','CSK_FALLEN_WICKETS','CSK_50_100','CSK_PP_SCORE','EXTRAS_BY_CSK']
X=my_data[CSK_KEY_POINTS]
X.describe()
X.head()
from sklearn.tree import DecisionTreeRegressor
my_model=DecisionTreeRegressor(random_state=123)
my_model.fit(X,Y)
