import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
sns.set(font="IPAexGothic")
import sklearn
from sklearn.linear_model import LinearRegression

df1=pd.read_excel('diabetes.xlsx')

df1.head()