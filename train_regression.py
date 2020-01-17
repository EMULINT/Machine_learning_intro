import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('properties.csv')

x=df[['area']]
y=df[['price']]

reg = linear_model.LinearRegression()
reg.fit(x,y)

print(reg.score(x,y))
print(reg.predict([[3300]]))
print(reg.coef_)
print(reg.intercept_)

from sklearn.externals import joblib
joblib.dump(reg,"linear_reg.pkl")