import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
dataset = pd.read_csv('position_salaries.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1:].values

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

lr = LinearRegression()
lr.fit(x_poly, y)

pred = lr.predict(x_poly)
error = pred - y

plt.scatter(x, y, color='r')
plt.plot(x, pred, color='b')
plt.title(' Polynomial regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
